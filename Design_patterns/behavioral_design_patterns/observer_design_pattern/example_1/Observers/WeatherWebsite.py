from Design_patterns.behavioral_design_patterns.observer_design_pattern.example_1.Observer import (
    Observer,
)


class WeatherWebsite(Observer):
    def update(self, temperature: float, humidity: float):
        self.display(temperature, humidity)

    def display(self, temperature: float, humidity: float):
        print(
            f"{self.name} Website - Current Weather:  {temperature}°C, Humidity: {humidity}%.",
        )
