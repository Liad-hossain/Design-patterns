from Design_patterns.creational_design_patterns.factory_design_pattern.example_1.factories.LinuxOperatingSystem import \
    LinuxOperatingSystem
from Design_patterns.creational_design_patterns.factory_design_pattern.example_1.factories.MacOperatingSystem import \
    MacOperatingSystem
from Design_patterns.creational_design_patterns.factory_design_pattern.example_1.factories.WindowsOperatingSystem import \
    WindowsOperatingSystem


class OperatingSystemFactory:

    def get_instance(self, name: str, version: str, architecture: str):
        if name == "Windows":
            return WindowsOperatingSystem(name, version, architecture)
        elif name == "Linux":
            return LinuxOperatingSystem(name, version, architecture)
        elif name == "Mac":
            return MacOperatingSystem(name, version, architecture)
        else:
            raise Exception("Operating system not found")


if __name__ == "__main__":

    print(
        OperatingSystemFactory()
        .get_instance("Windows", "10", "64bit")
        .get_specifications(),
    )

    print("")

    print(
        OperatingSystemFactory()
        .get_instance("Mac", "12", "64bit")
        .get_specifications(),
    )

    print("")

    print(
        OperatingSystemFactory()
        .get_instance("Linux", "18", "64bit")
        .get_specifications(),
    )

    print("")
