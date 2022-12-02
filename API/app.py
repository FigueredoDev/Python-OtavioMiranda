from flask import Flask, jsonify, request, redirect

app = Flask(__name__)

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


@app.route("/")
def home():
    return redirect("http://localhost:5000/books")


@app.route('/books', methods=["GET"])
def get_books():
    return jsonify(books)


@app.route('/books/<int:id>', methods=['GET'])
def get_books_by_id(id):
    for book in books:
        if book.get('id') == id:
            return jsonify(book)


@app.route('/books/<int:id>', methods=["PUT"])
def change_book(id):
    book_changed = request.get_json(books)
    for index, book in enumerate(books):
        if book.get('id') == id:
            books[index].update(book_changed)
            return jsonify(books[index])


@app.route('/books', methods=["POST"])
def create_book():
    new_book = request.get_json()
    books.append(new_book)

    return jsonify(books)


@app.route('/books/<int:id>', methods=["DELETE"])
def del_book():
    for index, book in enumerate(books):
        if book.get('id') == id:
            del books[index]

            return jsonify(books)


if __name__ == "__main__":
    app.run(port=5000, host='localhost', debug=True)
