import json
import random

class PracticeTests:
    def __init__(self, questions_file):
        self.questions_file = questions_file
        self.data = self.load_data()
        self.current_questions = []

    def load_data(self):
        with open(self.questions_file, 'r') as file:
            return json.load(file)

    def load_module_questions(self, module_name, num_questions=10):
        questions = self.data['modules'].get(module_name, [])
        random.shuffle(questions)
        self.current_questions = questions[:num_questions]
        return self.current_questions

    def load_full_exam(self):
        # Domain weights for 45 questions (rounded to nearest integer)
        domain_weights = {
            'General Security Concepts': 5,   # 12% of 45 ≈ 5
            'Threats, Vulnerabilities, and Mitigations': 10,  # 22% of 45 ≈ 10
            'Security Architecture': 8,      # 18% of 45 ≈ 8
            'Security Operations': 13,       # 28% of 45 ≈ 13
            'Security Program Management and Oversight': 9   # 20% of 45 ≈ 9
        }
        selected_questions = []
        for domain, count in domain_weights.items():
            questions = self.data['modules'].get(domain, [])
            random.shuffle(questions)
            selected_questions.extend(questions[:count])
        random.shuffle(selected_questions)
        self.current_questions = selected_questions
        return self.current_questions

    def get_available_modules(self):
        return list(self.data['modules'].keys())

    def get_available_exams(self):
        return [exam['title'] for exam in self.data.get('full_exams', [])]

    def evaluate_answers(self, user_answers):
        results = []
        correct_count = 0
        for q, user_answer in zip(self.current_questions, user_answers):
            is_correct = (user_answer == q['answer'])
            if is_correct:
                correct_count += 1
            results.append({
                'question': q['question'],
                'user_answer': user_answer,
                'correct_answer': q['answer'],
                'explanation': q.get('explanation', ''),
                'is_correct': is_correct
            })
        return {
            'correct': correct_count,
            'total': len(self.current_questions),
            'details': results
        }