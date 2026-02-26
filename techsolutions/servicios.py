from abc import ABC, abstractmethod


# ─────────────────────────────────────────────────────────────
#  CLASE BASE ABSTRACTA
# ─────────────────────────────────────────────────────────────

class Servicio(ABC):
    """
    Clase base para todos los servicios de TechSolutions.
    No se puede instanciar directamente.
    """

    def __init__(self, nombre: str, descripcion: str, precio_base: float):
        self._nombre = nombre
        self._descripcion = descripcion
        self._precio_base = precio_base

    @property
    def nombre(self):
        return self._nombre

    @property
    def descripcion(self):
        return self._descripcion

    @property
    def precio_base(self):
        return self._precio_base

    @abstractmethod
    def calcular_costo(self, cantidad: int = 1) -> float:
        """
        Método abstracto: cada subclase define cómo calcula su costo.
        Esto es polimorfismo en acción.
        """
        pass

    def __str__(self):
        return f"{self._nombre} | Precio base: ${self._precio_base:,.0f} | {self._descripcion}"

    def __repr__(self):
        return f"{self.__class__.__name__}(precio_base={self._precio_base})"


# ─────────────────────────────────────────────────────────────
#  SUBCLASES (Herencia de Servicio)
# ─────────────────────────────────────────────────────────────

class DesarrolloSoftware(Servicio):
    """
    Servicio de desarrollo de software.
    Se cobra por hora trabajada.
    """

    TARIFA_HORA = 85_000  # COP por hora

    def __init__(self):
        super().__init__(
            nombre="Desarrollo de Software",
            descripcion="Diseño, desarrollo e implementación de aplicaciones a medida",
            precio_base=self.TARIFA_HORA
        )

    def calcular_costo(self, cantidad: int = 1) -> float:
        """cantidad = número de horas"""
        return cantidad * self.TARIFA_HORA


class SoporteTecnico(Servicio):
    """
    Servicio de soporte técnico.
    Precio fijo mensual + cargo por cada hora extra.
    """

    PRECIO_MENSUAL = 350_000
    CARGO_HORA_EXTRA = 40_000

    def __init__(self):
        super().__init__(
            nombre="Soporte Técnico",
            descripcion="Asistencia técnica remota y presencial 8x5",
            precio_base=self.PRECIO_MENSUAL
        )

    def calcular_costo(self, cantidad: int = 0) -> float:
        """cantidad = horas extra sobre el plan mensual"""
        return self.PRECIO_MENSUAL + (cantidad * self.CARGO_HORA_EXTRA)


class Consultoria(Servicio):
    """
    Servicio de consultoría estratégica.
    Se cobra por sesión realizada.
    """

    PRECIO_SESION = 200_000

    def __init__(self):
        super().__init__(
            nombre="Consultoría",
            descripcion="Asesoría estratégica en transformación digital y procesos",
            precio_base=self.PRECIO_SESION
        )

    def calcular_costo(self, cantidad: int = 1) -> float:
        """cantidad = número de sesiones"""
        return cantidad * self.PRECIO_SESION


class AuditoriaQA(Servicio):
    """
    Auditoría de calidad de software.
    Se cobra por proyecto auditado.
    """

    PRECIO_PROYECTO = 1_200_000

    def __init__(self):
        super().__init__(
            nombre="Auditoría QA",
            descripcion="Revisión, pruebas y certificación de calidad del software",
            precio_base=self.PRECIO_PROYECTO
        )

    def calcular_costo(self, cantidad: int = 1) -> float:
        """cantidad = número de proyectos auditados"""
        return cantidad * self.PRECIO_PROYECTO


# ─────────────────────────────────────────────────────────────
#  CATÁLOGO DE SERVICIOS
# ─────────────────────────────────────────────────────────────

class CatalogoServicios:
    """Gestiona el catálogo completo de servicios disponibles."""

    def __init__(self):
        self.__servicios = {
            "1": DesarrolloSoftware(),
            "2": SoporteTecnico(),
            "3": Consultoria(),
            "4": AuditoriaQA(),
        }

    def obtener(self, codigo: str) -> Servicio:
        return self.__servicios.get(str(codigo))

    def listar(self):
        print("\n── CATÁLOGO DE SERVICIOS ─────────────────────────")
        for codigo, servicio in self.__servicios.items():
            print(f"  [{codigo}] {servicio}")

    def todos(self) -> dict:
        return self.__servicios