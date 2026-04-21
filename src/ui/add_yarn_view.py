from tkinter import ttk
from services.yarn_service import yarn_service

class AddYarnView:
    def __init__(self, root, handle_show_main_view):
        self._root = root
        self._handle_show_main_view = handle_show_main_view
        self._frame = None
        self._name_entry = None
        self._colour_entry = None
        self._weight_entry = None
        self._grams_entry = None
        self._meters_entry = None
        self._type_cb = None

        self._initialize()

    def destroy(self):
        self._frame.destroy()

    def _initialize_entry_fields(self):
        heading_label = ttk.Label(master=self._frame, text="Lisää lanka varastoon:")

        name_label = ttk.Label(master=self._frame, text="Lanka")
        self._name_entry = ttk.Entry(master=self._frame)

        colour_label = ttk.Label(master=self._frame, text="Väri")
        self._colour_entry = ttk.Entry(master=self._frame)

        weight_label = ttk.Label(master=self._frame, text="Määrä (grammoina)")
        self._weight_entry = ttk.Entry(master=self._frame)

        skein_size_label = ttk.Label(master=self._frame, text="Juoksevuus (keräkoko)")
        meters_label = ttk.Label(master=self._frame, text="metriä")
        grams_label = ttk.Label(master=self._frame, text="grammaa")
        self._meters_entry = ttk.Entry(master=self._frame)
        self._grams_entry = ttk.Entry(master=self._frame)

        yarn_types = ["-", "lace", "fingering", "sport", "dk", "aran/worsted", "bulky"]
        type_label = ttk.Label(master=self._frame, text="Langan vahvuus")
        self._type_cb = ttk.Combobox(master=self._frame, values=yarn_types)
        self._type_cb.set("valitse vahvuus")

        add_yarn_button = ttk.Button(master=self._frame, text="Lisää varastoon", command=self._handle_add_yarn)

        heading_label.grid(row=0, column=0, columnspan=2)

        name_label.grid(row=1, column=0)
        self._name_entry.grid(row=1, column=1)

        colour_label.grid(row=2, column=0)
        self._colour_entry.grid(row=2, column=1)

        weight_label.grid(row=3, column=0)
        self._weight_entry.grid(row=3, column=1)

        skein_size_label.grid(row=4, column=0)
        self._meters_entry.grid(row=4, column=1)
        meters_label.grid(row=4, column=3)
        self._grams_entry.grid(row=5, column=1)
        grams_label.grid(row=5, column=3)

        type_label.grid(row=6, column=0)
        self._type_cb.grid(row=6, column=1)

        add_yarn_button.grid(row=7, column=0, columnspan=2)

    def _handle_add_yarn(self):
        name = self._name_entry.get()
        colour = self._colour_entry.get()
        weight = self._weight_entry.get()
        meters = self._meters_entry.get()
        grams = self._grams_entry.get()
        type = self._type_cb.get()

        meters_total = (int(weight)/int(grams))*int(meters)

        yarn_service.add_yarn(name, colour, int(weight), int(meters_total), type)

        self._initialize_entry_fields()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._initialize_entry_fields()

        main_view_button = ttk.Button(master=self._frame, text="Takaisin", command=self._handle_show_main_view)
        main_view_button.grid(row=8, column=0, columnspan=2)

        self._frame.pack()
