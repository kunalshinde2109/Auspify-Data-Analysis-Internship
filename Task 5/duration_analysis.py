import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("netflix_cleaned.csv")

# Separate Movies and TV Shows
movies = df[df["type"] == "Movie"].copy()
tv_shows = df[df["type"] == "TV Show"].copy()

# Extract movie duration in minutes
movies["duration_value"] = movies["duration"].str.replace(" min", "", regex=False)
movies["duration_value"] = pd.to_numeric(movies["duration_value"], errors="coerce")

# Extract TV Show seasons
tv_shows["duration_value"] = tv_shows["duration"].str.replace(" Season", "", regex=False)
tv_shows["duration_value"] = tv_shows["duration_value"].str.replace(" Seasons", "", regex=False)
tv_shows["duration_value"] = pd.to_numeric(tv_shows["duration_value"], errors="coerce")

# Statistics
average_movie_duration = movies["duration_value"].mean()
average_tv_seasons = tv_shows["duration_value"].mean()

print("Netflix Duration Analysis")
print("-----------------------")
print("Total Movies:", len(movies))
print("Total TV Shows:", len(tv_shows))
print("Average Movie Duration:", round(average_movie_duration, 2), "minutes")
print("Average TV Show Seasons:", round(average_tv_seasons, 2))

# TV Show season distribution
season_distribution = tv_shows["duration_value"].value_counts().sort_index()

# Visualization
plt.figure(figsize=(12, 6))

season_distribution.plot(kind="bar")

plt.title("Netflix TV Shows - Season Distribution")
plt.xlabel("Number of Seasons")
plt.ylabel("Number of TV Shows")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("season_distribution.png")

plt.show()