import re
import argparse
import time
import random

class TriviaGame:
    def __init__(self, line):
        question_pattern = r"Q(\d+): (.+)$"
        answer_pattern = r"A(\d+): (.+)$"

        question_match = re.match(question_pattern, line)
        answer_match = re.match(answer_pattern, line)

        if question_match:
            self.q_number = int(question_match.group(1))
            self.question = question_match.group(2)
            self.answer = None  # Set answer to None for questions
        elif answer_match:
            self.a_number = int(answer_match.group(1))
            self.answer = answer_match.group(2)  # Set answer for answers
            self.q_number = None  # Set q_number to None for answers
            self.question = None  # Set question to None for answers
        else:
            raise ValueError(f"Invalid format for trivia line: {line}")

    def display_question(self):
        if self.question:
            print(f"Question {self.q_number}: {self.question}")
        elif self.answer:
            print(f"Answer {self.a_number}: {self.answer}")

    def get_answer(self):
        if self.question:
            return input("Your answer: ").strip()

class ScoreKeeper:
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0

    def get_player_score(self, player_answer, correct_answer):
        print(f"Player Answer: {player_answer}")
        if correct_answer is not None:
            print(f"Correct Answer: {correct_answer.lower()}")
            
            if player_answer and player_answer.lower() == correct_answer.lower():
                self.player_score += 1
                print(f"You now have {self.player_score} points!")
            else:
    
                print(f"You now have {self.player_score} points.")
        else:
            print("Invalid question format. Cannot determine correct answer.")

    def get_computer_score(self, correct_answer):
        if correct_answer is not None:
            computer_answer = random.choice(['beep bopp', correct_answer])
            print(f"Computer's answer: {computer_answer}, Correct: {computer_answer.lower() == correct_answer.lower()}")
            if computer_answer.lower() == correct_answer.lower():
                self.computer_score += 1
                print(f"Computer now has {self.computer_score} points!")
            else:
                print(f"Computer now has {self.computer_score} points.")
        else:
            print("Invalid question format. Cannot determine correct answer.")

    def display_score(self):
        print(f"Player: {self.player_score} | Computer: {self.computer_score}")

    def determine_winner(self):
        if self.player_score > self.computer_score:
            print("Congratulations! You win!")
        elif self.player_score < self.computer_score:
            print("Sorry, the computer wins.")
        else:
            print("It's a tie!")

class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = time.time()

    def end(self):
        self.end_time = time.time()
        time_passed = self.end_time - self.start_time
        print(f"Time elapsed: {time_passed} seconds")

def run_game(file_path):
    questions = []
    answers = []

    with open(file_path, 'r', encoding='utf-8') as f:
        for line_number, line in enumerate(f, start=1):
            line = line.strip()
            if line:  # Skip empty lines
                try:
                    game = TriviaGame(line)
                    if game.question:
                        questions.append(game)
                    elif game.answer:
                        answers.append(game)
                except ValueError as e:
                    print(f"Error on line {line_number}: {e}")

    score_keeper = ScoreKeeper()
    timer = Timer()

    for question, answer in zip(questions, answers):
        question.display_question()
        print("displayed question")
        timer.start()
        print("started timer")
        player_answer = question.get_answer()
        print(f"{player_answer!r}")
        timer.end()
        print("ended timer")

        score_keeper.get_player_score(player_answer, answer.answer)
        print(f"{player_answer}")
        score_keeper.get_computer_score(answer.answer)
        score_keeper.display_score()

    score_keeper.determine_winner()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Trivia Game')
    parser.add_argument('file_path', help='Path to the file containing trivia questions.')
    args = parser.parse_args()
    file_path = args.file_path

    run_game(file_path)
