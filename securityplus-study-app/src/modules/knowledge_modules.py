class KnowledgeModules:
    def __init__(self, json_file):
        self.json_file = json_file
        self.modules = self.load_modules()

    def load_modules(self):
        import json
        try:
            with open(self.json_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: The file {self.json_file} was not found.")
            return []
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON.")
            return []

    def get_module_info(self, module_name):
        for module in self.modules:
            if module['name'] == module_name:
                return module
        return None

    def list_modules(self):
        return [module['name'] for module in self.modules]