from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class Homepage(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        main_layout = BoxLayout(
            orientation="vertical"
        )

        header = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height=60
        )

        profile_label = Label(
            text="👤 João ▼"
        )

        title_label = Label(
            text="MY-PORT"
        )

        header.add_widget(profile_label)
        header.add_widget(title_label)

        main_layout.add_widget(header)

        content = BoxLayout(
            orientation="vertical"
        )

        title = Label(
            text="ESCOLHA SEU CONSOLE"
        )

        content.add_widget(title)

        console_grid = GridLayout(
            cols=3
        )

        console_grid.add_widget(
            Label(text="GAME BOY")
        )

        console_grid.add_widget(
            Label(text="GBC")
        )

        console_grid.add_widget(
            Label(text="GBA")
        )

        console_grid.add_widget(
            Label(text="NDS")
        )

        console_grid.add_widget(
            Label(text="3DS")
        )

        content.add_widget(console_grid)

        main_layout.add_widget(content)

        self.add_widget(main_layout)