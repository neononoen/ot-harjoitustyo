from tkinter import ttk, StringVar, constants
from services.yarn_service import yarn_service, EmptyInputError, InvalidInputError

class AddYarnView:
    """"Luokka, joka vastaa langan lisäys -näkymästä."""
    def __init__(self, root, handle_show_main_view):
        """Luokan konstruktori, joka luo uuden langan lisäys -näkymän.
        
        Args:
            root: Tkinter-elementti, johon näkymä alustetaan.
            handle_show_main_view: Arvo, jota kutsutaan, kun palataan takaisin sovelluksen päävalikkoon.
        """
        self._root = root
        self._handle_show_main_view = handle_show_main_view
        self._frame = None
        self._entry_fields_frame = None
        self._name_entry = None
        self._colour_entry = None
        self._weight_entry = None
        self._grams_entry = None
        self._meters_entry = None
        self._yarn_type_cb = None
        self._message_label = None
        self._message_variable = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_entry_fields(self):
        heading_label = ttk.Label(master=self._entry_fields_frame, text="Lisää lanka varastoon:")

        name_label = ttk.Label(master=self._entry_fields_frame, text="Lanka")
        self._name_entry = ttk.Entry(master=self._entry_fields_frame)

        colour_label = ttk.Label(master=self._entry_fields_frame, text="Väri")
        self._colour_entry = ttk.Entry(master=self._entry_fields_frame)

        weight_label = ttk.Label(master=self._entry_fields_frame, text="Määrä (grammoina)")
        self._weight_entry = ttk.Entry(master=self._entry_fields_frame)

        skein_size_label = ttk.Label(master=self._entry_fields_frame, text="Juoksevuus (keräkoko)")
        meters_label = ttk.Label(master=self._entry_fields_frame, text="metriä")
        grams_label = ttk.Label(master=self._entry_fields_frame, text="grammaa")
        self._meters_entry = ttk.Entry(master=self._entry_fields_frame)
        self._grams_entry = ttk.Entry(master=self._entry_fields_frame)

        yarn_types = ["lace", "fingering", "sport", "dk", "aran/worsted", "bulky"]
        yarn_type_label = ttk.Label(master=self._entry_fields_frame, text="Langan vahvuus")
        self._yarn_type_cb = ttk.Combobox(master=self._entry_fields_frame, values=yarn_types)
        self._yarn_type_cb.set("valitse vahvuus")

        add_yarn_button = ttk.Button(master=self._entry_fields_frame, text="Lisää varastoon", command=self._handle_add_yarn)

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

        yarn_type_label.grid(row=6, column=0)
        self._yarn_type_cb.grid(row=6, column=1)

        add_yarn_button.grid(row=7, column=0, columnspan=2)

    def _handle_add_yarn(self):
        name = self._name_entry.get()
        colour = self._colour_entry.get()
        weight = self._weight_entry.get()
        meters = self._meters_entry.get()
        grams = self._grams_entry.get()
        yarn_type = self._yarn_type_cb.get()

        try:
            yarn_service.add_yarn(name, colour, weight, meters, grams, yarn_type)
            self._show_message(f"Lanka {name} lisätty!")
            self._initialize_entry_fields()
        except EmptyInputError:
            self._show_message("Tarkista, että kaikki kentät on täytetty")
        except InvalidInputError:
            self._show_message("Gramma- ja metrimäärien tulee olla numeroita!")

    def _show_message(self, message):
        self._message_variable.set(message)
        self._message_label.grid()
        self._message_label.after(3000, self._hide_message)

    def _hide_message(self):
        self._message_label.grid_remove()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._message_variable = StringVar(self._frame)
        self._message_label = ttk.Label(master=self._frame, textvariable=self._message_variable)
        self._message_label.grid(padx=5, pady=5)

        self._entry_fields_frame = ttk.Frame(master=self._frame)
        self._entry_fields_frame.grid(padx=5, pady=5)

        self._initialize_entry_fields()

        main_view_button = ttk.Button(master=self._frame, text="Takaisin",
                                       command=self._handle_show_main_view)
        main_view_button.grid(column=0, padx=5, pady=5)

        self._hide_message()
