import flet as ft 

def app(page: ft.Page):
    input_field = ft.TextField(value="ввод", label="Введите что нибудь" )
    page.theme_mode = ft.ThemeMode

    def change_theme(_):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT


    def say_hello():
        text = input_field.value if input_field.value else ""
        print(text)
        if text.strip():
            plain_text.value = text 
            input_field.border_color = None
            input_field.border_color = None
        else:
            input_field.value = "не вводите пустую строку"
            input_field.border_color = ft.Colors.RED_900 


    input_field = ft.TextField(
        value="ввод", label="Введите что нибудь", on_submit=say_hello 
    )
    

    plain_text = ft.Text (value="Text")
    icon_btn = ft.IconButton(icon=ft.Icons.SEND, on_click=say_hello)
    theme_btn = ft.IconButton(icon=ft.Icons.CHANGE_CIRCLE, on_click=change_theme)


ft.run(app, view=ft.AppView.FLET_APP)

git rm -r --cached .