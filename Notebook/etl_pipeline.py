import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from sqlalchemy import create_engine

# Download stopwords
nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

# Step 1: Extract (Load CSV data)
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

# Step 2: Transform (Clean and Preprocess)
def clean_text(text):
    if pd.isnull(text):
        return ""
    
    # Convert to lowercase
    text = text.lower()
    
    # Remove special characters and numbers
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    
    # Remove stopwords
    words = text.split()
    words = [word for word in words if word not in stop_words]
    
    return " ".join(words)

def transform_data(df):
    # Drop duplicates
    df = df.drop_duplicates()

    # Drop null values
    df = df.dropna(subset=["reviews_text", "user_sentiment"])

    # Apply text cleaning
    df["cleaned_reviews"] = df["reviews_text"].apply(clean_text)

    return df

# Step 3: Load (Save Cleaned Data to CSV and Database)
def load_data_to_db(df, db_url="sqlite:///ecommerce_reviews.db"):
    engine = create_engine(db_url)
    df.to_sql("cleaned_reviews", con=engine, if_exists="replace", index=False)
    print("Data successfully loaded into the database.")

def load_data_to_csv(df, output_file="cleaned_ecommerce_reviews.csv"):
    df.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")

# Run the ETL Pipeline
if __name__ == "__main__":
    # Load data
    file_path = "ecommerce_reviews.csv"
    df = load_data(file_path)
    
    # Transform data
    df_cleaned = transform_data(df)
    
    # Load data
    load_data_to_csv(df_cleaned)
    load_data_to_db(df_cleaned)

    print("ETL process completed successfully!")