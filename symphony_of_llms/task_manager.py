class TaskManager:
    def __init__(self):
        self.tasks = {}

    def assign_task(self, agent, task):
        # Assign tasks to agents
        if agent not in self.tasks:
            self.tasks[agent] = []
        self.tasks[agent].append(task)
        print(f"Task '{task}' assigned to agent {agent}")

    def monitor_progress(self, agent):
        # Monitor task progress and provide feedback
        if agent in self.tasks:
            return self.tasks[agent]
        return []