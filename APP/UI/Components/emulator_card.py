from kivy.uix.button import Button


class EmulatorCard(Button):

    def __init__(self, system_name, **kwargs):
        super().__init__(**kwargs)

        self.text = system_name