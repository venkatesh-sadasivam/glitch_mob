#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run all necessary parts of the codebase
python -c "
from symphony_of_llms.agent import Agent
from symphony_of_llms.communication_channel import CommunicationChannel
from symphony_of_llms.task_manager import TaskManager
from symphony_of_llms.visualization_tool import VisualizationTool
from symphony_of_llms.debugging_tool import DebuggingTool
from symphony_of_llms.agent_templates import Storyteller, FactChecker, CodeWizard, Critic
from symphony_of_llms.memory_manager import MemoryManager
from symphony_of_llms.emotion_model import EmotionModel
from symphony_of_llms.role_manager import RoleManager
from symphony_of_llms.external_integration import ExternalIntegration

# Example usage
agent = Agent(name='Agent1', persona='Helper', role='Assistant', objectives=[])
agent.activate()

comm_channel = CommunicationChannel()
task_manager = TaskManager()
visual_tool = VisualizationTool()
debug_tool = DebuggingTool()
memory_manager = MemoryManager()
emotion_model = EmotionModel()
role_manager = RoleManager()
external_integration = ExternalIntegration()

# Example interactions
comm_channel.send_message('Agent1', 'Agent2', 'Hello')
task_manager.assign_task('Agent1', 'Task1')
visual_tool.visualize_interactions(comm_channel)
debug_tool.debug_agent(agent)
memory_manager.store_memory('Agent1', 'Memory1')
emotion_model.set_emotion('Agent1', 'Happy')
role_manager.assign_role(agent, 'Leader')
external_integration.connect_to_api(agent, 'http://api.example.com')
"

# Run tests
pytest
