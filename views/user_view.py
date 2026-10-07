from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

from services.user_service import UserService


class UserView(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        # Заголовок
        self.add_widget(Label(text='Управление пользователями',
                              font_size='20sp',
                              size_hint_y=None,
                              height=40))

        # Поля ввода
        self.login_input = TextInput(hint_text='Логин', multiline=False)
        self.age_input = TextInput(hint_text='Возраст', multiline=False, input_filter='int')
        self.email_input = TextInput(hint_text='Почта', multiline=False)

        self.add_widget(self.login_input)
        self.add_widget(self.age_input)
        self.add_widget(self.email_input)

        # Кнопки
        btn_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
        self.save_btn = Button(text='Сохранить данные')
        self.show_btn = Button(text='Вывести всех пользователей')
        self.save_btn.bind(on_press=self._on_save)
        self.show_btn.bind(on_press=self._on_show_all)
        btn_layout.add_widget(self.save_btn)
        btn_layout.add_widget(self.show_btn)
        self.add_widget(btn_layout)

        # Область со списком пользователей
        self.scroll = ScrollView(size_hint=(1, 1))
        self.users_layout = GridLayout(cols=1, size_hint_y=None, spacing=5)
        self.users_layout.bind(minimum_height=self.users_layout.setter('height'))
        self.scroll.add_widget(self.users_layout)
        self.add_widget(self.scroll)

        # Сервисный слой
        self.service = UserService()

    def _on_save(self, instance):
        try:
            user = self.service.create_user(
                login=self.login_input.text,
                age=self.age_input.text,
                email=self.email_input.text
            )
            print(f"Пользователь {user.login} успешно сохранён")
            self.login_input.text = ''
            self.age_input.text = ''
            self.email_input.text = ''
        except Exception as e:
            print(f"Ошибка: {e}")

    def _on_show_all(self, instance):
        self.users_layout.clear_widgets()
        try:
            users = self.service.get_all_users()
            if not users:
                self.users_layout.add_widget(
                    Label(text='Пользователей нет', size_hint_y=None, height=30)
                )
                return

            for user in users:
                text = (f"Логин: {user.login} | "
                        f"Возраст: {user.age} | "
                        f"Почта: {user.email}")
                self.users_layout.add_widget(
                    Label(text=text, size_hint_y=None, height=30)
                )
        except Exception as e:
            print(f"Ошибка при получении пользователей: {e}")