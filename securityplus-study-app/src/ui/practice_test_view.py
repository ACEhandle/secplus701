import os
import customtkinter as ctk
from modules.practice_tests import PracticeTests

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

class PracticeTestView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        questions_path = os.path.join(DATA_DIR, "questions_secplus.json")
        self.practice_tests = PracticeTests(questions_path)
        self.current_question_index = 0
        self.user_answers = []
        self.questions = []
        self.test_type = ctk.StringVar()
        self.selection_var = ctk.StringVar()
        self.selection_var.set("")
        self.passed_questions = []
        self.setup_selection_screen()

    def setup_selection_screen(self):
        for widget in self.winfo_children():
            widget.destroy()
        ctk.CTkLabel(self, text="Select Practice Test Type").pack(pady=10)
        self.test_type.set("Module")
        ctk.CTkOptionMenu(self, variable=self.test_type, values=["Module", "Full Exam"]).pack(pady=5)
        self.option_menu = None
        self.update_selection_options()
        ctk.CTkButton(self, text="Start Test", command=self.start_test).pack(pady=10)
        self.test_type.trace('w', lambda *args: self.update_selection_options())

    def update_selection_options(self):
        if self.option_menu:
            self.option_menu.destroy()
        if self.test_type.get() == "Module":
            options = self.practice_tests.get_available_modules()
            if options:
                self.selection_var.set(options[0])
                self.option_menu = ctk.CTkOptionMenu(self, variable=self.selection_var, values=options)
                self.option_menu.pack(pady=5)
            else:
                self.selection_var.set("")
                self.option_menu = None
        else:
            self.selection_var.set("")
            self.option_menu = None

    def start_test(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.current_question_index = 0
        self.user_answers = []
        self.passed_questions = []
        if self.test_type.get() == "Module":
            self.questions = self.practice_tests.load_module_questions(self.selection_var.get())
        else:
            self.questions = self.practice_tests.load_full_exam()
        if not self.questions:
            self.show_error("Error", "No questions found for this selection.")
            self.setup_selection_screen()
            return
        self.setup_test_ui()
        self.load_question()

    def setup_test_ui(self):
        self.question_label = ctk.CTkLabel(self, text="", wraplength=700)
        self.question_label.pack(pady=(10, 5))  # Reduce vertical padding
        # Frame for answer options
        self.options_frame = ctk.CTkFrame(self)
        self.options_frame.pack(pady=(0, 5), fill='x', padx=20)  # Reduce vertical padding
        self.selected_option = ctk.StringVar()
        button_frame = ctk.CTkFrame(self)
        button_frame.pack(pady=(0, 5))  # Reduce vertical padding
        self.submit_button = ctk.CTkButton(button_frame, text="Submit Answer", command=self.submit_answer)
        self.submit_button.pack(side="left", padx=5)
        self.pass_button = ctk.CTkButton(button_frame, text="Pass", command=self.pass_question)
        self.pass_button.pack(side="left", padx=5)
        self.back_button = ctk.CTkButton(button_frame, text="Back", command=self.back_question)
        self.back_button.pack(side="left", padx=5)
        self.review_passed_button = ctk.CTkButton(button_frame, text="Review Passed", command=self.review_passed_questions)
        self.review_passed_button.pack(side="left", padx=5)
        self.result_button = ctk.CTkButton(button_frame, text="View Results", command=self.view_results)
        self.result_button.pack(side="left", padx=5)
        self.progress_bar = ctk.CTkProgressBar(self, width=600)
        self.progress_bar.pack(pady=(0, 2))  # Reduce vertical padding
        self.progress_label = ctk.CTkLabel(self, text="")
        self.progress_label.pack(pady=(0, 0))
        self.passed_label = ctk.CTkLabel(self, text="")
        self.passed_label.pack(pady=(0, 10))  # Reduce vertical padding
        self.update_progress_bar()

    def load_question(self):
        if self.current_question_index < len(self.questions):
            q = self.questions[self.current_question_index]
            self.question_label.configure(text=q['question'])
            # Remove old radio buttons
            for widget in self.options_frame.winfo_children():
                widget.destroy()
            # Shuffle and display options as radio buttons
            options = q['options'][:]
            import random
            random.shuffle(options)
            self.shuffled_options = options  # Store for answer checking
            self.selected_option.set("")
            abcd = ['A', 'B', 'C', 'D', 'E', 'F']
            for idx, answer in enumerate(options):
                ctk.CTkRadioButton(
                    self.options_frame,
                    text=f"{abcd[idx]}. {answer}",
                    variable=self.selected_option,
                    value=answer
                ).pack(anchor='w', pady=2)
            self.update_progress_bar()
        else:
            self.show_info("Info", "No more questions available.")

    def update_progress_bar(self):
        total = len(self.questions) if self.questions else 1
        # Only count questions that have a non-empty answer and are not in passed_questions
        answered = sum(1 for i, ans in enumerate(self.user_answers) if ans and i not in self.passed_questions)
        self.progress_bar.set(answered / total)
        self.progress_label.configure(text=f"{answered} / {total} answered")
        passed_count = len(self.passed_questions)
        self.passed_label.configure(text=f"{passed_count} passed question{'s' if passed_count != 1 else ''} to revisit")

    def submit_answer(self):
        selected_answer = self.selected_option.get()
        if selected_answer:
            if len(self.user_answers) <= self.current_question_index:
                self.user_answers.append(selected_answer)
            else:
                self.user_answers[self.current_question_index] = selected_answer
            # Remove from passed_questions if it was passed before
            if self.current_question_index in self.passed_questions:
                self.passed_questions.remove(self.current_question_index)
            self.next_question()
        else:
            self.show_warning("Warning", "Please select an answer.")

    def pass_question(self):
        if self.current_question_index not in self.passed_questions:
            self.passed_questions.append(self.current_question_index)
        self.update_progress_bar()
        self.next_question()

    def next_passed_question(self):
        # Go to the next passed question in the queue, or next unanswered if none
        if self.passed_questions:
            self.current_question_index = self.passed_questions[0]
            self.load_question()
        else:
            self.next_question()

    def back_question(self):
        if self.current_question_index > 0:
            self.current_question_index -= 1
            self.load_question()

    def review_passed_questions(self):
        if self.passed_questions:
            self.current_question_index = self.passed_questions[0]
            self.load_question()
        else:
            self.show_info("Info", "No passed questions to review.")

    def next_question(self):
        if self.current_question_index < len(self.questions) - 1:
            self.current_question_index += 1
            self.load_question()
        else:
            self.show_info("Info", "This is the last question.")

    def view_results(self):
        results = self.practice_tests.evaluate_answers(self.user_answers)
        self.show_detailed_results(results)

    def show_detailed_results(self, results):
        result_win = ctk.CTkToplevel(self.master)
        result_win.title("Test Results")
        result_win.transient(self.master)
        result_win.grab_set()
        ctk.CTkLabel(result_win, text=f"Score: {results['correct']} / {results['total']}", font=("Helvetica", 14)).pack(pady=10)
        for detail in results['details']:
            if not detail['is_correct']:
                ctk.CTkLabel(result_win, text=f"Q: {detail['question']}", text_color="#ff6666", wraplength=500, justify='left').pack(anchor='w', padx=10)
                ctk.CTkLabel(result_win, text=f"Your answer: {detail['user_answer']}", text_color="#ffcc00", wraplength=500, justify='left').pack(anchor='w', padx=20)
                ctk.CTkLabel(result_win, text=f"Correct answer: {detail['correct_answer']}", text_color="#66ff66", wraplength=500, justify='left').pack(anchor='w', padx=20)
                ctk.CTkLabel(result_win, text=f"Explanation: {detail['explanation']}", wraplength=500, justify='left').pack(anchor='w', padx=20, pady=(0,10))
        if all(d['is_correct'] for d in results['details']):
            ctk.CTkLabel(result_win, text="All answers correct!", text_color="#66ff66").pack(pady=10)
        ctk.CTkButton(result_win, text="Close", command=result_win.destroy).pack(pady=10)

    def show_info(self, title, message):
        info_win = ctk.CTkToplevel(self.master)
        info_win.title(title)
        info_win.transient(self.master)
        info_win.grab_set()
        ctk.CTkLabel(info_win, text=message, wraplength=400).pack(padx=20, pady=20)
        ctk.CTkButton(info_win, text="OK", command=info_win.destroy).pack(pady=10)

    def show_warning(self, title, message):
        warn_win = ctk.CTkToplevel(self.master)
        warn_win.title(title)
        warn_win.transient(self.master)
        warn_win.grab_set()
        ctk.CTkLabel(warn_win, text=message, wraplength=400, text_color="#ffcc00").pack(padx=20, pady=20)
        ctk.CTkButton(warn_win, text="OK", command=warn_win.destroy).pack(pady=10)

    def show_error(self, title, message):
        err_win = ctk.CTkToplevel(self.master)
        err_win.title(title)
        err_win.transient(self.master)
        err_win.grab_set()
        ctk.CTkLabel(err_win, text=message, wraplength=400, text_color="#ff6666").pack(padx=20, pady=20)
        ctk.CTkButton(err_win, text="OK", command=err_win.destroy).pack(pady=10)