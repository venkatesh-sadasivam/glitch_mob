class VisualizationTool:
    def visualize_interactions(self, communication_channel):
        # Display message flow and task assignments
        for message in communication_channel.messages:
            print(f"Message from {message[0]} to {message[1]}: {message[2]}")