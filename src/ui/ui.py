from ui.add_yarn_view import AddYarnView
from ui.yarns_view import YarnsView
from ui.main_view import MainView

class UI:
    def __init__(self, root):
        self._root= root
        self._current_view = None
    
    def start(self):
        self._show_main_view()
    
    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
    
    def _show_main_view(self):
        self._hide_current_view()

        self._current_view = MainView(self._root, self._show_yarns_view, self._show_add_yarn_view)

    def _show_add_yarn_view(self):
        self._hide_current_view()

        self._current_view = AddYarnView(self._root, self._show_main_view)
    
    def _show_yarns_view(self):
        self._hide_current_view()

        self._current_view = YarnsView(self._root, self._show_main_view)

