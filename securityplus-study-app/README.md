# Security Plus Study Application

This is a study application designed to help users prepare for the Security Plus Exam 701. The application includes practice tests, knowledge modules, and a glossary of terms to aid in studying.

## Features

- **Practice Tests**: Users can take practice tests that simulate the exam environment. The application loads questions from a JSON file and evaluates user answers.
  
- **Knowledge Modules**: The application provides detailed knowledge modules related to the Security Plus exam, allowing users to study specific topics.

- **Glossary**: A comprehensive glossary of terms is available, providing definitions and explanations for key concepts related to the exam.

## Project Structure

```
securityplus-study-app
├── src
│   ├── main.py
│   ├── modules
│   │   ├── practice_tests.py
│   │   ├── knowledge_modules.py
│   │   └── glossary.py
│   ├── ui
│   │   ├── main_window.py
│   │   ├── practice_test_view.py
│   │   ├── knowledge_module_view.py
│   │   └── glossary_view.py
│   └── data
│       ├── questions.json
│       ├── modules.json
│       └── glossary.json
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd securityplus-study-app
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

This will launch the Tkinter application, where you can navigate through the practice tests, knowledge modules, and glossary.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.