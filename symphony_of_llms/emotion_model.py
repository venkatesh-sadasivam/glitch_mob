class EmotionModel:
    def __init__(self):
        self.emotions = {}

    def set_emotion(self, agent, emotion):
        # Set the emotional state of an agent
        self.emotions[agent] = emotion
        print(f"Emotion set for agent {agent}: {emotion}")

    def get_emotion(self, agent):
        # Get the current emotional state of an agent
        return self.emotions.get(agent, "Neutral")