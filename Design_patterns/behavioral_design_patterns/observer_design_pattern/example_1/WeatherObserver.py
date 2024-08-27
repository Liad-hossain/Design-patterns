from Design_patterns.behavioral_design_patterns.observer_design_pattern.example_1.Observers.NewsApp import (
    NewsApp,
)
from Design_patterns.behavioral_design_patterns.observer_design_pattern.example_1.Observers.SmartHome import (
    SmartHomeSystem,
)
from Design_patterns.behavioral_design_patterns.observer_design_pattern.example_1.Observers.WeatherWebsite import (
    WeatherWebsite,
)
from Design_patterns.behavioral_design_patterns.observer_design_pattern.example_1.WeatherStation import (
    WeatherStation,
)

if __name__ == "__main__":
    weather_station = WeatherStation()

    news_app = NewsApp("Global News")
    weather_website = WeatherWebsite("WeatherTracker")
    smart_home_system = SmartHomeSystem("SmartHome AI")

    weather_station.register_observer(news_app)
    weather_station.register_observer(weather_website)
    weather_station.register_observer(smart_home_system)

    weather_station.set_measurements(25, 60)  # Update temperature and humidity
    weather_station.set_measurements(22, 65)  # Update with new data

    weather_station.remove_observer(news_app)  # Remove one observer
    weather_station.set_measurements(20, 70)  # Update temperature and humidity again
