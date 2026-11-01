import os
import sys

def setup_android():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    if root_dir not in sys.path:
        sys.path.insert(0, root_dir)
    
    # Добавляем только frontend, backend не нужен!
    frontend_dir = os.path.join(root_dir, 'frontend')
    if frontend_dir not in sys.path:
        sys.path.insert(0, frontend_dir)

if __name__ == '__main__':
    setup_android()
    from main import MunchkinApp
    MunchkinApp().run()