import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("netflix_cleaned.csv")

# Analyze release years
year_counts = df["release_year"].value_counts().sort_index()

# Dashboard setup
fig, ax = plt.subplots(figsize=(14, 7))

fig.patch.set_facecolor("#101820")
ax.set_facecolor("#101820")

# Trend line
ax.plot(
    year_counts.index,
    year_counts.values,
    marker="o",
    linewidth=2.5,
    markersize=5,
    color="#00C9A7"
)

# Titles and labels
ax.set_title(
    "NETFLIX RELEASE YEAR TREND",
    fontsize=18,
    color="white",
    fontweight="bold",
    pad=20
)

ax.set_xlabel("Release Year", color="white", fontsize=12)
ax.set_ylabel("Number of Titles", color="white", fontsize=12)

# Axis styling
ax.tick_params(colors="white")
ax.grid(color="gray", linestyle="--", alpha=0.3)

for spine in ax.spines.values():
    spine.set_color("#444444")

# Highlight peak year
peak_year = year_counts.idxmax()
peak_count = year_counts.max()

ax.annotate(
    f"Peak: {peak_year}\n{peak_count} Titles",
    xy=(peak_year, peak_count),
    xytext=(peak_year - 5, peak_count),
    color="white",
    fontsize=10,
    arrowprops=dict(arrowstyle="->", color="#F4C542")
)

plt.tight_layout()

# Save dashboard
plt.savefig("release_year_trend.png", dpi=300, facecolor=fig.get_facecolor())

plt.show()

# Insights
print("NETFLIX RELEASE YEAR TREND ANALYSIS")
print("-----------------------------------")
print("Peak Release Year:", peak_year)
print("Maximum Titles:", peak_count)
print("\nRecent Year Counts:")
print(year_counts.tail(15))
