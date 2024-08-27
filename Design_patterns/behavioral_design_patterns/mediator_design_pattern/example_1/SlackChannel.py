from Design_patterns.behavioral_design_patterns.mediator_design_pattern.example_1.Channel import (
    Channel,
)
from Design_patterns.behavioral_design_patterns.mediator_design_pattern.example_1.User import (
    User,
)


class SlackChannel(Channel):
    def add_user(self, user: User):
        self.users.append(user)
        user.channels.append(self)
        print(f"{user.name} has joined the {self.name} channel.")

    def remove_user(self, user: User):
        if user in self.users:
            self.users.remove(user)
            user.channels.remove(self)
            print(f"{user.name} has left the {self.name} channel.")

    def send_message(self, sender: User, message: str):
        if sender not in self.users:
            print(
                f"{sender.name} is not permitted to send message in {self.name} channel.",
            )
            return

        print(f"{sender.name} in {self.name} channel: {message}")
        for user in self.users:
            if user != sender:
                user.receive_message(sender, self, message)
