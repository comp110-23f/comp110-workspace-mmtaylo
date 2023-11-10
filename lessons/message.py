"""CL11 Operator Overload, Union Types, Default Parameter Examples - Class that sends someone a message."""

class Message:

    to: str | int
    content: str
    important: bool

    def __init__(self, recipient: str | int, message_content: str = "", importance_flag: bool = False):
        """Construct a message."""
        self.to = recipient
        self.content = message_content
        self.important = importance_flag

    def __str__(self) -> str:
        """Actual construction of a message."""
        output: str = f"Message to {self.to}:\n"
        output += f"Important? {self.important}\n"
        output += f'"{self.content}"'
        return output
    
    def __mul__(self, factor: int):
        """Multiplication operator overload."""
        copy_val: str = self.content
        for loop_num in range(1, factor):
            self.content += " " + copy_val


msg_to_me: Message = Message("me", "do your 110 homework!", True)
print(msg_to_me)

msg_to_you: Message = Message("you", "u r so great!")
print(msg_to_you)

msg_to_archer: Message = Message(1)
print(msg_to_archer)
msg_to_archer.content = "good boy!"
msg_to_archer.important = True
print(msg_to_archer)