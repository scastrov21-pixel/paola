from clientes import RepositorioClientes
from servicios import CatalogoServicios
from facturacion import (
    Cotizacion,
    SinDescuento,
    DescuentoEmpresa,
    DescuentoVolumen,
    DescuentoPromocion
)
from notificaciones import GestorNotificaciones


# ─────────────────────────────────────────────────────────────
#  UTILIDADES DE CONSOLA
# ─────────────────────────────────────────────────────────────

def titulo(texto: str):
    print("\n" + "═" * 55)
    print(f"   {texto}")
    print("═" * 55)

def subtitulo(texto: str):
    print(f"\n  ── {texto} ──")

def pausar():
    input("\n  Presione ENTER para continuar...")

def pedir_texto(mensaje: str) -> str:
    while True:
        valor = input(f"  {mensaje}: ").strip()
        if valor:
            return valor
        print("  ⚠ El campo no puede estar vacío.")

def pedir_entero(mensaje: str, minimo: int = 0, maximo: int = 9999) -> int:
    while True:
        try:
            valor = int(input(f"  {mensaje}: "))
            if minimo <= valor <= maximo:
                return valor
            print(f"  ⚠ Ingrese un número entre {minimo} y {maximo}.")
        except ValueError:
            print("  ⚠ Ingrese un número válido.")

def pedir_float(mensaje: str, minimo: float = 0) -> float:
    while True:
        try:
            valor = float(input(f"  {mensaje}: "))
            if valor >= minimo:
                return valor
            print(f"  ⚠ Ingrese un valor mayor a {minimo}.")
        except ValueError:
            print("  ⚠ Ingrese un número válido.")


# ─────────────────────────────────────────────────────────────
#  CLASE MENÚ PRINCIPAL
# ─────────────────────────────────────────────────────────────

