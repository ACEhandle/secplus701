import customtkinter as ctk
import json
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

class KnowledgeModuleView(ctk.CTkFrame):
    def __init__(self, master=None, app_font=None):
        super().__init__(master)
        self.master = master
        self.app_font = app_font or ctk.CTkFont(size=16)
        self.create_widgets()
        self.load_knowledge_modules()

    def create_widgets(self):
        self.title_label = ctk.CTkLabel(self, text="Knowledge Module", font=self.app_font)
        self.title_label.pack(pady=10)

        self.text_area = ctk.CTkTextbox(self, wrap='word', width=700, height=400, font=self.app_font)
        self.text_area.pack(expand=True, fill='both')

    def load_knowledge_modules(self):
        with open(os.path.join(DATA_DIR, 'modules_secplus.json'), 'r') as file:
            modules = json.load(file)
            for module in modules['modules']:
                self.text_area.insert('end', f"{module['title']}\n{module['description']}\n\n")
        self.text_area.configure(state='disabled')  # Make text area read-only

    def run(self):
        self.pack()