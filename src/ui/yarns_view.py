from tkinter import ttk, constants
from services.yarn_service import yarn_service

class YarnsView:
    def __init__(self, root, handle_show_main_view):
        self._root = root
        self._handle_show_main_view = handle_show_main_view
        self._yarns = yarn_service.get_all_yarns()
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        for yarn in self._yarns:
            self._initialize_yarn(yarn)
        
    
    def _initialize_yarn(self, yarn):
        yarn_frame = ttk.Frame(master=self._root)
        
        name_label = ttk.Label(master=yarn_frame, text=yarn.name)
        colour_label = ttk.Label(master=yarn_frame, text=yarn.colour)
        weight_label = ttk.Label(master=yarn_frame, text=f'{yarn.weight} g')
        meters_label = ttk.Label(master=yarn_frame, text=f'{yarn.meters} m')
        type_label = ttk.Label(master=yarn_frame, text=yarn.type)

        name_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)
        colour_label.grid(row=0, column=1, padx=5, pady=5, sticky=constants.W)
        weight_label.grid(row=0, column=2, padx=5, pady=5, sticky=constants.W)
        meters_label.grid(row=0, column=3, padx=5, pady=5, sticky=constants.W)
        type_label.grid(row=0, column=4, padx=5, pady=5, sticky=constants.W)

        yarn_frame.columnconfigure(0, weight=3)
        yarn_frame.columnconfigure(1, weight=2)
        yarn_frame.columnconfigure(2, weight=1)
        yarn_frame.columnconfigure(3, weight=1)
        yarn_frame.columnconfigure(4, weight=2)

        yarn_frame.pack()
