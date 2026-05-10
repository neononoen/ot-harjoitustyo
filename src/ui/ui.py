from tkinter import ttk
from ui.add_yarn_view import AddYarnView
from ui.yarns_view import YarnsView
from ui.main_view import MainView
from ui.search_yarns_view import SearchYarnsView
from ui.stash_info_view import StashInfoView

class UI:
    """Käyttöliittymästä vastaava luokka."""
    def __init__(self, root):
        """Luokan konstruktori, joka luo uuden käyttöliittymästä vastaavan luokan.
        
        Args:
            root: Tkinter-elementti, johon käyttöliittymä alustetaan.
        """
        self._root= root
        self._current_view = None

    def _style(self):
        style = ttk.Style()
        style.configure("TFrame", background="#8BC935")
        style.configure("TLabel", font=("Monaco", 12), background="#8BC935", foreground="#000000")
        style.configure("TButton", font=("Monaco", 10), background="#F67390", foreground="#000000", borderwidth="3")

    def start(self):
        """Käynnistää käyttöliittymän."""
        self._style()
        self._show_main_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

    def _show_main_view(self):
        self._hide_current_view()

        self._current_view = MainView(self._root, self._show_yarns_view,
                                       self._show_add_yarn_view,
                                       self._show_search_yarns_view,
                                       self._show_stash_info_view)

    def _show_add_yarn_view(self):
        self._hide_current_view()

        self._current_view = AddYarnView(self._root, self._show_main_view)

        self._current_view.pack()

    def _show_yarns_view(self):
        self._hide_current_view()

        self._current_view = YarnsView(self._root, self._show_main_view)

        self._current_view.pack()

    def _show_search_yarns_view(self):
        self._hide_current_view()

        self._current_view = SearchYarnsView(self._root, self._show_main_view)

        self._current_view.pack()

    def _show_stash_info_view(self):
        self._hide_current_view()

        self._current_view = StashInfoView(self._root, self._show_main_view)

        self._current_view.pack()
