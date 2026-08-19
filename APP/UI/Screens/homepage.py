from email.mime import image

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout

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

        console_area = AnchorLayout(
            anchor_x="center",
            anchor_y="center"
        )

        console_grid = GridLayout(
            cols=3,
            spacing=20,
            padding=20,
            size_hint=(None, None),
            width=620,
            height=500
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

        console_area.add_widget(console_grid)
        content.add_widget(console_area)

        main_layout.add_widget(content)

        self.add_widget(main_layout)