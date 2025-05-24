import os
import json
import random
import customtkinter as ctk

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

class FlashcardsView(ctk.CTkFrame):
    def __init__(self, master=None, app_font=None):
        super().__init__(master)
        self.master = master
        self.app_font = app_font or ctk.CTkFont(size=16)
        self.pack(fill='both', expand=True)
        self.terms = self.load_terms()
        self.current_index = None
        self.showing_definition = False
        self.create_widgets()
        self.next_card()

    def load_terms(self):
        with open(os.path.join(DATA_DIR, 'glossary_secplus.json'), 'r') as file:
            glossary_data = json.load(file)
            return glossary_data.get('terms', [])

    def create_widgets(self):
        self.term_label = ctk.CTkLabel(self, text="", font=ctk.CTkFont(size=20, weight="bold"), wraplength=600)
        self.term_label.pack(pady=40)
        self.definition_label = ctk.CTkLabel(self, text="", font=self.app_font, wraplength=600)
        self.definition_label.pack(pady=20)
        self.show_button = ctk.CTkButton(self, text="Show Definition", command=self.show_definition, font=self.app_font)
        self.show_button.pack(pady=10)
        self.next_button = ctk.CTkButton(self, text="Next", command=self.next_card, font=self.app_font)
        self.next_button.pack(pady=10)

    def next_card(self):
        self.showing_definition = False
        self.definition_label.configure(text="")
        if not self.terms:
            self.term_label.configure(text="No flashcards available.")
            return
        self.current_index = random.randint(0, len(self.terms) - 1)
        self.term_label.configure(text=self.terms[self.current_index]['term'])
        self.show_button.configure(state='normal')

    def show_definition(self):
        if self.current_index is not None and not self.showing_definition:
            self.definition_label.configure(text=self.terms[self.current_index]['definition'])
            self.showing_definition = True
            self.show_button.configure(state='disabled')
