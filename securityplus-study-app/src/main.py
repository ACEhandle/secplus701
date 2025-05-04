from tkinter import Tk
from ui.main_window import MainWindow

def main():
    root = Tk()
    root.title("Security Plus Study App")
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()