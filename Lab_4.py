from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Базовый класс для геометрических фигур.
    """

    def __init__(self, color: str):
        """
        Конструктор базового класса.

        :param color: Цвет фигуры.
        """
        self.color = color

    @abstractmethod
    def calculate_area(self) -> float:
        """
        Абстрактный метод для расчета площади фигуры.
        """
        pass

    def __str__(self) -> str:
        """
        Магический метод для строкового представления объекта.
        """
        return f"{self.color} Shape"

    def __repr__(self) -> str:
        """
        Магический метод для представления объекта в виде строки,
        которая может быть использована для воссоздания объекта.
        """
        return f"{self.__class__.__name__}(color='{self.color}')"


class Circle(Shape):
    """
    Класс для представления круга.
    """

    def __init__(self, color: str, radius: float):
        """
        Конструктор класса Circle.

        :param color: Цвет круга.
        :param radius: Радиус круга.
        """
        super().__init__(color)
        self.radius = radius

    def calculate_area(self) -> float:
        """
        Расчет площади круга.
        """
        return 3.14 * self.radius ** 2

    def get_circumference(self) -> float:
        """
        Получение длины окружности круга.

        Метод добавлен для расширения функционала дочернего класса.
        """
        return 2 * 3.14 * self.radius

    def __repr__(self) -> str:
        """
        Переопределение магического метода для воссоздания объекта класса Circle.
        """
        return f"Circle(color='{self.color}', radius={self.radius})"
