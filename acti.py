"""
================================================================
  TECHSOLUTIONS S.A.S. - Sistema de Gestión de Servicios
  Proyecto de Grado - Programación Orientada a Objetos
  Estudiante: [Tu nombre] | Semestre 5
================================================================
  Conceptos aplicados:
    - Clases y Objetos
    - Herencia y Polimorfismo
    - Encapsulamiento
    - Métodos especiales (__str__, __repr__)
    - Módulos y separación de responsabilidades
    - Patrón de diseño: Strategy (descuentos)
    - Notificaciones automáticas
================================================================
"""

from datetime import datetime
from abc import ABC, abstractmethod


# ─────────────────────────────────────────────
#  MÓDULO 1: CLIENTES
# ─────────────────────────────────────────────

class Cliente:
    """Representa un cliente registrado en TechSolutions."""

    # Contador automático de IDs
    _contador_id = 1

    def __init__(self, nombre: str, email: str, telefono: str, tipo: str = "natural"):
        self.__id = Cliente._contador_id
        Cliente._contador_id += 1
        self.__nombre = nombre
        self.__email = email
        self.__telefono = telefono
        self.__tipo = tipo  # "natural" o "empresa"
        self.__fecha_registro = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.__servicios_contratados = []

    # ── Getters ──────────────────────────────
    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre

    @property
    def email(self):
        return self.__email

    @property
    def tipo(self):
        return self.__tipo

    @property
    def servicios_contratados(self):
        return self.__servicios_contratados

    # ── Métodos ──────────────────────────────
    def agregar_servicio(self, servicio):
        self.__servicios_contratados.append(servicio)

    def __str__(self):
        return (f"[Cliente #{self.__id}] {self.__nombre} | "
                f"{self.__email} | Tipo: {self.__tipo} | "
                f"Registrado: {self.__fecha_registro}")


# ─────────────────────────────────────────────
#  MÓDULO 2: SERVICIOS (Herencia)
# ─────────────────────────────────────────────

class Servicio(ABC):
    """Clase base abstracta para todos los servicios de TechSolutions."""

    def __init__(self, nombre: str, descripcion: str, precio_base: float):
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__precio_base = precio_base

    @property
    def nombre(self):
        return self.__nombre

    @property
    def descripcion(self):
        return self.__descripcion

    @property
    def precio_base(self):
        return self.__precio_base

    @abstractmethod
    def calcular_costo(self, horas: int = 1) -> float:
        """Cada servicio calcula su costo de forma distinta (polimorfismo)."""
        pass

    def __str__(self):
        return f"{self.__nombre} - Precio base: ${self.__precio_base:,.0f}"


class DesarrolloSoftware(Servicio):
    """Servicio de desarrollo de software. Cobra por hora."""

    TARIFA_HORA = 85_000  # COP por hora

    def __init__(self):
        super().__init__(
            nombre="Desarrollo de Software",
            descripcion="Diseño, desarrollo e implementación de aplicaciones a medida",
            precio_base=self.TARIFA_HORA
        )

    def calcular_costo(self, horas: int = 1) -> float:
        return horas * self.TARIFA_HORA


class SoporteTecnico(Servicio):
    """Servicio de soporte. Precio fijo mensual + cargo por hora extra."""

    PRECIO_MENSUAL = 350_000
    CARGO_HORA_EXTRA = 40_000

    def __init__(self):
        super().__init__(
            nombre="Soporte Técnico",
            descripcion="Asistencia técnica remota y presencial 8x5",
            precio_base=self.PRECIO_MENSUAL
        )

    def calcular_costo(self, horas: int = 0) -> float:
        return self.PRECIO_MENSUAL + (horas * self.CARGO_HORA_EXTRA)


class Consultoria(Servicio):
    """Servicio de consultoría. Tarifa por sesión."""

    PRECIO_SESION = 200_000

    def __init__(self):
        super().__init__(
            nombre="Consultoría",
            descripcion="Asesoría estratégica en transformación digital",
            precio_base=self.PRECIO_SESION
        )

    def calcular_costo(self, horas: int = 1) -> float:
        # Las sesiones se cuentan como 'horas' aquí (sesiones)
        return horas * self.PRECIO_SESION


