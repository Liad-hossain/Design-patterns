from Design_patterns.behavioral_design_patterns.observer_design_pattern.example_1.Observer import (
    Observer,
)


class SmartHomeSystem(Observer):
    def update(self, temperature: float, humidity: float) -> None:
        self.adjust_home_environment(temperature, humidity)

    def adjust_home_environment(self, temperature: float, humidity: float):
        print(
            f"{self.name} System - Adjusting home environment based on current temperature {temperature}°C and humidity {humidity}%.",
        )
