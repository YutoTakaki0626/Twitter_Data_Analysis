from datetime import timedelta
import pandas as pd
import tweepy

def get_search(
    api: tweepy.API, q: str, start_date: str, end_date: str, count: int = 1000
) -> pd.DataFrame:

    q = f"{q} since:{start_date} until:{end_date} -filter:retweets"

    tweets = api.search(
        q=q,
        count=count,
        tweet_mode="extended",
        locale="ja",
        lang="ja",
        include_entities=False,
    )

    df = pd.DataFrame(
        columns=[
            "user_id",
            "user_name",
            "user_screen_name",
            "user_profile_image_url",
            "tweet_id",
            "tweet_full_text",
            "tweet_favorite_count",
            "tweet_created_at",
        ]
    )

    for tweet in tweets:
        df = df.append(
            {
                "user_id": tweet.user.id,
                "user_name": tweet.user.name,
                "user_screen_name": tweet.user.screen_name,
                "user_profile_image_url": tweet.user.profile_image_url.replace(
                    "_normal", ""
                ),
                "tweet_id": tweet.id,
                "tweet_full_text": tweet.full_text,
                "tweet_favorite_count": tweet.favorite_count,
                "tweet_created_at": tweet.created_at + timedelta(hours=+9),
            },
            ignore_index=True,
        )
    return df