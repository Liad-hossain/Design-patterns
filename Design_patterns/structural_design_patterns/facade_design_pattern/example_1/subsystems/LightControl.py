class Light:
    def turn_on(self) -> None:
        print("Lights are turned on.")

    def turn_off(self) -> None:
        print("Lights are turned off.")

    def dim(self, level: int) -> None:
        print(f"Lights are dimmed to {level}%.")