class AuditoriaQA(Servicio):
    """Auditoría de calidad. Precio fijo por proyecto."""

    PRECIO_PROYECTO = 1_200_000

    def __init__(self):
        super().__init__(
            nombre="Auditoría QA",
            descripcion="Revisión y pruebas de calidad del software",
            precio_base=self.PRECIO_PROYECTO
        )

    def calcular_costo(self, horas: int = 1) -> float:
        # Cobro por cantidad de proyectos (reutilizamos el parámetro)
        return horas * self.PRECIO_PROYECTO


# ─────────────────────────────────────────────
#  MÓDULO 3: DESCUENTOS (Patrón Strategy)
# ─────────────────────────────────────────────

class EstrategiaDescuento(ABC):
    """Interfaz base para estrategias de descuento."""

    @abstractmethod
    def aplicar(self, total: float) -> float:
        pass

    @abstractmethod
    def descripcion(self) -> str:
        pass


class SinDescuento(EstrategiaDescuento):
    def aplicar(self, total: float) -> float:
        return total

    def descripcion(self) -> str:
        return "Sin descuento"


class DescuentoEmpresa(EstrategiaDescuento):
    """15% para clientes empresariales."""

    PORCENTAJE = 0.15

    def aplicar(self, total: float) -> float:
        return total * (1 - self.PORCENTAJE)

    def descripcion(self) -> str:
        return f"Descuento empresarial ({int(self.PORCENTAJE*100)}%)"


class DescuentoVolumen(EstrategiaDescuento):
    """10% si el total supera $1.000.000 COP."""

    UMBRAL = 1_000_000
    PORCENTAJE = 0.10

    def aplicar(self, total: float) -> float:
        if total >= self.UMBRAL:
            return total * (1 - self.PORCENTAJE)
        return total

    def descripcion(self) -> str:
        return f"Descuento por volumen ({int(self.PORCENTAJE*100)}% si > $1.000.000)"


class DescuentoPromocion(EstrategiaDescuento):
    """Descuento temporal configurable."""

    def __init__(self, porcentaje: float, motivo: str = "Promoción especial"):
        self.__porcentaje = porcentaje / 100
        self.__motivo = motivo

    def aplicar(self, total: float) -> float:
        return total * (1 - self.__porcentaje)

    def descripcion(self) -> str:
        return f"{self.__motivo} ({int(self.__porcentaje*100)}%)"


# ─────────────────────────────────────────────
#  MÓDULO 4: COTIZACIÓN / FACTURA
# ─────────────────────────────────────────────

class Cotizacion:
    """Genera cotizaciones para un cliente con varios servicios."""

    _numero = 1000

    def __init__(self, cliente: Cliente, descuento: EstrategiaDescuento = None):
        self.__numero = Cotizacion._numero
        Cotizacion._numero += 1
        self.__cliente = cliente
        self.__items = []  # lista de (Servicio, cantidad)
        self.__descuento = descuento or SinDescuento()
        self.__fecha = datetime.now().strftime("%Y-%m-%d")

    def agregar_item(self, servicio: Servicio, cantidad: int = 1):
        self.__items.append((servicio, cantidad))

    def calcular_subtotal(self) -> float:
        return sum(s.calcular_costo(c) for s, c in self.__items)

    def calcular_total(self) -> float:
        return self.__descuento.aplicar(self.calcular_subtotal())

    def generar_reporte(self) -> str:
        lineas = []
        lineas.append("=" * 55)
        lineas.append(f"     TECHSOLUTIONS S.A.S. - COTIZACIÓN #{self.__numero}")
        lineas.append("=" * 55)
        lineas.append(f"  Fecha    : {self.__fecha}")
        lineas.append(f"  Cliente  : {self.__cliente.nombre}")
        lineas.append(f"  Email    : {self.__cliente.email}")
        lineas.append("-" * 55)
        lineas.append(f"  {'SERVICIO':<28} {'CANT':>4} {'VALOR':>12}")
        lineas.append("-" * 55)

        for servicio, cantidad in self.__items:
            costo = servicio.calcular_costo(cantidad)
            lineas.append(f"  {servicio.nombre:<28} {cantidad:>4} ${costo:>11,.0f}")

        lineas.append("-" * 55)
        subtotal = self.calcular_subtotal()
        total = self.calcular_total()
        ahorro = subtotal - total

        lineas.append(f"  {'Subtotal':<40} ${subtotal:>11,.0f}")

        if ahorro > 0:
            lineas.append(f"  Descuento: {self.__descuento.descripcion()}")
            lineas.append(f"  {'Ahorro':<40} -${ahorro:>10,.0f}")

        lineas.append("=" * 55)
        lineas.append(f"  {'TOTAL A PAGAR':<40} ${total:>11,.0f}")
        lineas.append("=" * 55)

        return "\n".join(lineas)


