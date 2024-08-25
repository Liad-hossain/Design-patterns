from Design_patterns.structural_design_patterns.facade_design_pattern.example_1.subsystems.LightControl import (
    Light,
)
from Design_patterns.structural_design_patterns.facade_design_pattern.example_1.subsystems.MusicControl import (
    MusicSystem,
)
from Design_patterns.structural_design_patterns.facade_design_pattern.example_1.subsystems.SecurityControl import (
    SecurityCamera,
)
from Design_patterns.structural_design_patterns.facade_design_pattern.example_1.subsystems.ThermostatControl import (
    Thermostat,
)


class HomeAutomationFacade:
    def __init__(self):
        self.light = Light()
        self.thermostat = Thermostat()
        self.security_camera = SecurityCamera()
        self.music_system = MusicSystem()

    def good_morning_routine(self):
        print("Good Morning Routine initiated...")
        self.light.turn_on()
        self.light.dim(70)
        self.thermostat.set_temperature(28)
        self.music_system.play_music()
        self.security_camera.deactivate()

    def good_noon_routine(self):
        print("Good Noon Routine initiated...")
        self.light.turn_off()
        self.thermostat.set_temperature(22)
        self.music_system.pause_music()

    def good_afternoon_routine(self):
        print("Good Afternoon Routine initiated...")
        self.light.turn_on()
        self.light.dim(70)
        self.thermostat.set_temperature(25)

    def good_evening_routine(self):
        print("Good Evening Routine initiated...")
        self.light.dim(100)
        self.thermostat.set_temperature(27)
        self.music_system.resume_music()

    def good_night_routine(self):
        print("Good Night Routine initiated...")
        self.light.turn_off()
        self.thermostat.set_temperature(28)
        self.music_system.stop_music()
        self.security_camera.activate()


if __name__ == "__main__":
    home_automation = HomeAutomationFacade()
    home_automation.good_morning_routine()
    print("")
    home_automation.good_noon_routine()
    print("")
    home_automation.good_afternoon_routine()
    print("")
    home_automation.good_evening_routine()
    print("")
    home_automation.good_night_routine()
    print("")
