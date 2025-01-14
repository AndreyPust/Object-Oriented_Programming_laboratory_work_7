#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
import unittest

from src.task_5 import ContactApp


class TestContactApp(unittest.TestCase):
    """
    Класс тестов для проверки функциональности ContactApp.
    """

    def setUp(self) -> None:
        """
        Создаёт тестовое приложение перед каждым тестом.
        Инициализирует словарь с контактами и создаёт экземпляр ContactApp,
        связывая его с корневым окном Tk.
        """

        self.root = tk.Tk()
        self.contacts = {"Вася": "+7 928 822 76 78", "Петя": "+7 933 995 65 90", "Маша": "+7 926 906 81 11"}
        self.app = ContactApp(self.root, self.contacts)

    def tearDown(self) -> None:
        """
        Закрывает окно приложения после каждого теста.
        """

        self.root.destroy()

    def test_initial_state(self) -> None:
        """
        Проверяет начальное состояние приложения:
        - Убедиться, что переменная self.selected_contact пустая ("");
        - Убедиться, что в метке не отображается никакой текст.
        """

        self.assertEqual(self.app.selected_contact.get(), "")
        self.assertEqual(self.app.info_label.cget("text"), "")

    def test_show_info(self) -> None:
        """
        Тест метода show_info().
        При передачи ключей проверяем, что метка содержит соответствующие
        значения из self.contacts.
        """

        self.app.show_info("Вася")
        self.assertEqual(self.app.info_label.cget("text"), "+7 928 822 76 78")

        self.app.show_info("Петя")
        self.assertEqual(self.app.info_label.cget("text"), "+7 933 995 65 90")

        self.app.show_info("Маша")
        self.assertEqual(self.app.info_label.cget("text"), "+7 926 906 81 11")

    def test_radiobutton_selection(self) -> None:
        """
        Тест выбора значения радиокнопки.
        """

        self.app.selected_contact.set("Вася")
        self.app.show_info("Вася")
        self.assertEqual(self.app.info_label.cget("text"), "+7 928 822 76 78")

        self.app.selected_contact.set("Петя")
        self.app.show_info("Петя")
        self.assertEqual(self.app.info_label.cget("text"), "+7 933 995 65 90")


if __name__ == "__main__":
    unittest.main()
