import logging
from flask import Flask, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


app = Flask(__name__)
limiter = Limiter(
  app=app,
  key_func=get_remote_address
  )

logging.basicConfig(
  filename='app.log',
  level=logging.INFO,
  format='%(asctime)s %(levelname)s: %(message)s',
  datefmt='%Y-%m-%d %H:%M:%S'
  )


# list of books
books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 2, "title": "1984", "author": "George Orwell"},
    {"id": 3, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 4, "title": "Pride and Prejudice", "author": "Jane Austen"},
    {"id": 5, "title": "The Catcher in the Rye", "author": "J. D. Salinger"},
    {"id": 6, "title": "The Hobbit", "author": "J. R. R. Tolkien"},
    {"id": 7, "title": "The Lord of the Rings", "author": "J. R. R. Tolkien"},
    {"id": 8, "title": "Animal Farm", "author": "George Orwell"},
    {"id": 9, "title": "Brave New World", "author": "Aldous Huxley"},
    {"id": 10, "title": "Fahrenheit 451", "author": "Ray Bradbury"},
    {"id": 11, "title": "Jane Eyre", "author": "Charlotte Brontë"},
    {"id": 12, "title": "Wuthering Heights", "author": "Emily Brontë"},
    {"id": 13, "title": "Moby-Dick", "author": "Herman Melville"},
    {"id": 14, "title": "The Adventures of Huckleberry Finn", "author": "Mark Twain"},
    {"id": 15, "title": "The Adventures of Tom Sawyer", "author": "Mark Twain"},
    {"id": 16, "title": "Little Women", "author": "Louisa May Alcott"},
    {"id": 17, "title": "The Picture of Dorian Gray", "author": "Oscar Wilde"},
    {"id": 18, "title": "Dracula", "author": "Bram Stoker"},
    {"id": 19, "title": "Frankenstein", "author": "Mary Shelley"},
    {"id": 20, "title": "The Count of Monte Cristo", "author": "Alexandre Dumas"},
    {"id": 21, "title": "Les Misérables", "author": "Victor Hugo"},
    {"id": 22, "title": "The Three Musketeers", "author": "Alexandre Dumas"},
    {"id": 23, "title": "War and Peace", "author": "Leo Tolstoy"},
    {"id": 24, "title": "Anna Karenina", "author": "Leo Tolstoy"},
    {"id": 25, "title": "Crime and Punishment", "author": "Fyodor Dostoevsky"},
    {"id": 26, "title": "The Brothers Karamazov", "author": "Fyodor Dostoevsky"},
    {"id": 27, "title": "The Metamorphosis", "author": "Franz Kafka"},
    {"id": 28, "title": "Don Quixote", "author": "Miguel de Cervantes"},
    {"id": 29, "title": "The Alchemist", "author": "Paulo Coelho"},
    {"id": 30, "title": "One Hundred Years of Solitude", "author": "Gabriel García Márquez"},
    {"id": 31, "title": "The Old Man and the Sea", "author": "Ernest Hemingway"},
    {"id": 32, "title": "A Farewell to Arms", "author": "Ernest Hemingway"},
    {"id": 33, "title": "For Whom the Bell Tolls", "author": "Ernest Hemingway"},
    {"id": 34, "title": "The Grapes of Wrath", "author": "John Steinbeck"},
    {"id": 35, "title": "Of Mice and Men", "author": "John Steinbeck"},
    {"id": 36, "title": "East of Eden", "author": "John Steinbeck"},
    {"id": 37, "title": "The Kite Runner", "author": "Khaled Hosseini"},
    {"id": 38, "title": "A Thousand Splendid Suns", "author": "Khaled Hosseini"},
    {"id": 39, "title": "Life of Pi", "author": "Yann Martel"},
    {"id": 40, "title": "The Book Thief", "author": "Markus Zusak"},
    {"id": 41, "title": "The Road", "author": "Cormac McCarthy"},
    {"id": 42, "title": "The Hunger Games", "author": "Suzanne Collins"},
    {"id": 43, "title": "Catching Fire", "author": "Suzanne Collins"},
    {"id": 44, "title": "Mockingjay", "author": "Suzanne Collins"},
    {"id": 45, "title": "Harry Potter and the Sorcerer's Stone", "author": "J. K. Rowling"},
    {"id": 46, "title": "Harry Potter and the Chamber of Secrets", "author": "J. K. Rowling"},
    {"id": 47, "title": "Harry Potter and the Prisoner of Azkaban", "author": "J. K. Rowling"},
    {"id": 48, "title": "Harry Potter and the Goblet of Fire", "author": "J. K. Rowling"},
    {"id": 49, "title": "Harry Potter and the Order of the Phoenix", "author": "J. K. Rowling"},
    {"id": 50, "title": "Harry Potter and the Half-Blood Prince", "author": "J. K. Rowling"},
    {"id": 51, "title": "Harry Potter and the Deathly Hallows", "author": "J. K. Rowling"},
    {"id": 52, "title": "The Chronicles of Narnia", "author": "C. S. Lewis"},
    {"id": 53, "title": "The Lion, the Witch and the Wardrobe", "author": "C. S. Lewis"},
    {"id": 54, "title": "The Little Prince", "author": "Antoine de Saint-Exupéry"},
    {"id": 55, "title": "The Secret Garden", "author": "Frances Hodgson Burnett"},
    {"id": 56, "title": "A Christmas Carol", "author": "Charles Dickens"},
    {"id": 57, "title": "Oliver Twist", "author": "Charles Dickens"},
    {"id": 58, "title": "Great Expectations", "author": "Charles Dickens"},
    {"id": 59, "title": "David Copperfield", "author": "Charles Dickens"},
    {"id": 60, "title": "A Tale of Two Cities", "author": "Charles Dickens"},
    {"id": 61, "title": "The Scarlet Letter", "author": "Nathaniel Hawthorne"},
    {"id": 62, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 63, "title": "The Sun Also Rises", "author": "Ernest Hemingway"},
    {"id": 64, "title": "Slaughterhouse-Five", "author": "Kurt Vonnegut"},
    {"id": 65, "title": "Catch-22", "author": "Joseph Heller"},
    {"id": 66, "title": "The Handmaid's Tale", "author": "Margaret Atwood"},
    {"id": 67, "title": "Beloved", "author": "Toni Morrison"},
    {"id": 68, "title": "The Color Purple", "author": "Alice Walker"},
    {"id": 69, "title": "Invisible Man", "author": "Ralph Ellison"},
    {"id": 70, "title": "The Outsiders", "author": "S. E. Hinton"},
    {"id": 71, "title": "Lord of the Flies", "author": "William Golding"},
    {"id": 72, "title": "The Giver", "author": "Lois Lowry"},
    {"id": 73, "title": "The Maze Runner", "author": "James Dashner"},
    {"id": 74, "title": "Divergent", "author": "Veronica Roth"},
    {"id": 75, "title": "The Fault in Our Stars", "author": "John Green"},
    {"id": 76, "title": "Looking for Alaska", "author": "John Green"},
    {"id": 77, "title": "The Perks of Being a Wallflower", "author": "Stephen Chbosky"},
    {"id": 78, "title": "The Notebook", "author": "Nicholas Sparks"},
    {"id": 79, "title": "The Da Vinci Code", "author": "Dan Brown"},
    {"id": 80, "title": "Angels & Demons", "author": "Dan Brown"},
    {"id": 81, "title": "The Girl with the Dragon Tattoo", "author": "Stieg Larsson"},
    {"id": 82, "title": "Gone Girl", "author": "Gillian Flynn"},
    {"id": 83, "title": "The Shining", "author": "Stephen King"},
    {"id": 84, "title": "It", "author": "Stephen King"},
    {"id": 85, "title": "Misery", "author": "Stephen King"},
    {"id": 86, "title": "The Stand", "author": "Stephen King"},
    {"id": 87, "title": "Dune", "author": "Frank Herbert"},
    {"id": 88, "title": "Foundation", "author": "Isaac Asimov"},
    {"id": 89, "title": "I, Robot", "author": "Isaac Asimov"},
    {"id": 90, "title": "Ender's Game", "author": "Orson Scott Card"},
    {"id": 91, "title": "The Martian", "author": "Andy Weir"},
    {"id": 92, "title": "Ready Player One", "author": "Ernest Cline"},
    {"id": 93, "title": "The Hitchhiker's Guide to the Galaxy", "author": "Douglas Adams"},
    {"id": 94, "title": "The Name of the Wind", "author": "Patrick Rothfuss"},
    {"id": 95, "title": "The Shadow of the Wind", "author": "Carlos Ruiz Zafón"},
    {"id": 96, "title": "The Book of Lost Things", "author": "John Connolly"},
    {"id": 97, "title": "The Night Circus", "author": "Erin Morgenstern"},
    {"id": 98, "title": "The Midnight Library", "author": "Matt Haig"},
    {"id": 99, "title": "Project Hail Mary", "author": "Andy Weir"},
    {"id": 100, "title": "Cloud Atlas", "author": "David Mitchell"}
]

