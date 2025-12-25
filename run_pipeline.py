import pandas as pd
from pipelines.fetch_reviews import load_reviews
from pipelines.trend_builder import build_trends

def main():
    df = load_reviews()
    trend_df = build_trends(df)

    trend_df.to_csv("topic_trends_30_days.csv")
    print("✅ Topic trend table saved as topic_trends_30_days.csv")

if __name__ == "__main__":
    main()
