import json
import os

books = [
    {
        'id': 1,
        'title': 'O senhor dos anéis'
    },
    {
        'id': 2,
        'title': 'Harry Potter e a Pedra Filosofal'
    },
    {
        'id': 3,
        'title': 'Clean Code'
    }
]

# Save json file
BASE_DIR = os.path.dirname(__file__)
SAVE_TO = os.path.join(BASE_DIR, 'books.json')

with open(SAVE_TO, 'w') as file:
    json.dump(books, file, indent=2)

print(json.dumps(books, indent=2))


# Open json file
BASE_DIR = os.path.dirname(__file__)
JSON_FILE = os.path.join(BASE_DIR, 'books.json')

with open(JSON_FILE, 'r') as file:
    books = json.load(file)
    print(books)
