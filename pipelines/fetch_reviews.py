from google_play_scraper import reviews, Sort
import pandas as pd
from datetime import datetime
import os

MAX_REVIEWS = 5000   # hard limit
DATA_PATH = "data/raw_reviews.csv"

def fetch_reviews(app_id, start_date):
    print("🚀 Starting review fetch...")
    all_reviews = []
    continuation_token = None

    while True:
        print("🔄 Fetching next batch...")
        result, continuation_token = reviews(
            app_id,
            lang="en",
            country="in",
            sort=Sort.NEWEST,
            count=200,
            continuation_token=continuation_token
        )

        for r in result:
            if len(all_reviews) >= MAX_REVIEWS:
                print("🛑 Reached MAX review limit")
                return pd.DataFrame(all_reviews)

            review_date = r["at"].date()
            if review_date < start_date:
                print("🛑 Reached reviews before start date")
                return pd.DataFrame(all_reviews)

            all_reviews.append({
                "date": review_date,
                "review": r["content"]  # ✅ ensure this column is 'review'
            })

        print(f"✅ Collected {len(all_reviews)} reviews so far")

        if not continuation_token:
            break

    return pd.DataFrame(all_reviews)


def load_reviews():
    """
    Loads reviews from CSV for downstream pipeline
    """
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(
            "❌ raw_reviews.csv not found. Run fetch_reviews first."
        )

    df = pd.read_csv(DATA_PATH)

    # STANDARDIZE: if old CSV has 'content', rename to 'review'
    if "content" in df.columns:
        df.rename(columns={"content": "review"}, inplace=True)
    elif "review" not in df.columns:
        raise KeyError("No 'review' column found in CSV")

    df["date"] = pd.to_datetime(df["date"]).dt.date
    return df


if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)

    df = fetch_reviews(
        app_id="in.swiggy.android",
        start_date=datetime(2024, 6, 1).date()
    )

    print("💾 Saving to CSV...")
    df.to_csv(DATA_PATH, index=False)
    print("🎉 Done! Reviews saved to data/raw_reviews.csv")
