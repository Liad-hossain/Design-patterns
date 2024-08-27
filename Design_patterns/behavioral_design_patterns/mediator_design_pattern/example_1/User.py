from Design_patterns.behavioral_design_patterns.mediator_design_pattern.example_1.Channel import (
    Channel,
)


class User:
    def __init__(self, name: str):
        self.name = name
        self.channels = []

    def join_channel(self, channel: Channel):
        channel.add_user(self)

    def leave_channel(self, channel: Channel):
        channel.remove_user(self)

    def send_message(self, channel: Channel, message: str):
        if channel in self.channels:
            channel.send_message(self, message)
        else:
            print(f"{self.name} is not in the {channel.name} channel.")

    def receive_message(self, sender, channel: Channel, message: str):
        print(
            f"{self.name} received a message from {sender.name} in {channel.name} channel: {message}",
        )
