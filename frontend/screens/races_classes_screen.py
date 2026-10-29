"""
Экран списка рас и классов — только UI-логика
"""
from kivy.uix.screenmanager import Screen


class RacesClassesScreen(Screen):
    """Экран списка рас и классов"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = None
    
    def on_enter(self):
        """При входе на экран — загрузить список"""
        if self.controller:
            self.controller.load_races_and_classes()
    
    def on_back(self):
        """Вернуться на экран справочника"""
        if self.controller:
            self.controller.go_back()
    
    def on_search_text(self, text):
        """Обработчик изменения текста поиска"""
        if self.controller:
            self.controller.filter_list()
    
    def on_item_click(self, item_id, item_type):
        """Обработчик клика на элемент"""
        if self.controller:
            self.controller.open_detail(item_id, item_type)
    
    def update_list(self, items):
        """Обновить список в UI"""
        items_list = self.ids.items_list
        items_list.clear_widgets()
        
        if not items:
            from kivy.uix.label import Label
            label = Label(
                text='Ничего не найдено',
                font_size=24,
                color=(0.17, 0.09, 0.06, 1),
                size_hint_y=None,
                height=50
            )
            items_list.add_widget(label)
            return
        
        for item in items:
            from kivy.uix.button import Button
            btn = Button(
                text=item['name'],
                font_size=24,
                bold=True,
                background_color=(0.82, 0.71, 0.55, 1),
                color=(1, 1, 1, 1),
                size_hint_y=None,
                height=60
            )
            btn.bind(
                on_press=lambda instance, iid=item['id'], itype=item['type']: 
                self.on_item_click(iid, itype)
            )
            items_list.add_widget(btn)