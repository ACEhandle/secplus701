class Glossary:
    def __init__(self, json_file):
        self.json_file = json_file
        self.terms = {}
        self.load_terms()

    def load_terms(self):
        import json
        with open(self.json_file, 'r') as file:
            self.terms = json.load(file)

    def get_definition(self, term):
        return self.terms.get(term, "Definition not found.")