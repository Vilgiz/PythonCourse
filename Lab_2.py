class Book:
    def __init__(self, id_, name, pages):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f'Book(id_={self.id}, name={repr(self.name)}, pages={self.pages})'


class Library:
    def __init__(self, books=None):
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self):
        if not self.books:
            return 1
        else:
            return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id):
        for i, book in enumerate(self.books):
            if book.id == book_id:
                return i
        raise ValueError("Книги с запрашиваемым id не существует")


# Создаем несколько книг
book1 = Book(id_=1, name='Тестовая книга 1', pages=100)
book2 = Book(id_=2, name='Тестовая книга 2', pages=150)

# Создаем библиотеку и добавляем книги
library = Library([book1, book2])

# Получаем следующий идентификатор для новой книги
next_id = library.get_next_book_id()

# Создаем новую книгу с использованием полученного идентификатора
new_book = Book(id_=next_id, name='Новая книга', pages=120)

# Добавляем новую книгу в библиотеку
library.books.append(new_book)

# Получаем индекс книги по её идентификатору
book_id_to_find = 2
try:
    index = library.get_index_by_book_id(book_id_to_find)
    print(f"Книга найдена. Индекс: {index}")
except ValueError as e:
    print(e)
