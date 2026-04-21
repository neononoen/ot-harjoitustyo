from tkinter import ttk, constants
from services.yarn_service import yarn_service

class YarnsView:
    def __init__(self, root, handle_show_main_view):
        self._root = root
        self._handle_show_main_view = handle_show_main_view
        self._frame = None
        self._yarn_list_frame = None
        self._yarn_frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill="both")

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        if self._frame:
            self._frame.destroy()
            
        self._frame = ttk.Frame(master=self._root)
        self._yarn_list_frame = ttk.Frame(master=self._frame)

        main_view_button = ttk.Button(master=self._frame, text="Takaisin", command=self._handle_show_main_view)
        main_view_button.grid(row=0, column=0)

        self._yarn_list_frame.grid(row=1, column=0, columnspan=2)

        yarns = yarn_service.get_all_yarns()
        for yarn in yarns:
            self._initialize_yarn(yarn)
        
    def _initialize_yarn(self, yarn):
        self._yarn_frame = ttk.Frame(master=self._yarn_list_frame)

        name_label = ttk.Label(master=self._yarn_frame, text=yarn.name)
        colour_label = ttk.Label(master=self._yarn_frame, text=yarn.colour)
        weight_label = ttk.Label(master=self._yarn_frame, text=f'{yarn.weight} g')
        meters_label = ttk.Label(master=self._yarn_frame, text=f'{yarn.meters} m')
        type_label = ttk.Label(master=self._yarn_frame, text=yarn.type)
        delete_button = ttk.Button(master=self._yarn_frame, text="Poista", command=lambda: self._handle_remove_yarn(yarn.id))

        for i in range(6):
            self._yarn_frame.columnconfigure(i, weight=1)

        name_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.E)
        colour_label.grid(row=0, column=1, padx=5, pady=5, sticky=constants.E)
        weight_label.grid(row=0, column=2, padx=5, pady=5, sticky=constants.E)
        meters_label.grid(row=0, column=3, padx=5, pady=5, sticky=constants.E)
        type_label.grid(row=0, column=4, padx=5, pady=5, sticky=constants.E)
        delete_button.grid(row=0, column=5, padx=5, pady=5, sticky=constants.E)

        self._yarn_frame.pack()

    def _handle_remove_yarn(self, yarn_id):
        yarn_service.delete_yarn(yarn_id)
        self._initialize()
        self._frame.pack()

