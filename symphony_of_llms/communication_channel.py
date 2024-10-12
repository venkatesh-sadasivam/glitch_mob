class CommunicationChannel:
    def __init__(self):
        self.messages = []

    def send_message(self, sender, receiver, message):
        # Send a message from one agent to another
        self.messages.append((sender, receiver, message))
        print(f"Message sent from {sender} to {receiver}: {message}")

    def receive_message(self, receiver):
        # Receive a message for an agent
        received_messages = [msg for msg in self.messages if msg[1] == receiver]
        return received_messages