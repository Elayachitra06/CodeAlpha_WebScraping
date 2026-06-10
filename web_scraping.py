import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = []

for item in soup.find_all("article", class_="product_pod"):
    title = item.h3.a["title"]
    price = item.find("p", class_="price_color").text
    rating = item.p["class"][1]

    books.append({
        "Title": title,
        "Price": price,
        "Rating": rating
    })

df = pd.DataFrame(books)

print(df.head())

df.to_csv("books_dataset.csv", index=False)

print("Dataset saved successfully!")
