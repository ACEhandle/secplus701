from tkinter import Frame, Label, Text, Scrollbar, VERTICAL, RIGHT, Y
import json
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

class KnowledgeModuleView(Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="#222222")
        self.master = master
        self.create_widgets()
        self.load_knowledge_modules()

    def create_widgets(self):
        self.title_label = Label(self, text="Knowledge Module", font=("Helvetica", 16), bg="#222222", fg="#f0f0f0")
        self.title_label.pack(pady=10)

        self.scrollbar = Scrollbar(self, orient=VERTICAL, bg="#222222", troughcolor="#333333", activebackground="#444444")
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.text_area = Text(self, wrap='word', yscrollcommand=self.scrollbar.set, bg="#333333", fg="#f0f0f0", insertbackground="#f0f0f0")
        self.text_area.pack(expand=True, fill='both')
        self.scrollbar.config(command=self.text_area.yview)

    def load_knowledge_modules(self):
        with open(os.path.join(DATA_DIR, 'modules.json'), 'r') as file:
            modules = json.load(file)
            for module in modules:
                self.text_area.insert('end', f"{module['title']}\n{module['content']}\n\n")
        self.text_area.config(state='disabled')  # Make text area read-only

    def run(self):
        self.pack()