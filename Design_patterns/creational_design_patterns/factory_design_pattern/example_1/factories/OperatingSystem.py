class OperatingSystem:
    def __init__(self, name: str, version: str, architecture: str) -> None:
        self.name = name
        self.version = version
        self.architecture = architecture

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> str:
        self.name = name

    def get_version(self) -> str:
        return self.version

    def set_version(self, version: str) -> str:
        self.version = version

    def get_architecture(self) -> str:
        return self.architecture

    def set_architecture(self, architecture: str) -> str:
        self.architecture = architecture
