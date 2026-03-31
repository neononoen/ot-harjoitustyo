from tkinter import Tk
from ui.add_yarn_view import UI

def main():
    window = Tk()
    window.title("Lankavarasto")

    ui = UI(window)
    ui.add_yarn()

    window.mainloop()

if __name__ == "__main__":
    main()