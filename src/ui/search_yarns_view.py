from tkinter import ttk, constants, StringVar
from services.yarn_service import yarn_service, InvalidInputError

class YarnListView:
    """Luokka, joka vastaa hakuehtoja vastaavien lankojen listaamisesta"""
    def __init__(self, root, yarns):
        """Luokan konstruktori, joka luo uuden listaus-näkymän.
        
        Args:
            root: Tkinter-elementti, johon näkymä alustetaan.
            yarns: Lista Yarn-olioita, jotka vastaavat hakuehtoja.
        """
        self._root = root
        self._yarns = yarns
        self._frame = None

        self._initialize()

    def pack(self):
        """Näyttää näkymän."""
        self._frame.pack(fill="x")

    def destroy(self):
        """Tuhoaa näkymän."""
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        if self._yarns == []:
            no_results_label = ttk.Label(master=self._frame, text="Ei hakutuloksia")
            no_results_label.grid(padx=5, pady=5)
        else:
            for yarn in self._yarns:
                self._initialize_yarn(yarn)

    def _initialize_yarn(self, yarn):
        yarn_frame = ttk.Frame(master=self._frame)

        name_label = ttk.Label(master=yarn_frame, text=yarn.name)
        colour_label = ttk.Label(master=yarn_frame, text=yarn.colour)
        weight_label = ttk.Label(master=yarn_frame, text=f'{yarn.weight} g')
        meters_label = ttk.Label(master=yarn_frame, text=f'{yarn.meters} m')
        type_label = ttk.Label(master=yarn_frame, text=yarn.yarn_type)

        for i in range(6):
            yarn_frame.columnconfigure(i, weight=1)

        name_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.E)
        colour_label.grid(row=0, column=1, padx=5, pady=5, sticky=constants.E)
        weight_label.grid(row=0, column=2, padx=5, pady=5, sticky=constants.E)
        meters_label.grid(row=0, column=3, padx=5, pady=5, sticky=constants.E)
        type_label.grid(row=0, column=4, padx=5, pady=5, sticky=constants.E)

        yarn_frame.pack(fill='x')

class SearchYarnsView:
    """Luokka, joka vastaa lankojen haku -näkymästä"""
    def __init__(self, root, handle_show_main_view):
        """Luokan konstruktori, joka luo uuden lankojen haku -näkymän
        
        Args:
            root: Tkinter-elementti, johon näkymä alustetaan.
            handle_show_main_view: Arvo, jota kutsutaan, kun palataan päävalikkoon.
        """
        self._root = root
        self._handle_show_main_view = handle_show_main_view
        self._frame = None
        self._search_fields_frame = None
        self._meters_entry = None
        self._yarn_type_cb = None
        self._yarn_list_view = None
        self._yarn_list_frame = None
        self._results_frame = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def destroy(self):
        """Tuhoaa näkymän."""
        self._frame.destroy()

    def pack(self):
        """Näyttää näkymän."""
        self._frame.pack(fill="both")

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)
        self._error_label = ttk.Label(master=self._frame, textvariable=self._error_variable)
        self._error_label.grid(padx=5, pady=5)

        main_view_button = ttk.Button(master=self._frame, text="Takaisin", command=self._handle_show_main_view)
        main_view_button.grid(padx=5, pady=5)

        self._search_fields_frame = ttk.Frame(master=self._frame)
        self._search_fields_frame.grid(padx=5, pady=5)

        empty_fields_button = ttk.Button(master=self._frame, text="Tyhjennä", command=self._initialize_search_fields)
        empty_fields_button.grid(row=3, padx=5, pady=5)

        self._initialize_search_fields()

        self._hide_error()
        
    def _initialize_results(self):
        search_results_label = ttk.Label(master=self._results_frame, text="Hakutulokset:")
        search_results_label.grid(padx=5, pady=5)

    def _initialize_search_fields(self):
        meters_label = ttk.Label(master=self._search_fields_frame, text="Metrimäärä:")
        self._meters_entry = ttk.Entry(master=self._search_fields_frame)
        
        yarn_types = ["kaikki", "lace", "fingering", "sport", "dk", "aran/worsted", "bulky"]
        yarn_type_label = ttk.Label(master=self._search_fields_frame, text="Langan vahvuus")
        self._yarn_type_cb = ttk.Combobox(master=self._search_fields_frame, values=yarn_types)
        self._yarn_type_cb.set("valitse vahvuus")
        search_button = ttk.Button(master=self._search_fields_frame, text="Hae", command=self._handle_search)

        meters_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)
        self._meters_entry.grid(row=0, column=1, padx=5, pady=5, sticky=constants.W)
        yarn_type_label.grid(row=1, padx=5, pady=5, sticky=constants.W)
        self._yarn_type_cb.grid(row=1, column=1, padx=5, pady=5, sticky=constants.W)
        search_button.grid(row=2, columnspan=2, padx=5, pady=5)

    def _handle_search(self):
        if self._results_frame:
            self._results_frame.destroy()
        if self._yarn_list_frame:
            self._yarn_list_frame.destroy()

        self._results_frame = ttk.Frame(master=self._frame)
        self._yarn_list_frame = ttk.Frame(master=self._frame)
        self._results_frame.grid(padx=5, pady=5)
        self._yarn_list_frame.grid(padx=5, pady=5)

        meters = self._meters_entry.get()
        yarn_type = self._yarn_type_cb.get()

        try:
            yarns = yarn_service.get_yarns_by_search(meters, yarn_type)
            self._hide_error()
            self._initialize_results()
            self._initialize_yarns(yarns)
        except InvalidInputError:
            self._show_error("Virheellinen syöte")
    
    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()
    
    def _initialize_yarns(self, yarns):
        if self._yarn_list_view:
            self._yarn_list_view.destroy()
        
        self._yarn_list_view = YarnListView(self._yarn_list_frame, yarns)

        self._yarn_list_view.pack()
