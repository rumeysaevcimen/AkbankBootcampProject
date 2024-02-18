from flask import Flask, render_template, request, redirect, flash
import secrets

class Library:
    def __init__(self):
        self.file_path = "books.txt"
        self.file = open(self.file_path, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        book_lines = self.file.readlines()
        print(book_lines)  # Bu satırı ekleyin
        books = []
        for line in book_lines:
            book_info = line.strip().split(',')
            if len(book_info) == 4:
                book_entry = {
                    "Kitap Adı": book_info[0],
                    "Yazar": book_info[1],
                    "Yayın Yılı": book_info[2],
                    "Sayfa Sayısı": book_info[3]
                }
                books.append(book_entry)

        return books

    def add_book(self, title, author, release_date, num_pages):
        book_info = f"{title},{author},{release_date},{num_pages}\n"
        self.file.write(book_info)
        return "Book added successfully!"

    def remove_book(self, title_to_remove):
        self.file.seek(0)
        book_lines = self.file.read().splitlines()

        updated_book_list = [line for line in book_lines if title_to_remove not in line]

        self.file.seek(0)
        self.file.truncate()
        self.file.write('\n'.join(updated_book_list))
        return "Book removed successfully!"

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
lib = Library()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/list_books")
def list_books():
    books = lib.list_books()
    return render_template("list_books.html", books=books)

@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        release_date = request.form["release_date"]
        num_pages = request.form["num_pages"]

        message = lib.add_book(title, author, release_date, num_pages)
        flash(message)
        return redirect("/")
    return render_template("add_book.html")

@app.route("/remove_book", methods=["GET", "POST"])
def remove_book():
    if request.method == "POST":
        title_to_remove = request.form["title_to_remove"]
        message = lib.remove_book(title_to_remove)
        flash(message)

        # Kitaplar listesini güncelle
        books = lib.list_books()

        return render_template("list_books.html", books=books)

    return render_template("remove_book.html")

if __name__ == "__main__":
    app.run(debug=True)