# ─────────────────────────────────────────────
#  MÓDULO 5: NOTIFICACIONES AUTOMÁTICAS
# ─────────────────────────────────────────────

class GestorNotificaciones:
    """
    Simula el envío de notificaciones automáticas.
    En producción se conectaría con SMTP / WhatsApp API / SMS.
    """

    @staticmethod
    def notificar_bienvenida(cliente: Cliente):
        print(f"\n📧 [NOTIFICACIÓN] Bienvenida enviada a: {cliente.email}")
        print(f"   Estimado/a {cliente.nombre}, su cuenta ha sido creada exitosamente.")

    @staticmethod
    def notificar_cotizacion(cliente: Cliente, numero_cotizacion: int, total: float):
        print(f"\n📧 [NOTIFICACIÓN] Cotización #{numero_cotizacion} enviada a: {cliente.email}")
        print(f"   Total de la cotización: ${total:,.0f} COP")

    @staticmethod
    def notificar_pago(cliente: Cliente, valor: float):
        print(f"\n✅ [NOTIFICACIÓN] Confirmación de pago enviada a: {cliente.email}")
        print(f"   Valor recibido: ${valor:,.0f} COP. ¡Gracias por confiar en TechSolutions!")

    @staticmethod
    def notificar_recordatorio(cliente: Cliente, servicio: str, fecha_vencimiento: str):
        print(f"\n⚠️  [RECORDATORIO] Aviso enviado a: {cliente.email}")
        print(f"   Su servicio '{servicio}' vence el {fecha_vencimiento}.")


# ─────────────────────────────────────────────
#  MÓDULO 6: SISTEMA PRINCIPAL (Menú)
# ─────────────────────────────────────────────

class SistemaTechSolutions:
    """Controlador principal del sistema."""

    def __init__(self):
        self.__clientes = {}
        self.__notificador = GestorNotificaciones()
        # Catálogo de servicios disponibles
        self.__catalogo = {
            "1": DesarrolloSoftware(),
            "2": SoporteTecnico(),
            "3": Consultoria(),
            "4": AuditoriaQA(),
        }

    # ── Registro de cliente ──────────────────
    def registrar_cliente(self, nombre, email, telefono, tipo="natural"):
        cliente = Cliente(nombre, email, telefono, tipo)
        self.__clientes[cliente.id] = cliente
        self.__notificador.notificar_bienvenida(cliente)
        print(f"\n✔ Cliente registrado: {cliente}")
        return cliente

    # ── Ver clientes ─────────────────────────
    def listar_clientes(self):
        if not self.__clientes:
            print("\n⚠ No hay clientes registrados.")
            return
        print("\n── CLIENTES REGISTRADOS ──────────────────")
        for c in self.__clientes.values():
            print(f"  {c}")

    # ── Ver catálogo ─────────────────────────
    def mostrar_catalogo(self):
        print("\n── CATÁLOGO DE SERVICIOS ─────────────────")
        for key, servicio in self.__catalogo.items():
            print(f"  [{key}] {servicio}")

    # ── Crear cotización ─────────────────────
    def crear_cotizacion(self, cliente_id: int, items: list, tipo_descuento: str = "ninguno"):
        cliente = self.__clientes.get(cliente_id)
        if not cliente:
            print("❌ Cliente no encontrado.")
            return

        # Elegir descuento
        descuentos = {
            "empresa":   DescuentoEmpresa(),
            "volumen":   DescuentoVolumen(),
            "ninguno":   SinDescuento(),
        }
        descuento = descuentos.get(tipo_descuento, SinDescuento())

        cotizacion = Cotizacion(cliente, descuento)

        for codigo_servicio, cantidad in items:
            servicio = self.__catalogo.get(str(codigo_servicio))
            if servicio:
                cotizacion.agregar_item(servicio, cantidad)
                cliente.agregar_servicio(servicio.nombre)

        print("\n" + cotizacion.generar_reporte())

        self.__notificador.notificar_cotizacion(
            cliente,
            numero_cotizacion=cotizacion._Cotizacion__numero,
            total=cotizacion.calcular_total()
        )
        return cotizacion


