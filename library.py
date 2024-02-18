class Library:
    def __init__(self):
        self.file_path = "books.txt"
        self.file = open(self.file_path, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        book_lines = self.file.read().splitlines()
        for line in book_lines:
            book_info = line.split(',')
            print(f"Kitap: {book_info[0]}, Yazar: {book_info[1]}")

    def add_book(self):
        title = input("Kitap adını girin: ")
        author = input("Yazarı girin: ")
        release_year = input("Yayın yılı girin: ")
        num_pages = input("Sayfa sayısını girin: ")

        book_info = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        print("Kitap başarıyla eklendi!")

    def remove_book(self):
        title_to_remove = input("Kaldırmak istediğiniz kitabın adını girin: ")

        self.file.seek(0)
        book_lines = self.file.read().splitlines()
        
        updated_book_lines = [line for line in book_lines if title_to_remove not in line]

        self.file.seek(0)
        self.file.truncate()
        self.file.writelines('\n'.join(updated_book_lines))
        print(f"'{title_to_remove}' adlı kitap başarıyla kaldırıldı!")


lib = Library()

while True:
    print("\n*** MENÜ ***")
    print("1) Kitapları Listele")
    print("2) Kitap Ekle")
    print("3) Kitap Kaldır")
    print("4) Çıkış")

    user_input = input("Seçiminizi girin (1-4): ")

    if user_input == '1':
        lib.list_books()
    elif user_input == '2':
        lib.add_book()
    elif user_input == '3':
        lib.remove_book()
    elif user_input == '4':
        break
    else:
        print("Geçersiz giriş. Lütfen geçerli bir seçenek girin.")
