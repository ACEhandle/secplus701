import customtkinter as ctk
import json
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

class GlossaryView(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.load_glossary()

    def create_widgets(self):
        self.title_label = ctk.CTkLabel(self, text="Glossary of Terms")
        self.title_label.pack(pady=10)

        self.glossary_list = ctk.CTkComboBox(self, width=300)
        self.glossary_list.pack(padx=10, pady=5)
        self.glossary_list.bind('<<ComboboxSelected>>', self.show_definition)

        self.definition_label = ctk.CTkLabel(self, text="", wraplength=500, anchor="w")
        self.definition_label.pack(pady=10, fill="x", padx=10)

    def load_glossary(self):
        with open(os.path.join(DATA_DIR, 'glossary_secplus.json'), 'r') as file:
            glossary_data = json.load(file)
            self.terms = glossary_data.get('terms', [])
            self.glossary_list.configure(values=[entry['term'] for entry in self.terms])

    def show_definition(self, event):
        if not hasattr(self, 'terms') or not self.terms:
            return
        selected = self.glossary_list.get()
        for entry in self.terms:
            if entry['term'] == selected:
                self.definition_label.configure(text=entry['definition'])
                break