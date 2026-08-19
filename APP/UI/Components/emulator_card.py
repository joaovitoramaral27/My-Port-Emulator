from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior
from kivy.graphics import Color, RoundedRectangle


class EmulatorCard(ButtonBehavior, BoxLayout):

    def __init__(self, system_name, image, on_select=None, **kwargs):
        super().__init__(**kwargs)

        self.system_name = system_name
        self.on_select = on_select

        self.orientation = "vertical"

        self.size_hint = (None, None)
        self.size = (180, 220)

        self.spacing = 10
        self.padding = 10

        with self.canvas.before:
            Color(0.05, 0.07, 0.15, 1)

            self.background = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[15]
            )

        self.bind(
            pos=self.update_background,
            size=self.update_background
        )

        icon = Image(
            source=image,
            allow_stretch=True,
            keep_ratio=True
        )

        name = Label(
            text=system_name,
            size_hint_y=None,
            height=30
        )

        self.add_widget(icon)
        self.add_widget(name)

    def update_background(self, *args):
        self.background.pos = self.pos
        self.background.size = self.size

    def on_press(self):
        print(f"{self.system_name} pressionado")

    def on_release(self):
        print(f"Selecionado: {self.system_name}")

        if self.on_select:
            self.on_select(self.system_name)