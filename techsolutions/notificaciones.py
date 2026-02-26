from datetime import datetime


class GestorNotificaciones:
    """
    Gestiona todas las notificaciones automáticas del sistema.
    Usa métodos estáticos ya que no necesita estado interno.
    """

    @staticmethod
    def _timestamp() -> str:
        return datetime.now().strftime("%H:%M:%S")

    @staticmethod
    def notificar_bienvenida(cliente):
        """Se dispara automáticamente al registrar un cliente nuevo."""
        print(f"\n  📧 [NOTIF {GestorNotificaciones._timestamp()}] → {cliente.email}")
        print(f"     Bienvenido/a {cliente.nombre}, su cuenta fue creada exitosamente.")

    @staticmethod
    def notificar_cotizacion(cliente, numero: int, total: float):
        """Informa al cliente que su cotización fue generada."""
        print(f"\n  📄 [NOTIF {GestorNotificaciones._timestamp()}] → {cliente.email}")
        print(f"     Cotización #{numero} generada. Total: ${total:,.0f} COP")

    @staticmethod
    def notificar_pago_confirmado(cliente, valor: float):
        """Confirma la recepción de un pago."""
        print(f"\n  ✅ [NOTIF {GestorNotificaciones._timestamp()}] → {cliente.email}")
        print(f"     Pago de ${valor:,.0f} COP recibido. ¡Gracias por confiar en TechSolutions!")

    @staticmethod
    def notificar_recordatorio_vencimiento(cliente, servicio: str, fecha: str):
        """Recuerda al cliente una fecha de vencimiento próxima."""
        print(f"\n  ⚠️  [NOTIF {GestorNotificaciones._timestamp()}] → {cliente.email}")
        print(f"     Su servicio '{servicio}' vence el {fecha}. Renueve a tiempo.")

    @staticmethod
    def notificar_descuento_disponible(cliente, descripcion: str):
        """Comunica una promoción o descuento disponible."""
        print(f"\n  🎁 [NOTIF {GestorNotificaciones._timestamp()}] → {cliente.email}")
        print(f"     ¡Promoción disponible! {descripcion}")