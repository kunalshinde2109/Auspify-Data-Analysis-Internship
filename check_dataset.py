
import pandas as pd

# Load Dataset
df = pd.read_csv("Dataset/Dataset.csv")

print("DATA CLEANING STARTED")

# Remove extra spaces from text columns
text_columns = df.select_dtypes(include="str").columns

for col in text_columns:
    df[col] = df[col].str.strip()

# Convert date_added into datetime format
df["date_added"] = pd.to_datetime(
    df["date_added"].str.strip(),
    format="mixed",
    errors="coerce"
)

# Check data after cleaning
print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Export cleaned dataset
df.to_csv("Dataset/netflix_cleaned.csv", index=False)

print("\nCleaned Dataset Exported Successfully!")


# Standardize text columns

df["type"] = df["type"].str.strip().replace({
    "movie": "Movie",
    "Movie": "Movie",
    "tv show": "TV Show",
    "TV Show": "TV Show",
    "Tv Show": "TV Show"
})
df["country"] = df["country"].str.strip()

df["rating"] = df["rating"].str.strip().str.upper()

print("\nStandardization Completed!")

print("\nType Categories:")
print(df["type"].unique())

print("\nRating Categories:")
print(df["rating"].unique())


# Check unique values before standardization

print("\nUnique Type Values:")
print(df["type"].unique())

print("\nUnique Rating Values:")
print(df["rating"].unique())

print("\nSample Country Values:")
print(df["country"].dropna().unique()[:20])

# Export final cleaned dataset
df.to_csv("Dataset/netflix_cleaned.csv", index=False)

print("\nFinal Cleaned Dataset Exported Successfully!")

# Verify exported file
cleaned_df = pd.read_csv("Dataset/netflix_cleaned.csv")

print("\nFinal Dataset Shape:")
print(cleaned_df.shape)

print("\nFinal Type Categories:")
print(cleaned_df["type"].unique())