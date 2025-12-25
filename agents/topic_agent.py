import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

SIMILARITY_THRESHOLD = 0.85

def find_matching_topic(embedding, topic_memory):
    topics = topic_memory.get_topics()

    if not topics:
        return None

    existing_embeddings = [t["embedding"] for t in topics]
    similarities = cosine_similarity([embedding], existing_embeddings)[0]

    best_index = np.argmax(similarities)
    best_score = similarities[best_index]

    if best_score >= SIMILARITY_THRESHOLD:
        return topics[best_index]["name"]

    return None
