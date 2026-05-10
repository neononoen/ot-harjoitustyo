from tkinter import ttk, constants, StringVar
from services.yarn_service import yarn_service, InvalidInputError, EmptyInputError, ZeroMetersError

class YarnsView:
    """Luokka, joka vastaa näkymästä, joka listaa kaikki langat."""
    def __init__(self, root, handle_show_main_view):
        """Luokan konstruktori, joka luo uuden lankojen listaus -näkymän.
        
        Args:
            root: Tkinter-elementti, johon näkymä alustetaan.
            handle_show_main_view: Arvo, jota kutsutaan, kun palataan päävalikkoon.
        """
        self._root = root
        self._handle_show_main_view = handle_show_main_view
        self._frame = None
        self._yarn_list_frame = None
        self._yarn_frame = None
        self._edit_frame = None
        self._edit_weight_entry = None
        self._message_variable = None
        self._message_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._frame.columnconfigure(0, weight=1)

        self._message_variable = StringVar(self._frame)
        self._message_label = ttk.Label(master=self._frame, textvariable=self._message_variable)
        self._message_label.grid(padx=5, pady=5)

        main_view_button = ttk.Button(master=self._frame, text="Takaisin",
                                       command=self._handle_show_main_view)
        main_view_button.grid(row=1, column=0, sticky=constants.W)

        self._initialize_yarns()

        self._hide_message()

    def _initialize_yarns(self):
        if self._yarn_list_frame:
            self._yarn_list_frame.destroy()

        self._yarn_list_frame = ttk.Frame(master=self._frame)
        self._yarn_list_frame.grid(row=2, column=0, padx=5, pady=5, sticky=(constants.E, constants.W))

        yarns = yarn_service.get_all_yarns()
        for yarn in yarns:
            self._initialize_yarn(yarn)

    def _initialize_yarn(self, yarn):
        self._yarn_frame = ttk.Frame(master=self._yarn_list_frame)

        name_label = ttk.Label(master=self._yarn_frame, text=yarn.name)
        colour_label = ttk.Label(master=self._yarn_frame, text=yarn.colour)
        weight_label = ttk.Label(master=self._yarn_frame, text=f"{yarn.weight} g")
        meters_label = ttk.Label(master=self._yarn_frame, text=f"{yarn.meters} m")
        yarn_type_label = ttk.Label(master=self._yarn_frame, text=yarn.yarn_type)
        delete_button = ttk.Button(master=self._yarn_frame, text="Poista",
                                    command=lambda: self._handle_remove_yarn(yarn.id))
        edit_button = ttk.Button(master=self._yarn_frame, text="Muokkaa",
                                  command=lambda: self._initialize_edit_entry(yarn.id))

        for i in range(6):
            self._yarn_frame.columnconfigure(i, weight=1)

        name_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)
        colour_label.grid(row=0, column=1, padx=5, pady=5, sticky=constants.W)
        weight_label.grid(row=0, column=2, padx=5, pady=5, sticky=constants.W)
        meters_label.grid(row=0, column=3, padx=5, pady=5, sticky=constants.W)
        yarn_type_label.grid(row=0, column=4, padx=5, pady=5, sticky=constants.W)
        delete_button.grid(row=0, column=5, padx=5, pady=5, sticky=constants.W)
        edit_button.grid(row=0, column=6, padx=5, pady=5, sticky=constants.W)

        self._yarn_frame.pack(fill=constants.X)

    def _handle_remove_yarn(self, yarn_id):
        yarn_service.delete_yarn(yarn_id)
        self._initialize_yarns()
        self._show_message("Lanka poistettu")

    def _initialize_edit_entry(self, yarn_id):
        if self._edit_frame:
            self._edit_frame.destroy()

        self._edit_frame = ttk.Frame(master=self._yarn_frame)
        self._edit_frame.grid(row=1, columnspan=6, padx=5, pady=5)

        edit_label = ttk.Label(master=self._edit_frame, text="Uusi määrä: ")
        self._edit_weight_entry = ttk.Entry(master=self._edit_frame)
        save_button = ttk.Button(master=self._edit_frame, text="Tallenna",
                                  command=lambda: self._handle_edit(yarn_id))
        grams_label = ttk.Label(master=self._edit_frame, text="grammaa")

        edit_label.grid(row=0, column=0, padx=5, pady=5)
        self._edit_weight_entry.grid(row=0, column=1, padx=5, pady=5)
        grams_label.grid(row=0, column=2, padx=5, pady=5)
        save_button.grid(row=0, column=3, padx=5, pady=5)

    def _handle_edit(self, yarn_id):
        meters = self._edit_weight_entry.get()
        try:
            yarn_service.change_yarn_total_weight(meters, yarn_id)
            self._initialize_yarns()
            self._show_message("Määrä päivitetty!")
        except InvalidInputError:
            self._show_message("Syötä määrä numeroina")
        except EmptyInputError:
            self._show_message("Syöte ei voi olla tyhjä")
        except ZeroMetersError:
            self._show_message("Muokkaaminen ei onnistunut, metrimäärä jää alle 1 metrin")

    def _show_message(self, message):
        self._message_variable.set(message)
        self._message_label.grid()
        self._message_label.after(3000, self._hide_message)

    def _hide_message(self):
        self._message_label.grid_remove()
