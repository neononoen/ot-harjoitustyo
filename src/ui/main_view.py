from tkinter import ttk

class MainView:
    def __init__(self, root, handle_show_yarns_view, handle_show_add_yarn_view):
        self._root = root
        self._frame = None
        self._handle_show_yarns_view = handle_show_yarns_view
        self._handle_show_add_yarn_view = handle_show_add_yarn_view

        self._initialize()

    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        yarns_button = ttk.Button(master=self._frame, text="Kaikki langat", command=self._handle_show_yarns_view)
        add_yarn_button = ttk.Button(master=self._frame, text="Lisää lanka", command=self._handle_show_add_yarn_view)

        yarns_button.grid(row=0, column=0, padx=5, pady=5)
        add_yarn_button.grid(row=1, column=0, padx=5, pady=5)

        self._frame.pack()
        

