from flask import Flask, render_template_string

app = Flask(__name__)

# Sample book names
books = [
    "To Kill a Mockingbird",
    "Pride and Prejudice",
    "The Great Gatsby",
    "1984",
    "The Catcher in the Rye",
    "The Hobbit",
    "Fahrenheit 451",
    "The Grapes of Wrath",
    "To the Lighthouse",
    "Moby-Dick",
]

@app.route('/')
def index():
    # HTML content embedded within the Python code
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Library Management</title>
    </head>
    <body>
        <h1>Welcome to the Library</h1>
        <p>This is a simple Flask web application for library management.</p>
        <a href="/books">View Book List</a>
    </body>
    </html>
    """

    # Rendering HTML content using render_template_string
    return render_template_string(html_content)

@app.route('/books')
def book_list():
    # Generating HTML for displaying book list
    book_list_html = "<h2>Book List</h2><ul>"
    for book in books:
        book_list_html += f"<li>{book}</li>"
    book_list_html += "</ul>"

    return render_template_string(book_list_html)

if __name__ == '__main__':
    app.run(debug=True)
