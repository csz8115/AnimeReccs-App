import kagglehub

# Download latest version
path = kagglehub.dataset_download("sazzadsiddiquelikhon/myanimelist-anime-database-july-2025")

# List all the columns in the dataset
import pandas as pd

df = pd.read_csv(path + "/anime.csv")

# drop unwanted columns if present
cols_to_drop = [
    "approved",
    "title_synonyms",
    "image_jpg_large_url",
    "image_webp_url",
    "image_webp_small_url",
    "image_webp_large_url",
    "trailer_url",
    "trailer_embed_url",
    "trailer_image_url",
    "trailer_large_image_url",
    "trailer_maximum_image_url",
    "aired_prop_from_day",
    "aired_prop_from_month",
    "aired_prop_from_year",
    "aired_prop_to_day",
    "aired_prop_to_month",
    "aired_prop_to_year",
    "aired_string",
    "season",
    "year",
]
existing = [c for c in cols_to_drop if c in df.columns]
if existing:
    df = df.drop(columns=existing)

print("Columns in the dataset:")
for col in df.columns:
    print(f"  {col}")

print("Total number of columns:", len(df.columns))

print("Possible values for 'type' column:")
for value in df['type'].dropna().unique():
    print(f"  {value}")
