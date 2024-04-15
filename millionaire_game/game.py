class Game:
    def __init__(self, questions):
        self.questions = questions
        self.current_question_index = 0
        self._score = 0

    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index = + 1
            return question
        else:
            return None

    def submit_answer(self, answer):
        current_question = self.questions[self.current_question_index - 1]
        if current_question.check_answer(answer):
            self.get_score += 100
            return True
        else:
            return False

    def get_score(self):
        return f'{self._score}'

    def __str__(self):
        return f'Current score: {self._score}'
