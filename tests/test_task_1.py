#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from src.task_1 import Calculator


class TestCalculator(unittest.TestCase):
    """
    Класс для тестирования основных арифметических операций,
    реализованных в классе Calculator.
    """

    def setUp(self) -> None:
        """
        Инициализирует экземпляр класса Calculator перед запуском каждого теста.
        """

        self.calculator = Calculator()

    def test_addition(self) -> None:
        """
        Тест операции сложения.
        """

        self.assertEqual(self.calculator.calculate(5, 3, "+"), 8)

    def test_subtraction(self) -> None:
        """
        Тест операции вычитания.
        """

        self.assertEqual(self.calculator.calculate(5, 3, "-"), 2)

    def test_multiplication(self) -> None:
        """
        Тест операции умножения.
        """

        self.assertEqual(self.calculator.calculate(5, 3, "*"), 15)

    def test_division(self) -> None:
        """
        Тест операции деления.
        """

        self.assertEqual(self.calculator.calculate(6, 3, "/"), 2)

    def test_division_by_zero(self) -> None:
        """
        Тест операции деления на ноль.
        Ожидается, что результатом будет строка 'ошибка'.
        """

        self.assertEqual(self.calculator.calculate(6, 0, "/"), "ошибка")

    def test_invalid_operation(self) -> None:
        """
        Тест некорректной операции (неизвестный символ операции).
        Ожидается, что результатом будет строка 'ошибка'.
        """

        self.assertEqual(self.calculator.calculate(6, 3, "%"), "ошибка")

    def test_invalid_input(self) -> None:
        """
        Тест некорректного ввода чисел.
        """

        with self.assertRaises(TypeError):
            self.calculator.calculate("a", 3, "+")

        with self.assertRaises(TypeError):
            self.calculator.calculate(5, "b", "-")

        with self.assertRaises(TypeError):
            self.calculator.calculate("a", "b", "*")


if __name__ == "__main__":
    unittest.main()
