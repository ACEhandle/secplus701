import customtkinter as ctk
from ui.main_window import MainWindow

def main():
    ctk.set_appearance_mode("dark")  # Set dark mode before creating the window
    ctk.set_default_color_theme("blue")
    root = ctk.CTk()  # Use customtkinter's CTk for rounded corners and modern look
    root.title("Security Plus Study App")
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()