import os
import matplotlib.pyplot as plt


def plot_conversion_rate(df):
    os.makedirs("outputs", exist_ok=True)

    conversion = (
        df.groupby("test group")["converted"]
        .mean() * 100
    )

    plt.figure(figsize=(6, 4))
    plt.bar(conversion.index, conversion.values)

    plt.title("Conversion Rate by Group")
    plt.xlabel("Test Group")
    plt.ylabel("Conversion Rate (%)")

    plt.tight_layout()
    plt.savefig("outputs/conversion_rate.png")
    plt.close()


def plot_ads_day(df):

    day = (
        df.groupby("most ads day")["converted"]
        .mean() * 100
    )

    plt.figure(figsize=(8, 4))
    plt.bar(day.index, day.values)

    plt.title("Conversion Rate by Day")
    plt.xlabel("Day")
    plt.ylabel("Conversion Rate (%)")

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.savefig("outputs/day_analysis.png")
    plt.close()


def plot_ads_hour(df):

    hour = (
        df.groupby("most ads hour")["converted"]
        .mean() * 100
    )

    plt.figure(figsize=(10, 4))
    plt.plot(hour.index, hour.values, marker="o")

    plt.title("Conversion Rate by Hour")
    plt.xlabel("Hour")
    plt.ylabel("Conversion Rate (%)")

    plt.tight_layout()
    plt.savefig("outputs/hour_analysis.png")
    plt.close()


def plot_segment_analysis(segment_df):

    pivot = segment_df.pivot(
        index="ad_exposure",
        columns="test group",
        values="conversion_rate"
    )

    pivot.plot(
        kind="bar",
        figsize=(8, 5)
    )

    plt.title("Conversion Rate by User Segment")
    plt.xlabel("Ad Exposure")
    plt.ylabel("Conversion Rate (%)")

    plt.tight_layout()

    plt.savefig("outputs/segment_analysis.png")

    plt.close()