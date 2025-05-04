from tkinter import Tk, Frame, Button, Label, StringVar

class MainWindow:
    def __init__(self, master):
        self.master = master
        master.title("Security Plus Study App")
        master.configure(bg="#222222")

        self.label = Label(master, text="Welcome to the Security Plus Study App", bg="#222222", fg="#f0f0f0")
        self.label.pack()

        self.practice_test_button = Button(master, text="Practice Tests", command=self.open_practice_tests, bg="#333333", fg="#f0f0f0", activebackground="#444444", activeforeground="#ffffff")
        self.practice_test_button.pack()

        self.knowledge_modules_button = Button(master, text="Knowledge Modules", command=self.open_knowledge_modules, bg="#333333", fg="#f0f0f0", activebackground="#444444", activeforeground="#ffffff")
        self.knowledge_modules_button.pack()

        self.glossary_button = Button(master, text="Glossary", command=self.open_glossary, bg="#333333", fg="#f0f0f0", activebackground="#444444", activeforeground="#ffffff")
        self.glossary_button.pack()

    def open_practice_tests(self):
        # Logic to open practice tests view
        pass

    def open_knowledge_modules(self):
        # Logic to open knowledge modules view
        pass

    def open_glossary(self):
        # Logic to open glossary view
        pass

if __name__ == "__main__":
    root = Tk()
    main_window = MainWindow(root)
    root.mainloop()