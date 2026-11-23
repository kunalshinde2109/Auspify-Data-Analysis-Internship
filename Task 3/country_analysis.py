import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Load dataset
df = pd.read_csv("netflix_cleaned.csv")

# Clean country column
df["country"] = df["country"].fillna("Unknown")

# Split countries and count
country_data = df["country"].str.split(",").explode()
country_data = country_data.str.strip()

country_counts = country_data.value_counts()
country_counts = country_counts.drop("Unknown", errors="ignore")

top_10 = country_counts.head(10)
total_countries = country_counts.index.nunique()
total_mentions = country_counts.sum()
top_country = country_counts.index[0]
top_count = country_counts.iloc[0]

# Dashboard setup
fig = plt.figure(figsize=(16, 10), facecolor="#0b1320")
gs = GridSpec(3, 2, figure=fig, height_ratios=[0.8, 1.2, 2])

# Header
fig.text(0.5, 0.95, "NETFLIX COUNTRY-WISE CONTENT ANALYSIS",
         ha="center", fontsize=22, fontweight="bold", color="white")

fig.text(0.5, 0.91, "Global Content Distribution by Country",
         ha="center", fontsize=12, color="#b8c7d9")

# KPI Cards
fig.text(0.18, 0.80, f"{total_mentions:,}",
         ha="center", fontsize=24, fontweight="bold", color="#00d4ff")
fig.text(0.18, 0.76, "Total Country Mentions",
         ha="center", fontsize=11, color="white")

fig.text(0.50, 0.80, f"{total_countries:,}",
         ha="center", fontsize=24, fontweight="bold", color="#f7b731")
fig.text(0.50, 0.76, "Countries Represented",
         ha="center", fontsize=11, color="white")

fig.text(0.82, 0.80, top_country,
         ha="center", fontsize=22, fontweight="bold", color="#ff6b6b")
fig.text(0.82, 0.76, f"Top Country ({top_count:,} titles)",
         ha="center", fontsize=11, color="white")

# Bar chart
ax1 = fig.add_subplot(gs[1:, 0])
ax1.set_facecolor("#0b1320")

bars = ax1.barh(top_10.sort_values().index,
                top_10.sort_values().values)

ax1.set_title("Top 10 Content Producing Countries",
              color="white", fontsize=15, pad=15)

ax1.set_xlabel("Number of Titles", color="white")
ax1.tick_params(colors="white")

for spine in ax1.spines.values():
    spine.set_visible(False)

ax1.grid(axis="x", alpha=0.2)

# Bar labels
for bar in bars:
    width = bar.get_width()
    ax1.text(width + 10, bar.get_y() + bar.get_height()/2,
             f"{int(width):,}", va="center", color="white", fontsize=9)

# Top 5 pie chart
ax2 = fig.add_subplot(gs[1, 1])
ax2.set_facecolor("#0b1320")

top_5 = country_counts.head(5)

wedges, texts, autotexts = ax2.pie(
    top_5.values,
    labels=top_5.index,
    autopct="%1.1f%%",
    startangle=140,
    labeldistance=1.15,
    pctdistance=0.65
)

for text in texts:
    text.set_color("white")
    text.set_fontsize(9)

for text in autotexts:
    text.set_color("white")
    text.set_fontweight("bold")
    text.set_fontsize(5)

ax2.set_title("Top 5 Countries Share",
              color="white", fontsize=15)

# Insights
ax3 = fig.add_subplot(gs[2, 1])
ax3.set_facecolor("#0b1320")
ax3.axis("off")

insights = [
    "KEY INSIGHTS",
    "",
    f"1. {top_country} leads with {top_count:,} country mentions.",
    f"2. Top 10 countries account for {top_10.sum():,} mentions.",
    f"3. {total_countries:,} countries appear in the dataset.",
    "4. Country analysis helps identify content production hubs."
]

ax3.text(0.05, 0.95, "\n".join(insights),
         transform=ax3.transAxes,
         color="white", fontsize=12,
         verticalalignment="top", linespacing=1.8)

plt.tight_layout(rect=[0.03, 0.03, 0.97, 0.90])

# Save dashboard
plt.savefig("country_analysis_dashboard.png",
            dpi=300, facecolor=fig.get_facecolor())

plt.show()