class MenuTechSolutions:
    """Controlador del menú interactivo del sistema."""

    def __init__(self):
        self.repositorio  = RepositorioClientes()
        self.catalogo     = CatalogoServicios()
        self.notif        = GestorNotificaciones()
        self.cotizaciones = []  # historial de cotizaciones

    # ──────────────────────────────────────────────────
    #  MENÚ PRINCIPAL
    #───────────────────────────────────────────────────

    def iniciar(self):
        while True:
            titulo("TECHSOLUTIONS S.A.S. — Sistema de Gestión")
            print("""
   [1]  Gestión de Clientes
   [2]  Ver Catálogo de Servicios
   [3]  Crear Cotización
   [4]  Historial de Cotizaciones
   [5]  Enviar Notificación
   [0]  Salir
            """)
            opcion = input("  Seleccione una opción: ").strip()

            if opcion == "1":
                self.menu_clientes()
            elif opcion == "2":
                self.ver_catalogo()
            elif opcion == "3":
                self.menu_cotizacion()
            elif opcion == "4":
                self.ver_historial()
            elif opcion == "5":
                self.menu_notificaciones()
            elif opcion == "0":
                print("\n  ¡Hasta luego! — TechSolutions S.A.S.\n")
                break
            else:
                print("  ⚠ Opción inválida. Intente de nuevo.")

    # ─────────────────────────────────────────────────────────────
    #  SUBMENÚ: CLIENTES
    # ─────────────────────────────────────────────────────────────

    def menu_clientes(self):
        while True:
            titulo("GESTIÓN DE CLIENTES")
            print("""
   [1]  Registrar nuevo cliente
   [2]  Ver todos los clientes
   [3]  Buscar cliente por ID
   [4]  Buscar cliente por email
   [0]  Volver al menú principal
            """)
            opcion = input("  Seleccione una opción: ").strip()

            if opcion == "1":
                self.registrar_cliente()
            elif opcion == "2":
                self.listar_clientes()
            elif opcion == "3":
                self.buscar_cliente_id()
            elif opcion == "4":
                self.buscar_cliente_email()
            elif opcion == "0":
                break
            else:
                print("  ⚠ Opción inválida.")

    def registrar_cliente(self):
        titulo("REGISTRAR NUEVO CLIENTE")
        nombre   = pedir_texto("Nombre completo")
        email    = pedir_texto("Correo electrónico")
        telefono = pedir_texto("Teléfono")

        print("\n  Tipo de cliente:")
        print("   [1]  Persona natural")
        print("   [2]  Empresa")
        tipo_op = input("  Seleccione: ").strip()
        tipo = "empresa" if tipo_op == "2" else "natural"

        cliente = self.repositorio.registrar(nombre, email, telefono, tipo)
        self.notif.notificar_bienvenida(cliente)
        print(f"\n  ✔ Cliente registrado exitosamente.")
        print(f"  {cliente}")
        pausar()

    def listar_clientes(self):
        titulo("CLIENTES REGISTRADOS")
        clientes = self.repositorio.listar_todos()
        if not clientes:
            print("  ⚠ No hay clientes registrados aún.")
        else:
            for c in clientes:
                print(f"  {c}")
            print(f"\n  Total: {self.repositorio.total_clientes()} cliente(s)")
        pausar()

    def buscar_cliente_id(self):
        titulo("BUSCAR CLIENTE POR ID")
        id_buscar = pedir_entero("Ingrese el ID del cliente", 1)
        cliente = self.repositorio.buscar_por_id(id_buscar)
        if cliente:
            print(f"\n  ✔ Cliente encontrado:")
            print(f"  {cliente}")
            if cliente.servicios_contratados:
                print(f"  Servicios: {', '.join(cliente.servicios_contratados)}")
        else:
            print(f"  ✗ No se encontró cliente con ID #{id_buscar}.")
        pausar()

    def buscar_cliente_email(self):
        titulo("BUSCAR CLIENTE POR EMAIL")
        email = pedir_texto("Ingrese el email")
        cliente = self.repositorio.buscar_por_email(email)
        if cliente:
            print(f"\n  ✔ Cliente encontrado:")
            print(f"  {cliente}")
        else:
            print(f"  ✗ No se encontró cliente con ese email.")
        pausar()

    # ─────────────────────────────────────────────────────────────
    #  VER CATÁLOGO
    # ─────────────────────────────────────────────────────────────

    def ver_catalogo(self):
        titulo("CATÁLOGO DE SERVICIOS")
        self.catalogo.listar()
        pausar()

    # ─────────────────────────────────────────────────────────────
    #  SUBMENÚ: COTIZACIÓN
    # ─────────────────────────────────────────────────────────────

    def menu_cotizacion(self):
        titulo("CREAR COTIZACIÓN")

        if self.repositorio.total_clientes() == 0:
            print("  ⚠ Primero debe registrar al menos un cliente.")
            pausar()
            return

        # Seleccionar cliente
        subtitulo("Paso 1 — Seleccionar cliente")
        self._listar_clientes_compacto()
        cliente_id = pedir_entero("ID del cliente", 1)
        cliente = self.repositorio.buscar_por_id(cliente_id)

        if not cliente:
            print("  ✗ Cliente no encontrado.")
            pausar()
            return

        print(f"\n  ✔ Cliente: {cliente.nombre} | Tipo: {cliente.tipo}")

        # Seleccionar descuento
        subtitulo("Paso 2 — Seleccionar descuento")
        descuento = self._seleccionar_descuento(cliente)

        # Agregar servicios
        subtitulo("Paso 3 — Agregar servicios")
        cotizacion = Cotizacion(cliente, descuento)
        self._agregar_servicios(cotizacion)

        # Resultado final
        print("\n" + cotizacion.generar_reporte())
        self.notif.notificar_cotizacion(cliente, cotizacion.numero, cotizacion.calcular_total())
        self.cotizaciones.append(cotizacion)
        print(f"\n  ✔ Cotización #{cotizacion.numero} guardada en historial.")
        pausar()

    def _listar_clientes_compacto(self):
        for c in self.repositorio.listar_todos():
            print(f"   ID #{c.id:<3} → {c.nombre} ({c.tipo})")

    def _seleccionar_descuento(self, cliente):
        print("   [1]  Sin descuento")
        print("   [2]  Empresarial     → 15% de descuento")
        print("   [3]  Por volumen     → 10% si total > $1.000.000")
        print("   [4]  Promoción       → % personalizado")

        if cliente.tipo == "empresa":
            print(f"\n  💡 Sugerencia: opción [2] por ser cliente empresa.")

        op = input("\n  Tipo de descuento: ").strip()

        if op == "2":
            return DescuentoEmpresa()
        elif op == "3":
            return DescuentoVolumen()
        elif op == "4":
            pct    = pedir_float("Porcentaje de descuento (ej: 20 para 20%)", 1)
            motivo = pedir_texto("Nombre de la promoción")
            return DescuentoPromocion(pct, motivo)
        else:
            return SinDescuento()

    def _agregar_servicios(self, cotizacion: Cotizacion):
        self.catalogo.listar()
        print("\n  Agregue servicios uno a uno. Escriba [0] cuando termine.")

        while True:
            op = input("\n  Código del servicio (1-4) o [0] para terminar: ").strip()

            if op == "0":
                if not cotizacion._Cotizacion__items:
                    print("  ⚠ Debe agregar al menos un servicio.")
                    continue
                break

            servicio = self.catalogo.obtener(op)
            if not servicio:
                print("  ⚠ Código inválido. Use 1, 2, 3 o 4.")
                continue

            etiqueta = self._etiqueta_cantidad(servicio)
            cantidad = pedir_entero(f"Cantidad ({etiqueta})", 0)
            cotizacion.agregar_item(servicio, cantidad)

            subtotal = servicio.calcular_costo(cantidad)
            print(f"  ✔ {servicio.nombre} × {cantidad} {etiqueta} = ${subtotal:,.0f}")

    def _etiqueta_cantidad(self, servicio) -> str:
        nombre = servicio.nombre
        if "Desarrollo" in nombre:
            return "horas"
        elif "Soporte" in nombre:
            return "horas extra  (0 = solo plan mensual $350.000)"
        elif "Consultoría" in nombre:
            return "sesiones"
        elif "Auditoría" in nombre:
            return "proyectos"
        return "unidades"

    # ─────────────────────────────────────────────────────────────
    #  HISTORIAL DE COTIZACIONES
    # ─────────────────────────────────────────────────────────────

    def ver_historial(self):
        titulo("HISTORIAL DE COTIZACIONES")

        if not self.cotizaciones:
            print("  ⚠ Aún no se han generado cotizaciones.")
            pausar()
            return

        print(f"\n  {'#':<8} {'CLIENTE':<26} {'TOTAL':>14}")
        print("  " + "─" * 50)
        for cot in self.cotizaciones:
            print(f"  #{cot.numero:<7} {cot.cliente.nombre:<26} ${cot.calcular_total():>12,.0f}")

        print(f"\n  Total generadas: {len(self.cotizaciones)} cotización(es)")

        ver = input("\n  Ver detalle — ingrese número de cotización (o ENTER para omitir): ").strip()
        if ver:
            try:
                num = int(ver)
                cot = next((c for c in self.cotizaciones if c.numero == num), None)
                if cot:
                    print("\n" + cot.generar_reporte())
                else:
                    print("  ✗ Cotización no encontrada.")
            except ValueError:
                pass

        pausar()

    # ─────────────────────────────────────────────────────────────
    #  SUBMENÚ: NOTIFICACIONES
    # ─────────────────────────────────────────────────────────────

    def menu_notificaciones(self):
        titulo("ENVIAR NOTIFICACIÓN")

        if self.repositorio.total_clientes() == 0:
            print("  ⚠ No hay clientes registrados.")
            pausar()
            return

        print("""
   [1]  Confirmación de pago
   [2]  Recordatorio de vencimiento
   [3]  Descuento o promoción disponible
   [0]  Volver
        """)
        op = input("  Tipo de notificación: ").strip()

        if op == "0":
            return

        subtitulo("Seleccionar cliente destino")
        self._listar_clientes_compacto()
        cliente_id = pedir_entero("ID del cliente", 1)
        cliente = self.repositorio.buscar_por_id(cliente_id)

        if not cliente:
            print("  ✗ Cliente no encontrado.")
            pausar()
            return

        if op == "1":
            valor = pedir_float("Valor recibido ($)", 1)
            self.notif.notificar_pago_confirmado(cliente, valor)

        elif op == "2":
            servicio = pedir_texto("Nombre del servicio")
            fecha    = pedir_texto("Fecha de vencimiento (ej: 2026-12-31)")
            self.notif.notificar_recordatorio_vencimiento(cliente, servicio, fecha)

        elif op == "3":
            desc = pedir_texto("Descripción de la promoción")
            self.notif.notificar_descuento_disponible(cliente, desc)

        else:
            print("  ⚠ Opción inválida.")

        pausar()


# ─────────────────────────────────────────────────────────────
#  PUNTO DE ENTRADA
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    menu = MenuTechSolutions()
    menu.iniciar()