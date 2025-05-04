import os
from tkinter import Frame, Label, Button, Listbox, Scrollbar, messagebox, StringVar, OptionMenu, Toplevel
from modules.practice_tests import PracticeTests

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

class PracticeTestView(Frame):
    def __init__(self, master):
        super().__init__(master, bg="#222222")
        self.master = master
        questions_path = os.path.join(DATA_DIR, "questions.json")
        self.practice_tests = PracticeTests(questions_path)
        self.current_question_index = 0
        self.user_answers = []
        self.questions = []
        self.test_type = StringVar()
        self.selection_var = StringVar()
        self.selection_var.set("")
        self.passed_questions = []
        self.setup_selection_screen()

    def setup_selection_screen(self):
        for widget in self.winfo_children():
            widget.destroy()
        Label(self, text="Select Practice Test Type", bg="#222222", fg="#f0f0f0").pack(pady=10)
        self.test_type.set("Module")
        OptionMenu(self, self.test_type, "Module", "Full Exam").pack(pady=5)
        self.option_menu = None
        self.update_selection_options()
        Button(self, text="Start Test", command=self.start_test, bg="#333333", fg="#f0f0f0").pack(pady=10)
        self.test_type.trace('w', lambda *args: self.update_selection_options())

    def update_selection_options(self):
        if self.option_menu:
            self.option_menu.destroy()
        if self.test_type.get() == "Module":
            options = self.practice_tests.get_available_modules()
            if options:
                self.selection_var.set(options[0])
                self.option_menu = OptionMenu(self, self.selection_var, *options)
                self.option_menu.pack(pady=5)
            else:
                self.selection_var.set("")
                self.option_menu = None
        else:
            # For Full Exam, no selection needed
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
            messagebox.showerror("Error", "No questions found for this selection.")
            self.setup_selection_screen()
            return
        self.setup_test_ui()
        self.load_question()

    def setup_test_ui(self):
        self.question_label = Label(self, text="", wraplength=700, bg="#222222", fg="#f0f0f0")
        self.question_label.pack(pady=20)
        self.answer_listbox = Listbox(self, bg="#333333", fg="#f0f0f0", selectbackground="#444444", selectforeground="#ffffff", width=80)
        self.answer_listbox.pack(pady=10, fill='x', padx=20)
        self.submit_button = Button(self, text="Submit Answer", command=self.submit_answer, bg="#333333", fg="#f0f0f0", activebackground="#444444", activeforeground="#ffffff")
        self.submit_button.pack(pady=10)
        self.pass_button = Button(self, text="Pass", command=self.pass_question, bg="#333333", fg="#f0f0f0", activebackground="#444444", activeforeground="#ffffff")
        self.pass_button.pack(pady=10)
        self.back_button = Button(self, text="Back", command=self.back_question, bg="#333333", fg="#f0f0f0", activebackground="#444444", activeforeground="#ffffff")
        self.back_button.pack(pady=10)
        self.review_passed_button = Button(self, text="Review Passed", command=self.review_passed_questions, bg="#333333", fg="#f0f0f0", activebackground="#444444", activeforeground="#ffffff")
        self.review_passed_button.pack(pady=10)
        self.result_button = Button(self, text="View Results", command=self.view_results, bg="#333333", fg="#f0f0f0", activebackground="#444444", activeforeground="#ffffff")
        self.result_button.pack(pady=10)

    def load_question(self):
        if self.current_question_index < len(self.questions):
            q = self.questions[self.current_question_index]
            self.question_label.config(text=q['question'])
            self.answer_listbox.delete(0, 'end')
            # Shuffle options for each question display
            options = q['options'][:]
            import random
            random.shuffle(options)
            self.shuffled_options = options  # Store for answer checking
            for answer in options:
                self.answer_listbox.insert('end', answer)
        else:
            messagebox.showinfo("Info", "No more questions available.")

    def submit_answer(self):
        selected_answer_index = self.answer_listbox.curselection()
        if selected_answer_index:
            selected_answer = self.answer_listbox.get(selected_answer_index)
            if len(self.user_answers) <= self.current_question_index:
                self.user_answers.append(selected_answer)
            else:
                self.user_answers[self.current_question_index] = selected_answer
            self.next_question()
        else:
            messagebox.showwarning("Warning", "Please select an answer.")

    def pass_question(self):
        if self.current_question_index not in self.passed_questions:
            self.passed_questions.append(self.current_question_index)
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
            messagebox.showinfo("Info", "No passed questions to review.")

    def next_question(self):
        if self.current_question_index < len(self.questions) - 1:
            self.current_question_index += 1
            self.load_question()
        else:
            messagebox.showinfo("Info", "This is the last question.")

    def view_results(self):
        results = self.practice_tests.evaluate_answers(self.user_answers)
        self.show_detailed_results(results)

    def show_detailed_results(self, results):
        result_win = Toplevel(self.master)
        result_win.title("Test Results")
        result_win.configure(bg="#222222")
        result_win.transient(self.master)
        result_win.grab_set()
        Label(result_win, text=f"Score: {results['correct']} / {results['total']}", bg="#222222", fg="#f0f0f0", font=("Helvetica", 14)).pack(pady=10)
        for detail in results['details']:
            if not detail['is_correct']:
                Label(result_win, text=f"Q: {detail['question']}", bg="#222222", fg="#ff6666", wraplength=500, justify='left').pack(anchor='w', padx=10)
                Label(result_win, text=f"Your answer: {detail['user_answer']}", bg="#222222", fg="#ffcc00", wraplength=500, justify='left').pack(anchor='w', padx=20)
                Label(result_win, text=f"Correct answer: {detail['correct_answer']}", bg="#222222", fg="#66ff66", wraplength=500, justify='left').pack(anchor='w', padx=20)
                Label(result_win, text=f"Explanation: {detail['explanation']}", bg="#222222", fg="#f0f0f0", wraplength=500, justify='left').pack(anchor='w', padx=20, pady=(0,10))
        if all(d['is_correct'] for d in results['details']):
            Label(result_win, text="All answers correct!", bg="#222222", fg="#66ff66").pack(pady=10)
        Button(result_win, text="Close", command=result_win.destroy, bg="#333333", fg="#f0f0f0").pack(pady=10)