def find_book_by_id(book_id):
  """Find the book with the id 'book_id'.
  If there is no book with this id, return None. """
  book = None
  for b in books:
    if b['id'] == book_id:
      book = b
      break
  return book

@app.route('/api/books/<int:id>', methods=['PUT'])
def handle_book(id):
  # Find a book with the given ID
  book = find_book_by_id(id)

  # If the book wasn't found, return a 404 error
  if book is None:
    return '', 404
  
  # Update the book with the new data
  new_data = request.get_json()
  book.update(new_data)

  # Return the updated book
  return jsonify(book)

@app.route('/api/books/<int:id>', methods=['DELETE'])
def delete_book(id):
  book = find_book_by_id(id)

  if book is None:
    return '', 404

  books.remove(book)
  
  return jsonify(book), 200

def validate_book_data(data):
  if "title" not in data or "author" not in data:
    return False
  return True


@app.route('/api/books', methods=['GET', 'POST'])
@limiter.limit('10/minute')
def handle_books():
    if request.method == 'POST':
        # Get the new book data from the client
        new_book = request.get_json()
        if not validate_book_data(new_book):
          return jsonify({"error": "Invalid book data"}), 400

        # Generate a new ID for the book
        new_id = max(book['id'] for book in books) + 1
        new_book['id'] = new_id
        
        # Add the new book to our list
        books.append(new_book)
        
        # Return the new book data to the client
        return jsonify(new_book), 201
    else:
        app.logger.info('GET request received for /api/books')  # Log a message

        # Handle the GET request
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 10))

        start_index = (page - 1) * limit
        end_index = start_index + limit

        paginated_books = books[start_index:end_index]
        author = request.args.get('author')
        if author:
          filtered_books = [book for book in paginated_books if book.get('author') == author]
          return jsonify(filtered_books)
        else:
          return jsonify(paginated_books)

@app.errorhandler(404)
def not_found_error(error):
  return jsonify({"error": "Not found!"}), 404

@app.errorhandler(405)
def method_not_allowed(error):
  return jsonify({"error": "Method not allowed"}), 405


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)