# ─────────────────────────────────────────────
#  DEMO / PRUEBA DEL SISTEMA
# ─────────────────────────────────────────────

if __name__ == "__main__":

    print("=" * 55)
    print("  TECHSOLUTIONS S.A.S. — Sistema de Gestión")
    print("=" * 55)

    sistema = SistemaTechSolutions()

    # 1. Registrar clientes
    print("\n──── REGISTRANDO CLIENTES ────")
    cliente1 = sistema.registrar_cliente(
        nombre="Carlos Mendoza",
        email="carlos.mendoza@gmail.com",
        telefono="3001234567",
        tipo="natural"
    )

    cliente2 = sistema.registrar_cliente(
        nombre="Grupo Empresarial XYZ",
        email="contacto@grupoXYZ.com",
        telefono="6017654321",
        tipo="empresa"
    )

    # 2. Ver clientes
    print("\n──── LISTA DE CLIENTES ────")
    sistema.listar_clientes()

    # 3. Ver catálogo
    sistema.mostrar_catalogo()

    # 4. Crear cotización cliente natural (sin descuento)
    print("\n──── COTIZACIÓN CLIENTE NATURAL ────")
    sistema.crear_cotizacion(
        cliente_id=cliente1.id,
        items=[
            ("1", 20),  # Desarrollo: 20 horas
            ("2", 2),   # Soporte: 2 horas extra
        ],
        tipo_descuento="ninguno"
    )

    # 5. Crear cotización empresa (con descuento empresa)
    print("\n──── COTIZACIÓN EMPRESA ────")
    sistema.crear_cotizacion(
        cliente_id=cliente2.id,
        items=[
            ("1", 40),  # Desarrollo: 40 horas
            ("3", 3),   # Consultoría: 3 sesiones
            ("4", 2),   # Auditoría QA: 2 proyectos
        ],
        tipo_descuento="empresa"
    )

    # 6. Notificaciones manuales
    print("\n──── NOTIFICACIONES ────")
    GestorNotificaciones.notificar_pago(cliente2, 3_808_000)
    GestorNotificaciones.notificar_recordatorio(
        cliente1,
        servicio="Soporte Técnico",
        fecha_vencimiento="2025-03-31"
    )

    # 7. Probar descuento promoción especial
    print("\n──── COTIZACIÓN CON PROMOCIÓN ESPECIAL ────")
    from techsolutions_sistema import Cotizacion, DescuentoPromocion

    cotiz_promo = Cotizacion(cliente1, DescuentoPromocion(20, "Descuento lanzamiento"))
    cotiz_promo.agregar_item(SoporteTecnico(), 0)
    cotiz_promo.agregar_item(Consultoria(), 2)
    print(cotiz_promo.generar_reporte())

    print("\n✅ Sistema ejecutado correctamente.")