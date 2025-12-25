import pandas as pd
from collections import defaultdict
from agents.topic_memory import TopicMemory
from pipelines.daily_topic_extraction import process_day

def build_trends(df):
    topic_memory = TopicMemory()
    trend_data = defaultdict(dict)

    for date, group in df.groupby("date"):
        reviews = group["review"].tolist()
        daily_counts = process_day(reviews, topic_memory)

        for topic, count in daily_counts.items():
            trend_data[topic][date] = count

    trend_df = pd.DataFrame(trend_data).fillna(0).T
    trend_df = trend_df.sort_index(axis=1)

    return trend_df
