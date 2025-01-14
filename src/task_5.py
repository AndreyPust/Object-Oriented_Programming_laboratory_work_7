#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Виджеты Radiobatton и Checkbutton поддерживают большинство свойств
# оформления внешнего вида, которые есть у других элементов графического
# интерфейса. При этом у Radiobutton есть особое свойство indicatoron.
# По-умолчанию он равен единице, в этом случае радиокнопка выглядит как
# нормальная радиокнопка. Однако если присвоить этой опции ноль, то виджет
# Radiobutton становится похожим на обычную кнопку по внешнему виду.
# Но не по смыслу.
# Напишите программу, в которой имеется несколько объединенных в группу
# радиокнопок, индикатор которых выключен ( indicatoron=0 ). Если какая-нибудь
# кнопка включается, то в метке должна отображаться соответствующая ей информация.
# Обычных кнопок в окне быть не должно.

import tkinter as tk
from typing import Dict


class ContactApp:
    """
    Класс приложения, демонстрирующего работу радиокнопок, внешне
    похожих на обычные кнопки, но сохранивших поведение Radiobutton.
    """

    def __init__(self, root: tk.Tk, contacts: Dict[str, str]) -> None:
        """
        Инициализирует приложение, принимая на вход основное окно и
        словарь с контактными данными.

        :param root: Главное окно приложения.
        :param contacts: Словарь контактов.
        """

        self.contacts: Dict[str, str] = contacts
        # StringVar для хранения выбранного контакта
        self.selected_contact: tk.StringVar = tk.StringVar(value="")

        # Создаём и размещаем виджеты интерфейса
        self.create_widgets(root)

    def create_widgets(self, root: tk.Tk) -> None:
        """
        Создаёт основные элементы графического интерфейса.
        Фрейм с радиокнопками и метку для отображения информации.

        :param root: Главное окно приложения.
        """

        # Фрейм для радиокнопок
        frame: tk.Frame = tk.Frame(root)
        frame.pack(side=tk.LEFT, padx=10, pady=10)

        # Создание «кнопок»-радиокнопок с отключённым индикатором
        for name in self.contacts.keys():
            rb: tk.Radiobutton = tk.Radiobutton(
                frame,
                text=name,  # Текст, отображаемый на кнопке
                variable=self.selected_contact,  # Общая переменная для всех радиокнопок
                value=name,  # Значение, присваиваемое этой переменной при выборе
                indicatoron=bool(0),  # Отключает индикатор, делая радиокнопку похожей на обычную кнопку
                width=10,
                command=lambda n=name: self.show_info(n),  # type: ignore
            )
            rb.pack(pady=5)

        # Метка для отображения информации о выбранном пункте
        self.info_label: tk.Label = tk.Label(root, text="", width=30, anchor="w", font=("Arial", 14))
        self.info_label.pack(side=tk.LEFT, padx=10, pady=10)

    def show_info(self, name: str) -> None:
        """
        Обработчик переключения радиокнопок. По названию контакта получает
        соответствующую информацию и отображает её в метке.

        :param name: Ключ (название контакта).
        """

        info: str = self.contacts.get(name, "")
        self.info_label.config(text=info)


def main() -> None:
    """
    Основная функция, создаёт окно Tk, инициализирует словарь с контактами
    и запускает приложение ContactApp в главном цикле событий.
    """
    contacts: Dict[str, str] = {"Вася": "+7 928 822 76 78", "Петя": "+7 933 995 65 90", "Маша": "+7 926 906 81 11"}

    # Создаём главное окно
    root: tk.Tk = tk.Tk()
    root.title("Контакты")

    # Запускаем приложение
    app: ContactApp = ContactApp(root, contacts)

    # Главный цикл обработки событий
    root.mainloop()


if __name__ == "__main__":
    main()
