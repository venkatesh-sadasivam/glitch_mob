class MemoryManager:
    def __init__(self):
        self.memory = {}

    def store_memory(self, agent, information):
        # Store information for an agent
        if agent not in self.memory:
            self.memory[agent] = []
        self.memory[agent].append(information)
        print(f"Memory stored for agent {agent}")

    def retrieve_memory(self, agent):
        # Retrieve stored information
        return self.memory.get(agent, [])