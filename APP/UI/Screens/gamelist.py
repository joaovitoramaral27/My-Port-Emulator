from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button


class GameList(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.system_name = None

        main_layout = BoxLayout(
            orientation="vertical"
        )

        header = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height=60
        )

        back_button = Button(
            text="<",
            size_hint_x=None,
            width=50
        )

        back_button.bind(
            on_release=self.go_home
        )

        self.emu_image = Image(
            size_hint_x=None,
            width=40
        )

        self.emu_label = Label()

        header.add_widget(back_button)
        header.add_widget(self.emu_image)
        header.add_widget(self.emu_label)

        main_layout.add_widget(header)

        games_label = Label(
            text="Game ROMS"
        )

        main_layout.add_widget(games_label)

        self.add_widget(main_layout)

    def set_system(self, system_name):
        self.system_name = system_name

        self.emu_label.text = system_name
        self.emu_image.source = f"Assets/{system_name}icon.png"

        print(f"GameList recebeu: {system_name}")

    def go_home(self, *args):
        self.manager.current = "homepage"