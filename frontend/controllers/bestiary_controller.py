"""
Контроллер бестиария — бизнес-логика списка монстров
"""
from app.database import SessionLocal
from app.services.catalog_service import CatalogService


class BestiaryController:
    """Логика экрана списка бестиария"""
    
    def __init__(self, screen):
        self.screen = screen
        self._all_monsters = []  # Все загруженные монстры
        self._current_filter = 'all'  # Текущий фильтр
        self._search_text = ''  # Текущий поисковый запрос
    
    def load_bestiary(self):
        """Загрузить весь бестиарий из БД"""
        db = SessionLocal()
        try:
            catalog = CatalogService(db)
            monsters = catalog.bestiary_list()
            
            # Преобразуем в список словарей для удобства
            self._all_monsters = [
                {
                    'id': m.id_bestiary,
                    'name': m.name,
                    'type': m.monster_type,
                    'level': m.level,
                    'description': m.description,
                    'quirk': m.quirk,
                    'xp_reward': m.xp_reward,
                    'treasure_reward': m.treasure_reward,
                }
                for m in monsters
            ]
            
            self.filter_bestiary()
        except Exception as e:
            print(f'Ошибка загрузки бестиария: {e}')
        finally:
            db.close()
    
    def filter_bestiary(self):
        """Фильтрация монстров по типу и поисковому запросу"""
        # Получаем текущие значения из UI
        search_text = self.screen.ids.search_input.text.strip().lower()
        filter_value = self.screen.ids.filter_dropdown.text
        
        # Определяем тип фильтра
        if filter_value == 'Все':
            self._current_filter = 'all'
        elif filter_value == 'Нормальные':
            self._current_filter = 'normal'
        elif filter_value == 'Андеды':
            self._current_filter = 'undead'
        elif filter_value == 'Драконы':
            self._current_filter = 'dragon'
        
        # Применяем фильтры
        filtered = self._all_monsters
        
        # Фильтр по типу
        if self._current_filter != 'all':
            filtered = [m for m in filtered if m['type'] == self._current_filter]
        
        # Фильтр по поиску
        if search_text:
            filtered = [m for m in filtered if search_text in m['name'].lower()]
        
        # Обновляем UI
        self.screen.update_monster_list(filtered)
    
    def open_monster_detail(self, monster_id):
        """Открыть экран с детальным описанием монстра"""
        # Находим монстра в списке
        monster = next((m for m in self._all_monsters if m['id'] == monster_id), None)
        
        if monster:
            # Передаем данные на экран деталей
            detail_screen = self.screen.manager.get_screen('monster_detail')
            detail_screen.controller.set_monster_data(monster)
            self.screen.manager.current = 'monster_detail'
    
    def go_back(self):
        """Вернуться на экран справочника"""
        self.screen.manager.current = 'catalog'