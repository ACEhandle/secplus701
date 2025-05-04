import customtkinter as ctk
from ui.practice_test_view import PracticeTestView
from ui.knowledge_module_view import KnowledgeModuleView
from ui.glossary_view import GlossaryView
from ui.flashcards_view import FlashcardsView

class MainWindow:
    def __init__(self, master):
        self.master = master
        ctk.set_appearance_mode("dark")  # Default to dark mode
        ctk.set_default_color_theme("blue")
        self.current_mode = "dark"
        master.title("Security Plus Study App")
        master.geometry("800x600")
        self.current_view = None

        self.label = ctk.CTkLabel(master, text="Welcome to the Security Plus Study App")
        self.label.pack(pady=10)

        self.practice_test_button = ctk.CTkButton(master, text="Practice Tests", command=self.open_practice_tests)
        self.practice_test_button.pack(pady=5)

        self.knowledge_modules_button = ctk.CTkButton(master, text="Knowledge Modules", command=self.open_knowledge_modules)
        self.knowledge_modules_button.pack(pady=5)

        self.glossary_button = ctk.CTkButton(master, text="Glossary", command=self.open_glossary)
        self.glossary_button.pack(pady=5)

        self.flashcards_button = ctk.CTkButton(master, text="Flashcards", command=self.open_flashcards)
        self.flashcards_button.pack(pady=5)

        # Place the light/dark mode switch at the top right
        self.toggle_mode_switch = ctk.CTkSwitch(master, text="Light Mode", command=self.toggle_mode)
        self.toggle_mode_switch.select()  # Default to dark mode
        self.toggle_mode_switch.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)

    def clear_view(self):
        if self.current_view:
            self.current_view.pack_forget()
            self.current_view.destroy()
            self.current_view = None

    def open_practice_tests(self):
        self.clear_view()
        self.current_view = PracticeTestView(self.master)
        self.current_view.pack(fill='both', expand=True)

    def open_knowledge_modules(self):
        self.clear_view()
        self.current_view = KnowledgeModuleView(self.master)
        self.current_view.pack(fill='both', expand=True)

    def open_glossary(self):
        self.clear_view()
        self.current_view = GlossaryView(self.master)
        self.current_view.pack(fill='both', expand=True)

    def open_flashcards(self):
        self.clear_view()
        self.current_view = FlashcardsView(self.master)
        self.current_view.pack(fill='both', expand=True)

    def toggle_mode(self):
        if self.toggle_mode_switch.get():
            ctk.set_appearance_mode("dark")
            self.toggle_mode_switch.configure(text="Light Mode")
        else:
            ctk.set_appearance_mode("light")
            self.toggle_mode_switch.configure(text="Dark Mode")

if __name__ == "__main__":
    root = ctk.CTk()
    main_window = MainWindow(root)
    root.mainloop()