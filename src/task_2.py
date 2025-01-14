#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Напишите программу, состоящую из семи кнопок, цвета которых соответствуют
# цветам радуги. При нажатии на ту или иную кнопку в текстовое поле должен
# вставляться код цвета, а в метку – название цвета. Коды цветов в шестнадцатеричной
# кодировке: #ff0000 – красный, #ff7d00 – оранжевый, #ffff00 – желтый,
# 00ff00 – зеленый, #007dff – голубой, #0000ff – синий, #7d00ff – фиолетовый.

import tkinter as tk
from typing import Dict


class ColorManager:
    """
    Класс для управления цветовыми данными.
    """

    def __init__(self, colors: Dict[str, str]) -> None:
        """
        Инициализирует ColorManager, принимая на вход словарь соответствия:
        название цвета -> шестнадцатеричный код.

        :param colors: Словарь кодов цветов.
        """

        self.colors = colors

    def get_color_code(self, color_name: str) -> str:
        """
        Возвращает код цвета по его названию. Если цвет не найден,
        возвращает строку "Неизвестный цвет".

        :param color_name: Название цвета.
        :return: Строка с шестнадцатеричным кодом цвета.
        """

        return self.colors.get(color_name, "Неизвестный цвет")


class ColorApp:
    """
    Класс, представляющий графическое приложение для отображения цветов радуги.
    """

    def __init__(self, root: tk.Tk, color_manager: ColorManager) -> None:
        """
        Инициализирует класс ColorApp.

        :param root: Главное окно приложения.
        :param color_manager: Экземпляр класса ColorManager.
        """

        self.root: tk.Tk = root
        self.color_manager: ColorManager = color_manager
        self.create_widgets()

    def create_widgets(self) -> None:
        """
        Создаёт и размещает на форме все виджеты: метку для кода цвета,
        текстовое поле для названия цвета и кнопки, соответствующие цветам радуги.
        """

        # Метка для отображения кода цвета
        self.color_label: tk.Label = tk.Label(self.root, text="", font=("Arial", 14))
        self.color_label.grid(row=0, column=0, padx=5, pady=5)

        # Текстовое поле для отображения названия цвета
        self.color_entry: tk.Entry = tk.Entry(self.root, width=20, font=("Arial", 14))
        self.color_entry.grid(row=1, column=0, padx=5, pady=5)

        # Создание кнопок для каждого цвета из словаря ColorManager
        for idx, (color_name, color_code) in enumerate(self.color_manager.colors.items()):
            button: tk.Button = tk.Button(
                self.root,
                text=color_name,  # Текст на кнопке: название цвета
                bg=color_code,  # Цвет фона кнопки: шестнадцатеричный код
                width=20,
                command=lambda code=color_code, name=color_name: self.set_color(code, name),  # type: ignore
            )
            # Размещение кнопки ниже предыдущих виджетов
            button.grid(row=2 + idx, column=0, padx=5, pady=5)

    def set_color(self, color_code: str, color_name: str) -> None:
        """
        Устанавливает название цвета в текстовое поле и код цвета в метку.

        :param color_code: Шестнадцатеричный код цвета (например, "#ff0000").
        :param color_name: Название цвета (например, "Красный").
        """
        self.color_entry.delete(0, tk.END)  # Очищаем текстовое поле
        self.color_entry.insert(0, color_name)  # Вставляем название цвета в текстовое поле
        self.color_label.config(text=color_code)  # Обновляем метку, показывая код цвета


def main() -> None:
    """
    Основная функция приложения. Создаёт окно, инициализирует ColorManager и ColorApp,
    а затем запускает главный цикл обработки событий Tkinter.
    """
    # Словарь соответствий цвета радуги и их hex-кодов
    colors: Dict[str, str] = {
        "Красный": "#ff0000",
        "Оранжевый": "#ff7d00",
        "Желтый": "#ffff00",
        "Зеленый": "#00ff00",
        "Голубой": "#007dff",
        "Синий": "#0000ff",
        "Фиолетовый": "#7d00ff",
    }

    root: tk.Tk = tk.Tk()
    root.title("Цвета радуги")

    # Создаём экземпляр ColorManager, который управляет данными о цветах
    color_manager: ColorManager = ColorManager(colors)

    # Создаём и запускаем приложение
    app: ColorApp = ColorApp(root, color_manager)
    root.mainloop()


if __name__ == "__main__":
    main()
