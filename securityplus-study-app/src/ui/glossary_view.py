import customtkinter as ctk
import json
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

class GlossaryView(ctk.CTkFrame):
    def __init__(self, master=None, app_font=None):
        super().__init__(master)
        self.master = master
        self.app_font = app_font or ctk.CTkFont(size=16)
        self.pack(fill="both", expand=True)
        self.create_widgets()
        self.load_glossary()

    def create_widgets(self):
        self.title_label = ctk.CTkLabel(self, text="Glossary of Terms", font=ctk.CTkFont(size=18, weight="bold"))
        self.title_label.pack(pady=(10, 0))

        # Main frame for horizontal layout
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Scrollable frame for terms list
        self.scrollable_frame = ctk.CTkScrollableFrame(self.main_frame, width=250, height=400)
        self.scrollable_frame.pack(side="left", fill="y", expand=False, padx=(0, 10))

        # Frame for definition display
        self.definition_frame = ctk.CTkFrame(self.main_frame)
        self.definition_frame.pack(side="left", fill="both", expand=True)

        self.definition_label = ctk.CTkLabel(self.definition_frame, text="Select a term to view its definition.", wraplength=500, anchor="nw", justify="left", font=self.app_font)
        self.definition_label.pack(fill="both", expand=True, padx=10, pady=10)

        self.term_buttons = []

    def load_glossary(self):
        # Clear previous buttons if reloading
        for btn in getattr(self, 'term_buttons', []):
            btn.destroy()
        self.term_buttons = []

        with open(os.path.join(DATA_DIR, 'glossary_secplus.json'), 'r') as file:
            glossary_data = json.load(file)
            self.terms = glossary_data.get('terms', [])

        for entry in self.terms:
            btn = ctk.CTkButton(self.scrollable_frame, text=entry['term'], width=220, anchor="w", fg_color="transparent", hover_color="#444444", command=lambda e=entry: self.show_definition(e), font=self.app_font)
            btn.pack(fill="x", pady=2, padx=2, anchor="w")
            self.term_buttons.append(btn)

    def show_definition(self, entry):
        self.definition_label.configure(text=entry['definition'])