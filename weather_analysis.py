import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import os

# ✅ PostgreSQL Connection Details
DB_NAME = "weather_db"
DB_USER = "postgres"
DB_PASSWORD = "kuzgigi2025"
DB_HOST = "localhost"
DB_PORT = "5432"

# ✅ Fetch Weather Data from PostgreSQL for the Last 6 Hours
def fetch_weather_data():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
        )
        cur = conn.cursor()
        sql = """
        SELECT city, temperature, timestamp FROM weather_data
        WHERE timestamp >= NOW() - INTERVAL '6 hours'
        ORDER BY timestamp ASC;
        """
        cur.execute(sql)
        rows = cur.fetchall()
        df = pd.DataFrame(rows, columns=["City", "Temperature", "Timestamp"])
        df["Timestamp"] = pd.to_datetime(df["Timestamp"])
        df["Hour"] = df["Timestamp"].dt.strftime("%I %p")  # Format as 12 AM, 1 AM, etc.
        cur.close()
        conn.close()
        return df
    except Exception as e:
        print(f"❌ Error fetching data: {e}")
        return None

# ✅ Define HEX color for each city
CITY_COLORS = {
    "London": "#FB9833",
    "Paris": "#FCEFEF",
    "New York": "#1B768E",
    "Tokyo": "#012538",
    "Sydney": "#4D555B",
}

def plot_temperature_bar_chart(df, city):
    """Generates and saves a bar chart for a specific city with exact temperature values."""
    city_df = df[df["City"] == city]

    if city_df.empty:
        print(f"⚠️ No data available for {city}. Skipping...")
        return

    plt.figure(figsize=(8, 5))

    # ✅ Bar chart with city's assigned HEX color
    ax = sns.barplot(data=city_df, x="Hour", y="Temperature", color=CITY_COLORS.get(city, "#1B768E"), edgecolor="black")

    # ✅ Add temperature labels directly above each bar
    for index, row in city_df.iterrows():
        plt.text(index, row["Temperature"] + 0.2, f"{row['Temperature']:.1f}°C",
                 ha="center", va="bottom", fontsize=10, fontweight="bold", color="black")

    # ✅ Add temperature values on the bars for clarity
    for bar, row in zip(ax.patches, city_df.itertuples()):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() / 2, f"{row.Temperature:.1f}°C",
                ha="center", va="center", fontsize=10, fontweight="bold", color="white")

    plt.xlabel("Hour (Last 6 Hours)", fontsize=12, fontweight='bold')
    plt.ylabel("Temperature (°C)", fontsize=12, fontweight='bold')
    plt.title(f"🌡️ Temperature Trend in {city} (Last 6 Hours)", fontsize=14, fontweight='bold')

    plt.xticks(rotation=45)
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.tight_layout()

    # ✅ Save the chart in a specific folder
    save_folder = r"C:\Users\ri\Documents\Data app\Work\City_Charts"
    os.makedirs(save_folder, exist_ok=True)
    filename = os.path.join(save_folder, f"{city}_temperature_trend_{datetime.datetime.now().strftime('%Y%m%d%H%M')}.png")

    plt.savefig(filename)
    plt.close()  # Prevent overlapping plots
    print(f"✅ Saved: {filename}")

# ✅ Main Execution
if __name__ == "__main__":
    df = fetch_weather_data()
    if df is not None:
        for city in CITY_COLORS.keys():
            plot_temperature_bar_chart(df, city)
