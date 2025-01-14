#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from src.task_3 import ColorManager


class TestColorManager(unittest.TestCase):
    """
    Класс тестов для проверки функциональности ColorManager.
    """

    def setUp(self) -> None:
        """
        Подготавливает общий набор цветов для каждого теста
        и инициализирует экземпляр класса ColorManager.
        """

        self.colors = {
            "красный": "#ff0000",
            "оранжевый": "#ff7f00",
            "желтый": "#ffff00",
            "зеленый": "#00ff00",
            "голубой": "#00ffff",
            "синий": "#0000ff",
            "фиолетовый": "#7f00ff",
        }
        self.color_manager = ColorManager(self.colors)

    def test_get_valid_color_code(self) -> None:
        """
        Проверяет корректное получение существующих цветовых кодов.
        """

        self.assertEqual(self.color_manager.get_color_code("красный"), "#ff0000")
        self.assertEqual(self.color_manager.get_color_code("желтый"), "#ffff00")
        self.assertEqual(self.color_manager.get_color_code("фиолетовый"), "#7f00ff")

    def test_get_invalid_color_code(self) -> None:
        """
        Проверяет поведение при запросе несуществующего цвета.
        Ожидаем, что будет возвращён белый цвет (#ffffff) по умолчанию.
        """

        self.assertEqual(self.color_manager.get_color_code("неизвестный"), "#ffffff")


if __name__ == "__main__":
    unittest.main()
