import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Приветствие по времени суток"
    page.theme_mode = ft.ThemeMode.LIGHT

    name_field = ft.TextField(label="Введите имя")
    greeting_text = ft.Text("")

    def greet(e):
        name = name_field.value.strip()
        if not name:
            greeting_text.value = "Введите имя!"
        
        else:
            hour = datetime.now().hour
            if 6 <= hour < 12:
                greeting = "Доброе утро"
            elif 12 <= hour < 18:
                greeting = "Добрый день"
            elif 18 <= hour < 24:
                greeting = "Добрый вечер"
            else:
                greeting = "Доброй ночи"
            greeting_text.value = f"{greeting}, {name}!"
        page.update()

    def toggle_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()

    greet_button = ft.ElevatedButton("Поздороваться", on_click=greet)
    theme_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=toggle_theme)

    page.add(name_field, greet_button, greeting_text, theme_button)

ft.app(target=main)
