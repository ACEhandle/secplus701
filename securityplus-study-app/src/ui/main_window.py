from tkinter import Tk, Frame, Button, Label, StringVar
from ui.practice_test_view import PracticeTestView
from ui.knowledge_module_view import KnowledgeModuleView
from ui.glossary_view import GlossaryView

class MainWindow:
    def __init__(self, master):
        self.master = master
        master.title("Security Plus Study App")
        master.configure(bg="#222222")
        master.geometry("800x600")  # Set a wider default window size
        self.current_view = None

        self.label = Label(master, text="Welcome to the Security Plus Study App", bg="#222222", fg="#f0f0f0")
        self.label.pack()

        self.practice_test_button = Button(master, text="Practice Tests", command=self.open_practice_tests, bg="#333333", fg="#f0f0f0", activebackground="#444444", activeforeground="#ffffff")
        self.practice_test_button.pack()

        self.knowledge_modules_button = Button(master, text="Knowledge Modules", command=self.open_knowledge_modules, bg="#333333", fg="#f0f0f0", activebackground="#444444", activeforeground="#ffffff")
        self.knowledge_modules_button.pack()

        self.glossary_button = Button(master, text="Glossary", command=self.open_glossary, bg="#333333", fg="#f0f0f0", activebackground="#444444", activeforeground="#ffffff")
        self.glossary_button.pack()

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

if __name__ == "__main__":
    root = Tk()
    main_window = MainWindow(root)
    root.mainloop()