#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from unittest.mock import mock_open, patch

from src.task_4 import FileManager


class TestFileManager(unittest.TestCase):
    """
    Класс тестов для проверки функциональности класса FileManager.
    """

    def setUp(self) -> None:
        """
        Создаёт экземпляр FileManager, который будет использоваться во всех тестах.
        """
        self.file_manager = FileManager()

    @patch("builtins.open", new_callable=mock_open, read_data="test content")
    def test_open_file_success(self, mock_file: mock_open) -> None:
        """
        Тест на успешное открытие файла:
        - mock_open эмулирует чтение из файла, возвращая строку "test content".
        - Проверяем, что метод open_file возвращает корректное содержимое.
        """

        content = self.file_manager.open_file("test.txt")
        self.assertEqual(content, "test content")
        mock_file.assert_called_once_with("test.txt", "r", encoding="utf-8")

    @patch("tkinter.messagebox.showerror")
    def test_open_file_not_found(self, mock_messagebox) -> None:
        """
        Тест на реакцию при отсутствии файла.
        Ожидается, что метод open_file вернёт None и будет показано окно с ошибкой.
        """

        content = self.file_manager.open_file("nonexistent.txt")
        self.assertIsNone(content)
        mock_messagebox.assert_called_once_with("Ошибка", "Файл nonexistent.txt не найден!")

    @patch("tkinter.messagebox.showerror")
    @patch("builtins.open", side_effect=PermissionError("Permission denied"))
    def test_open_file_permission_error(self, mock_file, mock_messagebox) -> None:
        """
        Тест на реакцию при ошибке прав доступа при чтении файла.
        Ожидается, что метод open_file вернёт None и будет показано окно с ошибкой.
        """

        content = self.file_manager.open_file("test.txt")
        self.assertIsNone(content)
        mock_messagebox.assert_called_once_with("Ошибка", "Не удалось открыть файл: Permission denied")


if __name__ == "__main__":
    unittest.main()
