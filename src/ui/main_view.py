from tkinter import ttk, constants

class MainView:
    def __init__(self, root, handle_show_yarns_view, handle_show_add_yarn_view, handle_show_search_yarns_view):
        self._root = root
        self._frame = None
        self._handle_show_yarns_view = handle_show_yarns_view
        self._handle_show_add_yarn_view = handle_show_add_yarn_view
        self._handle_show_search_yarns_view = handle_show_search_yarns_view

        self._initialize()

    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._frame.columnconfigure(0, weight=1)
        self._frame.rowconfigure(0, weight=1)
        self._frame.rowconfigure(1, weight=1)
        self._frame.rowconfigure(2, weight=1)

        yarns_button = ttk.Button(master=self._frame, text="Kaikki langat", command=self._handle_show_yarns_view)
        add_yarn_button = ttk.Button(master=self._frame, text="Lisää lanka", command=self._handle_show_add_yarn_view)
        search_yarns_button = ttk.Button(master=self._frame, text="Hae lankoja", command=self._handle_show_search_yarns_view)

        yarns_button.grid(row=0, column=0, sticky=constants.NSEW, padx=5, pady=5)
        add_yarn_button.grid(row=1, column=0, sticky=constants.NSEW, padx=5, pady=5)
        search_yarns_button.grid(row=2, column=0, sticky=constants.NSEW, padx=5, pady=5)

        self._frame.pack(fill="both", expand=True)
