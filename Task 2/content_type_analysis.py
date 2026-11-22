import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../Task1/Dataset/netflix_cleaned.csv")

# Analysis
content_counts = df["type"].value_counts()
total_titles = len(df)
percentages = content_counts / total_titles * 100

movies = content_counts["Movie"]
tv_shows = content_counts["TV Show"]

# Dashboard figure
fig = plt.figure(figsize=(14, 10), facecolor="#101820")

gs = fig.add_gridspec(
    4, 2,
    height_ratios=[0.8, 1.5, 4, 2],
    hspace=0.50,
    wspace=0.25
)

# ---------------- HEADER ----------------
ax_header = fig.add_subplot(gs[0, :])
ax_header.axis("off")

ax_header.text(
    0.5, 0.65,
    "NETFLIX CONTENT TYPE ANALYSIS",
    ha="center", va="center",
    fontsize=22, fontweight="bold", color="white"
)

ax_header.text(
    0.5, 0.15,
    "Movies vs TV Shows Distribution",
    ha="center", va="center",
    fontsize=12, color="#B0BEC5"
)

# ---------------- KPI CARDS ----------------
kpi_gs = gs[1, :].subgridspec(1, 3, wspace=0.25)

kpi_data = [
    ("TOTAL TITLES", f"{total_titles:,}", "#243447"),
    ("MOVIES", f"{movies:,}\n{percentages['Movie']:.2f}%", "#E50914"),
    ("TV SHOWS", f"{tv_shows:,}\n{percentages['TV Show']:.2f}%", "#0077B6")
]

for i, (label, value, color) in enumerate(kpi_data):
    ax = fig.add_subplot(kpi_gs[0, i])
    ax.set_facecolor(color)
    ax.set_xticks([])
    ax.set_yticks([])

    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.text(
        0.5, 0.5,
        f"{label}\n{value}",
        ha="center", va="center",
        fontsize=16, fontweight="bold",
        color="white", linespacing=1.4
    )

# ---------------- BAR CHART ----------------
ax1 = fig.add_subplot(gs[2, 0])
ax1.set_facecolor("#101820")

bars = ax1.bar(
    content_counts.index,
    content_counts.values,
    color=["#E50914", "#0077B6"],
    width=0.55
)

ax1.set_title(
    "Content Count Comparison",
    fontsize=15, color="white", pad=15
)

ax1.set_ylabel("Number of Titles", color="white")
ax1.tick_params(colors="white")
ax1.set_ylim(0, max(content_counts.values) * 1.15)

for bar in bars:
    ax1.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 80,
        f"{int(bar.get_height()):,}",
        ha="center", va="bottom",
        color="white", fontsize=11
    )

for spine in ax1.spines.values():
    spine.set_color("#607080")

# ---------------- PIE CHART ----------------
ax2 = fig.add_subplot(gs[2, 1])
ax2.set_facecolor("#101820")

ax2.pie(
    percentages,
    labels=content_counts.index,
    autopct="%1.2f%%",
    startangle=90,
    colors=["#E50914", "#0077B6"],
    textprops={"color": "white", "fontsize": 12}
)

ax2.set_title(
    "Content Percentage",
    fontsize=15, color="white", pad=15
)

# ---------------- INSIGHTS ----------------
ax_insights = fig.add_subplot(gs[3, :])
ax_insights.set_facecolor("#243447")
ax_insights.axis("off")

insights_text = (
    "KEY INSIGHTS\n\n"
    f"• Movies account for {percentages['Movie']:.2f}% of total content.\n"
    f"• TV Shows account for {percentages['TV Show']:.2f}% of total content.\n"
    "• Movies represent the majority of Netflix content."
)

ax_insights.text(
    0.5, 0.5,
    insights_text,
    ha="center", va="center",
    fontsize=12, color="white",
    linespacing=1.6
)

# ---------------- SAVE ----------------
plt.savefig(
    "content_type_dashboard.png",
    dpi=300,
    facecolor="#101820"
)

plt.show()

print("Dashboard saved successfully!")