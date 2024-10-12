class RoleManager:
    def assign_role(self, agent, role):
        # Assign a new role to an agent
        agent.role = role
        print(f"Role '{role}' assigned to agent {agent.name}")

    def change_role(self, agent, new_role):
        # Change the role of an agent based on the situation
        agent.role = new_role
        print(f"Role changed for agent {agent.name} to {new_role}")