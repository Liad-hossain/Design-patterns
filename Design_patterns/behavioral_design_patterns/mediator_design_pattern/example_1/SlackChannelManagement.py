from Design_patterns.behavioral_design_patterns.mediator_design_pattern.example_1.SlackChannel import (
    SlackChannel,
)
from Design_patterns.behavioral_design_patterns.mediator_design_pattern.example_1.User import (
    User,
)

if __name__ == "__main__":
    general_channel = SlackChannel("general")
    random_channel = SlackChannel("random")
    dev_channel = SlackChannel("development")

    alice = User("Alice")
    bob = User("Bob")
    charlie = User("Charlie")

    alice.join_channel(general_channel)
    alice.join_channel(dev_channel)

    bob.join_channel(general_channel)
    bob.join_channel(random_channel)

    charlie.join_channel(random_channel)
    charlie.join_channel(dev_channel)

    alice.send_message(general_channel, "Hi everyone in general!")
    bob.send_message(random_channel, "Hey, anyone here?")
    charlie.send_message(dev_channel, "Development is going well!")

    alice.leave_channel(general_channel)
    bob.send_message(
        random_channel,
        "Why did Alice leave from general? Charlie can you help?",
    )
    charlie.send_message(dev_channel, "Why did Alice leave from general?")
