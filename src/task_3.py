#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Программа с графическим интерфейсом (Tkinter) для отображения и выбора цветов.
При запуске создаётся окно с меткой, в которой отображается название текущего
цвета, и с текстовым полем, куда выводится его шестнадцатеричный код.
Семь кнопок, каждая из которых окрашена в один из цветов, располагаются
горизонтально. При нажатии кнопки метка и текстовое поле обновляются
соответствующими значениями.
"""

import tkinter as tk
from typing import Dict


class ColorManager:
    """
    Класс для управления набором цветов.
    Хранит соответствия названий цветов их шестнадцатеричным кодам.
    """

    def __init__(self, colors: Dict[str, str]) -> None:
        """
        Инициализирует ColorManager словарём, в котором ключ — это название цвета,
        а значение — его шестнадцатеричный код.

        :param colors: Словарь вида {название_цвета: hex-код_цвета}.
        """
        self.colors = colors

    def get_color_code(self, color_name: str) -> str:
        """
        Возвращает шестнадцатеричный код цвета по его названию. Если цвет
        не найден, возвращает белый цвет (#ffffff) по умолчанию.

        :param color_name: Название цвета.
        :return: Шестнадцатеричный код цвета или #ffffff, если цвет не найден.
        """
        return self.colors.get(color_name, "#ffffff")


class ColorApp:
    """
    Класс приложения, позволяющего выбрать цвет из набора и отобразить название
    и шестнадцатеричный код выбранного цвета.
    """

    def __init__(self, root: tk.Tk, color_manager: ColorManager) -> None:
        """
        Инициализирует приложение, создавая необходимые элементы интерфейса
        и связывая их с обработчиками.

        :param root: Главное окно приложения (экземпляр tk.Tk).
        :param color_manager: Экземпляр ColorManager для получения кодов цветов.
        """
        self.root: tk.Tk = root
        self.color_manager: ColorManager = color_manager
        self.create_widgets()

    def create_widgets(self) -> None:
        """
        Создаёт и размещает элементы интерфейса:
        - Метку с начальным названием цвета (по умолчанию "желтый");
        - Текстовое поле, куда вставляется код выбранного цвета;
        - Горизонтальные кнопки, каждая из которых окрашена в соответствующий цвет.
        """
        # Метка, отображающая название текущего цвета
        self.label: tk.Label = tk.Label(self.root, text="желтый", width=20, font=("Arial", 14))
        self.label.pack(pady=5)

        # Текстовое поле для отображения кода цвета
        self.color_code_entry: tk.Entry = tk.Entry(self.root, width=10, justify="center", font=("Arial", 14))
        self.color_code_entry.insert(0, self.color_manager.get_color_code("желтый"))
        self.color_code_entry.pack(pady=5)

        # Создаём горизонтальные кнопки для каждого цвета из словаря
        for color_name, color_code in self.color_manager.colors.items():
            btn: tk.Button = tk.Button(
                self.root,
                bg=color_code,
                width=4,
                height=2,
                command=lambda c=color_name: self.update_color(c),  # type: ignore
            )
            # Размещаем кнопки слева направо в одной строке
            btn.pack(side=tk.LEFT, padx=2, pady=10)

    def update_color(self, selected_color: str) -> None:
        """
        Обработчик нажатия кнопки, обновляет текстовое поле и метку
        в соответствии с выбранным цветом.

        :param selected_color: Название выбранного цвета.
        """
        # Получаем код выбранного цвета из ColorManager
        color_code = self.color_manager.get_color_code(selected_color)

        # Обновляем текстовое поле кодом цвета
        self.color_code_entry.delete(0, tk.END)
        self.color_code_entry.insert(0, color_code)

        # Обновляем метку названием цвета
        self.label.config(text=selected_color)


def main() -> None:
    """
    Основная функция программы. Создаёт окно, инициализирует объекты ColorManager
    и ColorApp, а затем запускает главный цикл обработки событий.
    """
    # Словарь с набором цветов (название_цвета -> шестнадцатеричный_код)
    colors: Dict[str, str] = {
        "красный": "#ff0000",
        "оранжевый": "#ff7f00",
        "желтый": "#ffff00",
        "зеленый": "#00ff00",
        "голубой": "#00ffff",
        "синий": "#0000ff",
        "фиолетовый": "#7f00ff",
    }

    root: tk.Tk = tk.Tk()
    root.title("Цветовая палитра")

    # Создаём экземпляр ColorManager
    color_manager: ColorManager = ColorManager(colors)

    # Создаём экземпляр приложения и запускаем цикл обработки событий
    app: ColorApp = ColorApp(root, color_manager)
    root.mainloop()


if __name__ == "__main__":
    main()
