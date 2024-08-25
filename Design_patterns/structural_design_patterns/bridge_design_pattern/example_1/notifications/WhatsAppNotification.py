from Design_patterns.structural_design_patterns.bridge_design_pattern.example_1.Notification import (
    Notification,
)


class WhatsAppNotification(Notification):
    def send(self, message: str) -> str:
        return f"WhatsApp: {message}"
