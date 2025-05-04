# SecurityPlus Study App

A modern, cross-platform desktop application for studying CompTIA Security+ (SY0-701) exam objectives. Built with Python and [customtkinter](https://github.com/TomSchimansky/CustomTkinter) for a sleek, user-friendly experience. Easily adaptable for other certifications (e.g., CCNA, DevNet) by swapping out data files.

## Features

- **Practice Tests:**
  - Take module-based or full exam practice tests.
  - ABCD-style radio button answer selection.
  - Pass questions to revisit later; review passed questions in a focused mode.
  - Progress bar and counters for answered and passed questions.
  - Results with detailed explanations.

- **Knowledge Modules:**
  - Browse exam domains/modules and their descriptions.

- **Glossary:**
  - Searchable glossary of key terms and definitions.

- **Flashcards:**
  - Randomized flashcard mode for rapid review of glossary terms.

- **Modern UI:**
  - Built with customtkinter for a dark/light mode toggle, rounded corners, and a clean layout.
  - Responsive design with side-by-side buttons and compact answer areas.

## Usage

1. **Install requirements:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the app:**
   ```bash
   python src/main.py
   ```

3. **Navigate the app:**
   - Use the main menu to access Practice Tests, Knowledge Modules, Glossary, or Flashcards.
   - Toggle light/dark mode with the switch in the top right.

## Adapting for Other Certifications

To use this app for another certification (e.g., CCNA, DevNet):

1. **Create new data files** in `src/data/`:
   - `questions_<cert>.json` — All practice questions for the new cert.
   - `modules_<cert>.json` — Module/domain descriptions for the new cert.
   - `glossary_<cert>.json` — Glossary terms for the new cert.

2. **Update the code** to reference the new data files (or add a selector for multiple certifications).

3. **(Optional) Customize UI labels** to reflect the new certification.

## File Structure

```
securityplus-study-app/
├── README.md
├── requirements.txt
└── src/
    ├── main.py
    ├── data/
    │   ├── questions_secplus.json
    │   ├── modules_secplus.json
    │   └── glossary_secplus.json
    ├── modules/
    │   ├── practice_tests.py
    │   ├── knowledge_modules.py
    │   └── glossary.py
    └── ui/
        ├── main_window.py
        ├── practice_test_view.py
        ├── knowledge_module_view.py
        ├── glossary_view.py
        └── flashcards_view.py
```

## Requirements
- Python 3.8+
- customtkinter

Install dependencies with:
```
pip install -r requirements.txt
```

## License
MIT License

---

*This app is not affiliated with CompTIA or any certification body. For educational use only.*