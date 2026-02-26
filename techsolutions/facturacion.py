from abc import ABC, abstractmethod
from datetime import datetime


# ─────────────────────────────────────────────────────────────
#  PATRÓN STRATEGY: DESCUENTOS
# ─────────────────────────────────────────────────────────────

class EstrategiaDescuento(ABC):
    """Interfaz base para todas las estrategias de descuento."""

    @abstractmethod
    def aplicar(self, total: float) -> float:
        pass

    @abstractmethod
    def descripcion(self) -> str:
        pass


class SinDescuento(EstrategiaDescuento):
    """Sin descuento aplicado."""

    def aplicar(self, total: float) -> float:
        return total

    def descripcion(self) -> str:
        return "Sin descuento"


class DescuentoEmpresa(EstrategiaDescuento):
    """15% de descuento para clientes empresariales."""

    PORCENTAJE = 0.15

    def aplicar(self, total: float) -> float:
        return total * (1 - self.PORCENTAJE)

    def descripcion(self) -> str:
        return f"Descuento empresarial ({int(self.PORCENTAJE * 100)}%)"


class DescuentoVolumen(EstrategiaDescuento):
    """10% de descuento si el total supera $1.000.000 COP."""

    UMBRAL = 1_000_000
    PORCENTAJE = 0.10

    def aplicar(self, total: float) -> float:
        if total >= self.UMBRAL:
            return total * (1 - self.PORCENTAJE)
        return total

    def descripcion(self) -> str:
        return f"Descuento por volumen ({int(self.PORCENTAJE * 100)}% sobre ${self.UMBRAL:,.0f})"


class DescuentoPromocion(EstrategiaDescuento):
    """Descuento temporal configurable para promociones especiales."""

    def __init__(self, porcentaje: float, motivo: str = "Promoción especial"):
        self.__porcentaje = porcentaje / 100
        self.__motivo = motivo

    def aplicar(self, total: float) -> float:
        return total * (1 - self.__porcentaje)

    def descripcion(self) -> str:
        return f"{self.__motivo} ({int(self.__porcentaje * 100)}%)"


# ─────────────────────────────────────────────────────────────
#  COTIZACIÓN
# ─────────────────────────────────────────────────────────────

class Cotizacion:
    """
    Genera una cotización para un cliente con uno o más servicios.
    Aplica la estrategia de descuento seleccionada.
    """

    _numero_cotizacion = 1000  # Numeración automática

    def __init__(self, cliente, descuento: EstrategiaDescuento = None):
        self.__numero = Cotizacion._numero_cotizacion
        Cotizacion._numero_cotizacion += 1
        self.__cliente = cliente
        self.__items = []  # Lista de tuplas (Servicio, cantidad)
        self.__descuento = descuento or SinDescuento()
        self.__fecha = datetime.now().strftime("%Y-%m-%d")
        self.__hora = datetime.now().strftime("%H:%M")

    @property
    def numero(self):
        return self.__numero

    @property
    def cliente(self):
        return self.__cliente

    def agregar_item(self, servicio, cantidad: int = 1):
        self.__items.append((servicio, cantidad))
        self.__cliente.agregar_servicio(servicio.nombre)

    def calcular_subtotal(self) -> float:
        return sum(servicio.calcular_costo(cantidad) for servicio, cantidad in self.__items)

    def calcular_descuento(self) -> float:
        subtotal = self.calcular_subtotal()
        return subtotal - self.__descuento.aplicar(subtotal)

    def calcular_total(self) -> float:
        return self.__descuento.aplicar(self.calcular_subtotal())

    def generar_reporte(self) -> str:
        lineas = []
        sep = "=" * 57
        guion = "-" * 57

        lineas.append(sep)
        lineas.append(f"       TECHSOLUTIONS S.A.S.")
        lineas.append(f"       COTIZACIÓN #{self.__numero}  |  Fecha: {self.__fecha}")
        lineas.append(sep)
        lineas.append(f"  Cliente  : {self.__cliente.nombre}")
        lineas.append(f"  Email    : {self.__cliente.email}")
        lineas.append(f"  Tipo     : {self.__cliente.tipo.capitalize()}")
        lineas.append(guion)
        lineas.append(f"  {'SERVICIO':<30} {'CANT':>5} {'SUBTOTAL':>14}")
        lineas.append(guion)

        for servicio, cantidad in self.__items:
            costo = servicio.calcular_costo(cantidad)
            unidad = self.__obtener_unidad(servicio)
            lineas.append(f"  {servicio.nombre:<30} {cantidad:>3}{unidad} ${costo:>12,.0f}")

        subtotal = self.calcular_subtotal()
        descuento_val = self.calcular_descuento()
        total = self.calcular_total()

        lineas.append(guion)
        lineas.append(f"  {'Subtotal':<44} ${subtotal:>11,.0f}")

        if descuento_val > 0:
            lineas.append(f"  Descuento  : {self.__descuento.descripcion()}")
            lineas.append(f"  {'Ahorro':<44} -${descuento_val:>10,.0f}")

        lineas.append(sep)
        lineas.append(f"  {'TOTAL A PAGAR':<44} ${total:>11,.0f}")
        lineas.append(sep)

        return "\n".join(lineas)

    def __obtener_unidad(self, servicio) -> str:
        """Retorna la unidad de medida según el tipo de servicio."""
        nombre = servicio.nombre
        if "Desarrollo" in nombre:
            return "h"   # horas
        elif "Soporte" in nombre:
            return "h+"  # horas extra
        elif "Consultoría" in nombre:
            return "s"   # sesiones
        elif "Auditoría" in nombre:
            return "p"   # proyectos
        return " "