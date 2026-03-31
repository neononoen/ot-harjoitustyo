from tkinter import ttk
from services.yarn_service import yarn_service

class UI:
    def __init__(self, root):
        self._root = root
        self._name_entry = None
        self._colour_entry = None
        self._weight_entry = None
        self._meters_entry = None
        self._type_entry = None

    def add_yarn(self):
        heading_label = ttk.Label(master=self._root, text="Lisää lanka varastoon:")
        
        name_label = ttk.Label(master=self._root, text="Lanka")
        self._name_entry = ttk.Entry(master=self._root)
        
        colour_label = ttk.Label(master=self._root, text="Väri")
        self._colour_entry = ttk.Entry(master=self._root)

        weight_label = ttk.Label(master=self._root, text="Määrä (grammoina)")
        self._weight_entry = ttk.Entry(master=self._root)

        meters_label = ttk.Label(master=self._root, text="Metrimäärä")
        self._meters_entry = ttk.Entry(master=self._root)

        type_label = ttk.Label(master=self._root, text="Langan vahvuus")
        self._type_entry = ttk.Entry(master=self._root)

        button = ttk.Button(master=self._root, text="Lisää varastoon", command=self._add_yarn_handler)

        heading_label.grid(row=0, column=0, columnspan=2)

        name_label.grid(row=1, column=0)
        self._name_entry.grid(row=1, column=1)

        colour_label.grid(row=2, column=0)
        self._colour_entry.grid(row=2, column=1)

        weight_label.grid(row=3, column=0)
        self._weight_entry.grid(row=3, column=1)

        meters_label.grid(row=4, column=0)
        self._meters_entry.grid(row=4, column=1)

        type_label.grid(row=5, column=0)
        self._type_entry.grid(row=5, column=1)

        button.grid(row=6, column=0, columnspan=2)

    def _add_yarn_handler(self):
        name = self._name_entry.get()
        colour = self._colour_entry.get()
        weight = self._weight_entry.get()
        meters = self._meters_entry.get()
        type = self._type_entry.get()

        yarn_service.add_yarn(name, colour, int(weight), int(meters), type)
        print(f"{name} lisätty varastoon")


