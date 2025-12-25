import pandas as pd
from collections import defaultdict

from utils.text_cleaner import clean_text
from utils.embeddings import get_embeddings
from agents.topic_memory import TopicMemory
from agents.topic_agent import find_matching_topic

def process_day(reviews, topic_memory):
    cleaned_reviews = [clean_text(r) for r in reviews]
    embeddings = get_embeddings(cleaned_reviews)

    daily_topic_counts = defaultdict(int)

    for review, emb in zip(cleaned_reviews, embeddings):
        topic = find_matching_topic(emb, topic_memory)

        if topic is None:
            topic_name = review[:50]  # temporary readable topic
            topic_memory.add_topic(topic_name, emb)
            daily_topic_counts[topic_name] += 1
        else:
            daily_topic_counts[topic] += 1

    return daily_topic_counts
