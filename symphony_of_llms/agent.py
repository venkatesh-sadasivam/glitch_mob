from dataclasses import dataclass

@dataclass
class Agent:
    name: str
    persona: str
    role: str
    objectives: list

    def activate(self):
        # Activate the agent for interaction
        print(f"Activating agent {self.name}")

    def terminate(self):
        # Terminate the agent's lifecycle
        print(f"Terminating agent {self.name}")