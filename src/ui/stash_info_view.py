from tkinter import ttk, constants
from services.yarn_service import yarn_service

class StashInfoView:
    def __init__(self, root, handle_show_main_view):
        self._root = root
        self._handle_show_main_view = handle_show_main_view
        self._frame = None
        self._total_weight_list_frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        main_view_button = ttk.Button(master=self._frame,
                                      text="Takaisin",
                                      command=self._handle_show_main_view)

        main_view_button.grid(column=0, padx=5, pady=5, sticky=constants.W)

        header_label = ttk.Label(master=self._frame, text="Varastotilanne")
        total_weight_label = ttk.Label(master=self._frame, text=f"Lankojen yhteispaino: {yarn_service.get_total_yarn_weight()} grammaa")
        total_meterage_label = ttk.Label(master=self._frame, text=f"Lankojen metrimäärä yhteensä: {yarn_service.get_total_yarn_meterage()} metriä")
        total_yarns_label = ttk.Label(master=self._frame, text=f"Erilaisten lankojen määrä: {yarn_service.get_number_of_yarns_in_stash()}")
        
        self._total_weight_list_frame = ttk.Frame(master=self._frame)
        yarn_types = yarn_service.get_total_weight_by_yarn_type()
        for yarn_type, total_weight in yarn_types.items():
            i = list(yarn_types).index(yarn_type)
            self._initialize_totals_by_yarn_type(yarn_type, total_weight, i)
            self._total_weight_list_frame.columnconfigure(i, weight=1)

        header_label.grid(row=0, columnspan=2, padx=5, pady=5, sticky=constants.N)
        total_weight_label.grid(row=1, padx=5, pady=5, sticky=constants.W)
        total_meterage_label.grid(row=2, padx=5, pady=5, sticky=constants.W)
        total_yarns_label.grid(row=3, padx=5, pady=5, sticky=constants.W)
        self._total_weight_list_frame.grid(row=4, padx=5, pady=5, sticky=(constants.E, constants.W))

    def _initialize_totals_by_yarn_type(self, yarn_type, total_weight, column):
        yarn_type_label = ttk.Label(master=self._total_weight_list_frame, text=f"{yarn_type}:")
        total_weight_label = ttk.Label(master=self._total_weight_list_frame, text=f"{total_weight} g")

        yarn_type_label.grid(row=0, column=column, padx=10, pady=5)
        total_weight_label.grid(row=1, column=column, padx=10, pady=5)
