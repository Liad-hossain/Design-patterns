from Design_patterns.structural_design_patterns.bridge_design_pattern.example_1.Platform import Platform


class WindowsPlatform(Platform):
    def deliver(self, message: str) -> str:
        return f"Delivering '{self.notification.send(message)}' on Windows platform"
