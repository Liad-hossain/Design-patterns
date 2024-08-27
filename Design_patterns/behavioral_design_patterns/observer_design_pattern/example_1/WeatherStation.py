from Design_patterns.behavioral_design_patterns.observer_design_pattern.example_1.Observer import (
    Observer,
)


class WeatherStation:
    def __init__(self):
        self._observers = []
        self._temperature = None
        self._humidity = None

    def register_observer(self, observer: Observer) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update(self._temperature, self._humidity)

    def set_measurements(self, temperature: float, humidity: float) -> None:
        self._temperature = temperature
        self._humidity = humidity
        self.notify_observers()
