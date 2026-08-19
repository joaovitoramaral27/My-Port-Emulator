from email.mime import image

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from APP.UI.Components.emulator_card import EmulatorCard

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
            text="👤 Profile ▼"
        )

        title_label = Label(
            text="Omni"
        )

        header.add_widget(profile_label)
        header.add_widget(title_label)

        main_layout.add_widget(header)

        content = BoxLayout(
            orientation="vertical"
        )

        console_grid = GridLayout(
            cols=3
        )

        console_grid.add_widget(
            EmulatorCard(image="Assets/GBicon.png", system_name="GB")
        )

        console_grid.add_widget(
            EmulatorCard(image=None, system_name="GBC")
        )

        console_grid.add_widget(
            EmulatorCard(image=None, system_name="GBA")
        )

        console_grid.add_widget(
            EmulatorCard(image=None, system_name="NDS")
        )

        console_grid.add_widget(
            EmulatorCard(image=None, system_name="3DS")
        )

        content.add_widget(console_grid)

        main_layout.add_widget(content)

        self.add_widget(main_layout)