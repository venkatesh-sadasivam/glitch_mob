from .agent import Agent

class Storyteller(Agent):
    def __init__(self, name):
        super().__init__(name, "Storyteller", "Narrative Generation", [])

class FactChecker(Agent):
    def __init__(self, name):
        super().__init__(name, "Fact Checker", "Information Verification", [])

class CodeWizard(Agent):
    def __init__(self, name):
        super().__init__(name, "Code Wizard", "Code Generation", [])

class Critic(Agent):
    def __init__(self, name):
        super().__init__(name, "Critic", "Feedback Provider", [])