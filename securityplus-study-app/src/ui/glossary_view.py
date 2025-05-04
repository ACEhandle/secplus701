from tkinter import Frame, Label, Listbox, Scrollbar, StringVar, Tk, END
import json
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

class GlossaryView(Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="#222222")
        self.master = master
        self.pack()
        self.create_widgets()
        self.load_glossary()

    def create_widgets(self):
        self.title_label = Label(self, text="Glossary of Terms", font=("Helvetica", 16), bg="#222222", fg="#f0f0f0")
        self.title_label.pack(pady=10)

        self.scrollbar = Scrollbar(self, bg="#222222", troughcolor="#333333", activebackground="#444444")
        self.scrollbar.pack(side="right", fill="y")

        self.glossary_list = Listbox(self, yscrollcommand=self.scrollbar.set, width=50, height=20, bg="#333333", fg="#f0f0f0", selectbackground="#444444", selectforeground="#ffffff")
        self.glossary_list.pack(padx=10, pady=10)
        self.glossary_list.bind('<<ListboxSelect>>', self.show_definition)

        self.scrollbar.config(command=self.glossary_list.yview)

        self.definition_label = Label(self, text="", wraplength=400, justify="left", bg="#222222", fg="#f0f0f0")
        self.definition_label.pack(pady=10)

    def load_glossary(self):
        with open(os.path.join(DATA_DIR, 'glossary.json'), 'r') as file:
            glossary_data = json.load(file)
            for term in glossary_data:
                self.glossary_list.insert(END, term)

    def show_definition(self, event):
        selected_term = self.glossary_list.get(self.glossary_list.curselection())
        with open(os.path.join(DATA_DIR, 'glossary.json'), 'r') as file:
            glossary_data = json.load(file)
            definition = glossary_data[selected_term]
            self.definition_label.config(text=definition)