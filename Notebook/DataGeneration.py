import pandas as pd
import numpy as np
from faker import Faker
import random
import uuid

# Initialize Faker
fake = Faker()

# Generate random categories
categories_list = [
    "Electronics, Phones, Accessories",
    "Movies, Music & Books, CDs & Vinyl",
    "Home & Kitchen, Furniture, Decor",
    "Clothing, Shoes & Jewelry, Men's Fashion",
    "Beauty & Personal Care, Skincare, Makeup",
]

brands = ["Samsung", "Apple", "Sony", "Nike", "Adidas", "Universal Music", "LG", "Bose"]
manufacturers = ["Samsung Electronics", "Apple Inc.", "Sony Corp.", "Nike Ltd.", "Adidas AG", "Universal Music Group"]
product_names = ["iPhone 13", "Galaxy S22", "Sony Headphones", "Nike Air Max", "Adidas Ultraboost", "Classic Vinyl Album"]

# Generate dataset
num_samples = 40000  # Adjust the number of rows as needed
data = []

for _ in range(num_samples):
    review_id = str(uuid.uuid4())[:16]  # Generate a unique ID
    brand = random.choice(brands)
    categories = random.choice(categories_list)
    manufacturer = random.choice(manufacturers)
    product_name = random.choice(product_names)
    review_date = fake.date_time_this_decade().isoformat()
    did_purchase = random.choice(["Yes", "No"])
    do_recommend = random.choice(["Yes", "No"])
    rating = random.randint(1, 5)
    review_text = fake.sentence(nb_words=15)
    review_title = fake.sentence(nb_words=4)
    user_city = fake.city()
    user_province = fake.state_abbr()
    username = fake.user_name()
    sentiment = "Positive" if rating > 3 else "Negative" if rating < 3 else "Neutral"

    data.append([
        review_id, brand, categories, manufacturer, product_name, review_date, 
        did_purchase, do_recommend, rating, review_text, review_title, 
        user_city, user_province, username, sentiment
    ])

# Create DataFrame
columns = [
    "id", "brand", "categories", "manufacturer", "name", "reviews_date", 
    "reviews_didPurchase", "reviews_doRecommend", "reviews_rating", "reviews_text", 
    "reviews_title", "reviews_userCity", "reviews_userProvince", "reviews_username", "user_sentiment"
]

df = pd.DataFrame(data, columns=columns)

# Save to CSV
df.to_csv("ecommerce_reviews.csv", index=False)

print("Dataset generated and saved as 'ecommerce_reviews.csv'")