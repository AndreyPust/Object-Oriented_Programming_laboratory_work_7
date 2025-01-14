#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Напишите простейший калькулятор, состоящий из двух текстовых полей,
# куда пользователь вводит числа, и четырех кнопок "+", "-", "*", "/".
# Результат вычисления должен отображаться в метке. Если арифметическое
# действие выполнить невозможно (например, если были введены буквы, а
# не числа), то в метке должно появляться слово "ошибка".

import tkinter as tk
from typing import Union


class Calculator:
    """
    Класс калькулятора, реализующий базовые арифметические операции.
    """

    def calculate(self, first: float, second: float, operation: str) -> Union[float, str]:
        """
        Выполняет арифметические операции (сложение, вычитание, умножение, деление).

        :param first: Первое число.
        :param second: Второе число.
        :param operation: Строка, обозначающая требуемую операцию: "+", "-", "*", "/".
        :return: Результат вычисления (float или "ошибка" при делении на ноль или неверном типе операции).
        """

        if operation == "+":
            return first + second
        elif operation == "-":
            return first - second
        elif operation == "*":
            return first * second
        elif operation == "/":
            # Проверяем деление на ноль
            return first / second if second != 0 else "ошибка"
        return "ошибка"


class CalculatorApp:
    """
    Класс, отвечающий за графический интерфейс калькулятора на базе Tkinter.
    """

    def __init__(self, root: tk.Tk, calculator: Calculator) -> None:
        """
        Инициализирует приложение, создавая все необходимые элементы интерфейса.

        :param root: Окно (экземпляр tk.Tk), в котором будут размещаться все элементы.
        :param calculator: Экземпляр класса Calculator, выполняющий арифметические операции.
        """

        self.root = root
        self.calculator = calculator
        self.create_widgets()

    def create_widgets(self) -> None:
        """
        Создаёт и размещает на форме все виджеты: поля ввода, кнопки операций и метку для результата.
        """

        # Поля ввода для двух чисел
        self.entry1 = tk.Entry(self.root, width=10)
        self.entry1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.entry2 = tk.Entry(self.root, width=10)
        self.entry2.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        # Кнопки операций
        btn_add = tk.Button(self.root, text="+", width=5, command=lambda: self.calculate("+"))
        btn_add.grid(row=2, column=0, columnspan=2, padx=5, pady=2)

        btn_sub = tk.Button(self.root, text="-", width=5, command=lambda: self.calculate("-"))
        btn_sub.grid(row=3, column=0, columnspan=2, padx=5, pady=2)

        btn_mul = tk.Button(self.root, text="*", width=5, command=lambda: self.calculate("*"))
        btn_mul.grid(row=4, column=0, columnspan=2, padx=5, pady=2)

        btn_div = tk.Button(self.root, text="/", width=5, command=lambda: self.calculate("/"))
        btn_div.grid(row=5, column=0, columnspan=2, padx=5, pady=2)

        # Метка для отображения результата
        self.result_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.result_label.grid(row=6, column=0, columnspan=2, pady=10)

    def calculate(self, operation: str) -> None:
        """
        Получает значения из полей ввода, вызывает метод calculate() у объекта Calculator
        и отображает результат в метке. Если введены неверные данные, выводит "ошибка".

        :param operation: Строка, обозначающая требуемую операцию: "+", "-", "*", "/".
        :return: None
        """

        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            result = self.calculator.calculate(num1, num2, operation)
            self.result_label.config(text=str(result))
        except ValueError:
            self.result_label.config(text="ошибка")


def main() -> None:
    """
    Главная функция: создаёт окно, инициализирует приложение калькулятора и запускает главный цикл.
    """

    root = tk.Tk()
    root.title("Калькулятор")

    # Создаем экземпляры калькулятора и приложения
    calculator = Calculator()
    app = CalculatorApp(root, calculator)

    # Запускаем основной цикл обработки событий
    root.mainloop()


if __name__ == "__main__":
    main()
