from tkinter import ttk, StringVar, constants
from services.yarn_service import yarn_service, EmptyInputError, InvalidInputError, InputZeroError, InvalidYarnTypeError

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
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _initialize_entry_fields(self):
        heading_label = ttk.Label(master=self._entry_fields_frame, text="Lisää lanka varastoon:")

        name_label = ttk.Label(master=self._entry_fields_frame, text="Lanka")
        self._name_entry = ttk.Entry(master=self._entry_fields_frame)

        colour_label = ttk.Label(master=self._entry_fields_frame, text="Väri")
        self._colour_entry = ttk.Entry(master=self._entry_fields_frame)

        weight_label = ttk.Label(master=self._entry_fields_frame, text="Määrä")
        self._weight_entry = ttk.Entry(master=self._entry_fields_frame)
        grams1_label = ttk.Label(master=self._entry_fields_frame, text="grammaa")


        skein_size_label = ttk.Label(master=self._entry_fields_frame, text="Juoksevuus")
        meters_label = ttk.Label(master=self._entry_fields_frame, text="metriä/")
        grams2_label = ttk.Label(master=self._entry_fields_frame, text="grammaa")
        self._meters_entry = ttk.Entry(master=self._entry_fields_frame)
        self._grams_entry = ttk.Entry(master=self._entry_fields_frame)

        yarn_types = yarn_service.get_yarn_types()
        yarn_type_label = ttk.Label(master=self._entry_fields_frame, text="Langan vahvuus")
        self._yarn_type_cb = ttk.Combobox(master=self._entry_fields_frame, values=yarn_types)
        self._yarn_type_cb.set(yarn_types[0])

        add_yarn_button = ttk.Button(master=self._entry_fields_frame,
                                     text="Lisää varastoon",
                                     command=self._handle_add_yarn)

        heading_label.grid(row=0, columnspan=2, sticky=constants.W)

        name_label.grid(row=1, padx=5, pady=5, sticky=constants.W)
        self._name_entry.grid(row=1, column=1, columnspan=3, sticky=(constants.E, constants.W))

        colour_label.grid(row=2, padx=5, pady=5, sticky=constants.W)
        self._colour_entry.grid(row=2, column=1, columnspan=3, sticky=(constants.E, constants.W))

        weight_label.grid(row=3, padx=5, pady=5, sticky=constants.W)
        self._weight_entry.grid(row=3, column=1, columnspan=3, sticky=(constants.E, constants.W))
        grams1_label.grid(row=3, column=4, padx=(5, 0))

        skein_size_label.grid(row=4, padx=5, pady=5, sticky=constants.W)

        self._meters_entry.grid(row=4, column=1, sticky=(constants.E, constants.W))
        meters_label.grid(row=4, column=2, padx=(5, 0))

        self._grams_entry.grid(row=4, column=3, sticky=(constants.E, constants.W))
        grams2_label.grid(row=4, column=4, padx=(5, 0))

        yarn_type_label.grid(row=5, padx=5, pady=5, sticky=constants.W)
        self._yarn_type_cb.grid(row=5, column=1, columnspan=3, sticky=(constants.E, constants.W))

        add_yarn_button.grid(row=6,column=1, columnspan=3, pady=(10, 0))

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
        except InputZeroError:
            self._show_message("Gramma- ja metrimäärät eivät voi olla 0")
        except InvalidYarnTypeError:
            self._show_message("Valitse langan vahvuus listasta")

    def _show_message(self, message):
        self._message_variable.set(message)
        self._message_label.grid()
        self._message_label.after(3000, self._hide_message)

    def _hide_message(self):
        self._message_label.grid_remove()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._frame.columnconfigure(0, weight=1)

        self._message_variable = StringVar(self._frame)
        self._message_label = ttk.Label(master=self._frame, textvariable=self._message_variable)
        self._message_label.grid(padx=5, pady=5)

        main_view_button = ttk.Button(master=self._frame,
                                      text="Takaisin",
                                      command=self._handle_show_main_view)

        main_view_button.grid(column=0, padx=5, pady=5, sticky=constants.W)

        self._entry_fields_frame = ttk.Frame(master=self._frame)
        self._entry_fields_frame.grid(padx=5, pady=5, sticky=(constants.E, constants.W, constants.N, constants.S))
        self._entry_fields_frame.columnconfigure(1, weight=1)
        self._entry_fields_frame.columnconfigure(3, weight=1)

        self._initialize_entry_fields()

        self._hide_message()
