from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window

from APP.UI.Screens.homepage import Homepage
#from APP.UI.Screens.gamelist import Gamelist
from APP.UI.theme import BACKGROUND

Window.clearcolor = BACKGROUND

class MyPortApp(App):

    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(Homepage(name="homepage"))
        #screen_manager.add_widget(Gamelist(name="gamelist"))

        return screen_manager


if __name__ == "__main__":
    MyPortApp().run()