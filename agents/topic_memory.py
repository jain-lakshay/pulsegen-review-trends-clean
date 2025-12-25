class TopicMemory:
    def __init__(self):
        self.topics = []  # [{name, embedding}]

    def add_topic(self, name, embedding):
        self.topics.append({
            "name": name,
            "embedding": embedding
        })

    def get_topics(self):
        return self.topics
