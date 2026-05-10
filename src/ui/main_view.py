from tkinter import ttk, constants

class MainView:
    """Luokka, joka vastaa sovelluksen päävalikko-näkymästä."""
    def __init__(self, root, handle_show_yarns_view, handle_show_add_yarn_view, handle_show_search_yarns_view, handle_show_stash_info_view):
        """Luokan konstruktori, joka luo uuden päävalikko-näkymän.
        
        Args:
            root: Tkinter-elementti, johon näkymä alustetaan.
            handle_show_yarns_view: Arvo, jota kutsutaan, kun siirrytään "Kaikki langat"-näkymään.
            handle_show_add_yarn_view: Arov, jota kutsutaan, kun siirrytään "Lisää lanka"-näkymään.
            handle_show_search_yarns_view: Arvo, jota kutsutaan, kun siirrytään "Hae lankoja"-näkymään.
        """
        self._root = root
        self._frame = None
        self._handle_show_yarns_view = handle_show_yarns_view
        self._handle_show_add_yarn_view = handle_show_add_yarn_view
        self._handle_show_search_yarns_view = handle_show_search_yarns_view
        self._handle_show_stash_info_view = handle_show_stash_info_view

        self._initialize()

    def destroy(self):
        """Tuhoaa näkymän."""
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        style = ttk.Style()
        style.configure("M.TLabel", font=("Courier New", 18, "bold"), foreground="#4A0010", background="#8BC935")
        style.configure("M.TButton", font=("Courier New", 16, "bold"), foreground="#4A0010", background="#F67390", borderwidth="5")

        self._frame.columnconfigure(0, weight=1)
        self._frame.rowconfigure(0, weight=1)
        self._frame.rowconfigure(1, weight=2)
        self._frame.rowconfigure(2, weight=2)
        self._frame.rowconfigure(3, weight=2)
        self._frame.rowconfigure(4, weight=2)

        header_label = ttk.Label(master=self._frame, text="Lankavarasto", style="M.TLabel", anchor=constants.CENTER)
        yarns_button = ttk.Button(master=self._frame, text="Kaikki langat", style="M.TButton", command=self._handle_show_yarns_view)
        add_yarn_button = ttk.Button(master=self._frame, text="Lisää lanka", style="M.TButton", command=self._handle_show_add_yarn_view)
        search_yarns_button = ttk.Button(master=self._frame, text="Hae lankoja", style="M.TButton", command=self._handle_show_search_yarns_view)
        stash_info_button = ttk.Button(master=self._frame, text="Varastotilanne", style="M.TButton", command=self._handle_show_stash_info_view)

        header_label.grid(row=0, column=0, sticky=constants.NSEW, padx=5, pady=5)
        yarns_button.grid(row=1, column=0, sticky=constants.NSEW, padx=5, pady=5)
        add_yarn_button.grid(row=2, column=0, sticky=constants.NSEW, padx=5, pady=5)
        search_yarns_button.grid(row=3, column=0, sticky=constants.NSEW, padx=5, pady=5)
        stash_info_button.grid(row=4, column=0, sticky=constants.NSEW, padx=5, pady=5)

        self._frame.pack(fill="both", expand=True)
