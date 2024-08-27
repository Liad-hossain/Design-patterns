from Design_patterns.behavioral_design_patterns.observer_design_pattern.example_1.Observer import (
    Observer,
)


class NewsApp(Observer):
    def update(self, temperature: float, humidity: float) -> None:
        self.display(temperature, humidity)

    def display(self, temperature: float, humidity: float) -> None:
        print(
            f"{self.name} App - Breaking News: The temperature is {temperature}°C and the humidity is {humidity}%.",
        )
