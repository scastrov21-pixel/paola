from datetime import datetime


class Cliente:
    """Representa un cliente registrado en TechSolutions."""

    _contador_id = 1  # Auto-incremento de IDs

    def __init__(self, nombre: str, email: str, telefono: str, tipo: str = "natural"):
        self.__id = Cliente._contador_id
        Cliente._contador_id += 1
        self.__nombre = nombre
        self.__email = email
        self.__telefono = telefono
        self.__tipo = tipo  # "natural" o "empresa"
        self.__fecha_registro = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.__servicios_contratados = []

    # ── Getters (encapsulamiento) ─────────────
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
    def telefono(self):
        return self.__telefono

    @property
    def tipo(self):
        return self.__tipo

    @property
    def servicios_contratados(self):
        return self.__servicios_contratados

    # ── Métodos ───────────────────────────────
    def agregar_servicio(self, nombre_servicio: str):
        self.__servicios_contratados.append(nombre_servicio)

    def __str__(self):
        return (f"[Cliente #{self.__id}] {self.__nombre} | "
                f"Email: {self.__email} | Tel: {self.__telefono} | "
                f"Tipo: {self.__tipo} | Registrado: {self.__fecha_registro}")

    def __repr__(self):
        return f"Cliente(id={self.__id}, nombre='{self.__nombre}', tipo='{self.__tipo}')"


class RepositorioClientes:
    """
    Almacena y gestiona todos los clientes registrados.
    Actúa como una 'base de datos' en memoria.
    """

    def __init__(self):
        self.__clientes = {}  # {id: Cliente}

    def registrar(self, nombre: str, email: str, telefono: str, tipo: str = "natural") -> Cliente:
        cliente = Cliente(nombre, email, telefono, tipo)
        self.__clientes[cliente.id] = cliente
        return cliente

    def buscar_por_id(self, cliente_id: int) -> Cliente:
        return self.__clientes.get(cliente_id)

    def buscar_por_email(self, email: str) -> Cliente:
        for cliente in self.__clientes.values():
            if cliente.email == email:
                return cliente
        return None

    def listar_todos(self) -> list:
        return list(self.__clientes.values())

    def total_clientes(self) -> int:
        return len(self.__clientes)