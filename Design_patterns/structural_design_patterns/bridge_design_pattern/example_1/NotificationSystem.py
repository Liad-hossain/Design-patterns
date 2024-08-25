from Design_patterns.structural_design_patterns.bridge_design_pattern.example_1.notifications.EmailNotification import (
    EmailNotification,
)
from Design_patterns.structural_design_patterns.bridge_design_pattern.example_1.notifications.SMSNotification import (
    SMSNotification,
)
from Design_patterns.structural_design_patterns.bridge_design_pattern.example_1.notifications.WhatsAppNotification import (
    WhatsAppNotification,
)
from Design_patterns.structural_design_patterns.bridge_design_pattern.example_1.Platform import (
    Platform,
)
from Design_patterns.structural_design_patterns.bridge_design_pattern.example_1.platforms.LinuxPlatform import (
    LinuxPlatform,
)
from Design_patterns.structural_design_patterns.bridge_design_pattern.example_1.platforms.MacPlatform import (
    MacPlatform,
)
from Design_patterns.structural_design_patterns.bridge_design_pattern.example_1.platforms.WindowsPlatform import (
    WindowsPlatform,
)


class NOtificationSystem:
    def __init__(self, platform: Platform) -> None:
        self.platform = platform

    def deliver(self, message: str) -> str:
        return self.platform.deliver(message)


if __name__ == "__main__":
    print(
        NOtificationSystem(WindowsPlatform(WhatsAppNotification())).deliver(
            "Hello Alice!",
        ),
    )

    print("")

    print(NOtificationSystem(LinuxPlatform(EmailNotification())).deliver("Hello Bob!"))

    print("")

    print(NOtificationSystem(MacPlatform(SMSNotification())).deliver("Hello Charlie!"))

    print("")
