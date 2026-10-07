from kivy.app import App
from views.user_view import UserView


class MainApp(App):
    def build(self):
        return UserView()


if __name__ == '__main__':
    MainApp().run()