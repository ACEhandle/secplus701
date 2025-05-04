import os
import json
import random
from tkinter import Frame, Label, Button, Toplevel

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

class FlashcardsView(Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="#222222")
        self.master = master
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
        self.term_label = Label(self, text="", font=("Helvetica", 20, "bold"), bg="#222222", fg="#f0f0f0", wraplength=600)
        self.term_label.pack(pady=40)
        self.definition_label = Label(self, text="", font=("Helvetica", 14), bg="#222222", fg="#f0f0f0", wraplength=600)
        self.definition_label.pack(pady=20)
        self.show_button = Button(self, text="Show Definition", command=self.show_definition, bg="#333333", fg="#f0f0f0")
        self.show_button.pack(pady=10)
        self.next_button = Button(self, text="Next", command=self.next_card, bg="#333333", fg="#f0f0f0")
        self.next_button.pack(pady=10)

    def next_card(self):
        self.showing_definition = False
        self.definition_label.config(text="")
        if not self.terms:
            self.term_label.config(text="No flashcards available.")
            return
        self.current_index = random.randint(0, len(self.terms) - 1)
        self.term_label.config(text=self.terms[self.current_index]['term'])
        self.show_button.config(state='normal')

    def show_definition(self):
        if self.current_index is not None and not self.showing_definition:
            self.definition_label.config(text=self.terms[self.current_index]['definition'])
            self.showing_definition = True
            self.show_button.config(state='disabled')
