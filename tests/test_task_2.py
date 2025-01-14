#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from src.task_2 import ColorManager


class TestColorManager(unittest.TestCase):
    """
    Класс с тестами для проверки функциональности класса ColorManager.
    """

    def setUp(self) -> None:
        """
        Создаёт экземпляр ColorManager с предопределённым набором цветов
        и их кодов перед каждым тестом.
        """

        self.colors = {
            "Красный": "#ff0000",
            "Оранжевый": "#ff7d00",
            "Желтый": "#ffff00",
            "Зеленый": "#00ff00",
            "Голубой": "#007dff",
            "Синий": "#0000ff",
            "Фиолетовый": "#7d00ff",
        }
        self.color_manager = ColorManager(self.colors)

    def test_get_valid_color_code(self) -> None:
        """
        Проверяет, что метод get_color_code возвращает корректный
        шестнадцатеричный код для существующих цветов.
        """

        self.assertEqual(self.color_manager.get_color_code("Красный"), "#ff0000")
        self.assertEqual(self.color_manager.get_color_code("Оранжевый"), "#ff7d00")
        self.assertEqual(self.color_manager.get_color_code("Фиолетовый"), "#7d00ff")

    def test_get_invalid_color_code(self) -> None:
        """
        Проверяет, что метод get_color_code возвращает
        'Неизвестный цвет', если цвет не найден в словаре.
        """

        self.assertEqual(self.color_manager.get_color_code("Неизвестный"), "Неизвестный цвет")
        self.assertEqual(self.color_manager.get_color_code("Чёрный"), "Неизвестный цвет")


if __name__ == "__main__":
    unittest.main()
