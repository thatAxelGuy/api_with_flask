import time

import requests

BASE_URL = "http://127.0.0.1:5000/api/books"

all_books = []
page = 1
limit = 10

while len(all_books) < 100:

    response = requests.get(
        BASE_URL,
        params={"page": page, "limit": limit}
    )

    if response.status_code == 429:
        print("Rate limited. Waiting...")
        time.sleep(65)
        continue

    books = response.json()
    

    if not books:
        break

    all_books.extend(books)
    page += 1

    if len(books) < limit:
        break

print(all_books)
print(f"\n{max([book["id"] for book in all_books])} items returned")

