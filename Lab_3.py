class Book:
    """Базовый класс книги."""

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = None
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise ValueError("Pages must be an integer.")
        if value <= 0:
            raise ValueError("Number of pages must be greater than zero.")
        self._pages = value


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = None
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Duration must be a number.")
        if value <= 0:
            raise ValueError("Duration must be greater than zero.")
        self._duration = value


# Пример использования:
paper_book = PaperBook("Тайна", "Иванов", 300)
audio_book = AudioBook("Путешествие", "Петров", 5.5)

# Пример попытки недопустимого значения (приведет к ошибке)
# paper_book.pages = "Invalid"  # ValueError: Pages must be an integer.
# audio_book.duration = -3  # ValueError: Duration must be greater than zero.

print(paper_book.pages)  # 300
print(audio_book.duration)  # 5.5
