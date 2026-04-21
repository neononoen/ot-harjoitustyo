from tkinter import ttk, constants
from services.yarn_service import yarn_service

class YarnListView:
    def __init__(self, root, yarns):
        self._root = root
        self._yarns = yarns
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill="both")

    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        for yarn in self._yarns:
            self._initialize_yarn(yarn)

    def _initialize_yarn(self, yarn):
        yarn_frame = ttk.Frame(master=self._frame)

        name_label = ttk.Label(master=yarn_frame, text=yarn.name)
        colour_label = ttk.Label(master=yarn_frame, text=yarn.colour)
        weight_label = ttk.Label(master=yarn_frame, text=f'{yarn.weight} g')
        meters_label = ttk.Label(master=yarn_frame, text=f'{yarn.meters} m')
        type_label = ttk.Label(master=yarn_frame, text=yarn.type)

        for i in range(6):
            yarn_frame.columnconfigure(i, weight=1)

        name_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.E)
        colour_label.grid(row=0, column=1, padx=5, pady=5, sticky=constants.E)
        weight_label.grid(row=0, column=2, padx=5, pady=5, sticky=constants.E)
        meters_label.grid(row=0, column=3, padx=5, pady=5, sticky=constants.E)
        type_label.grid(row=0, column=4, padx=5, pady=5, sticky=constants.E)

        yarn_frame.pack(fill='x')

class SearchYarnsView:
    def __init__(self, root, handle_show_main_view):
        self._root = root
        self._handle_show_main_view = handle_show_main_view
        self._frame = None
        self._search_fields_frame = None
        self._meters_entry = None
        self._yarn_list_view = None
        self._yarn_list_frame = None
        
        self._initialize()

    def destroy(self):
        self._frame.destroy()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._yarn_list_frame = ttk.Frame(master=self._frame)

        self._initialize_search_fields()

    def _initialize_header(self):
        pass


    def _initialize_search_fields(self):
        self._search_fields_frame = ttk.Frame(master=self._frame)

        meters_label = ttk.Label(master=self._search_fields_frame, text="Metrimäärä:")
        self._meters_entry = ttk.Entry(master=self._search_fields_frame)
        search_button = ttk.Button(master=self._search_fields_frame, text="Hae", command=self._handle_search)


        meters_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)
        self._meters_entry.grid(row=0, column=1, padx=5, pady=5, sticky=constants.W)
        search_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        
        self._search_fields_frame.pack()

    def _handle_search(self):
        if self._yarn_list_frame:
            self._yarn_list_frame.destroy()
        
        self._yarn_list_frame = ttk.Frame(master=self._frame)
        self._yarn_list_frame.pack()

        meters = self._meters_entry.get()

        yarns = yarn_service.get_yarns_by_meterage(int(meters))

        self._initialize_yarns(yarns)
    
    def _initialize_yarns(self, yarns):
        if self._yarn_list_view:
            self._yarn_list_view.destroy()
        
        self._yarn_list_view = YarnListView(self._yarn_list_frame, yarns)

        self._yarn_list_view.pack()
