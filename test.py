import re
import argparse
import time
import random

class TriviaGame:
    def __init__(self, line):
        question_pattern = r"Q(\d+): (.*)$"
        answer_pattern = r"A(\d+): (.*)$"

        question_match = re.match(question_pattern, line)
        answer_match = re.match(answer_pattern, line)

        if question_match:
            self.q_number = int(question_match.group(1))
            self.question = question_match.group(2)
            self.answer = None
        elif answer_match:
            self.a_number = int(answer_match.group(1))
            self.answer = answer_match.group(2)
            self.q_number = None
            self.question = None
        else:
            raise ValueError(f"Invalid format for trivia line: {line}")

    def display_question(self):
        if hasattr(self, 'question') and self.question:
            print(f"Question {self.q_number}: {self.question}")
        elif hasattr(self, 'answer') and self.answer:
            print(f"Answer {self.a_number}: {self.answer}")

    def get_answer(self):
        if hasattr(self, 'q_number') and self.q_number is not None:
            return input("Your answer: ").strip()
        else:
            return None  # No need to get an answer for answers

class ScoreKeeper:
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0

    # def get_player_score(self, player_answer, correct_answer):
    #     print(f"Player Answer: {player_answer}")
    #     if correct_answer is not None:
    #         print(f"Correct Answer: {correct_answer.lower()}")
    #         if player_answer and player_answer.lower() == correct_answer.lower():
    #             self.player_score += 1
    #             print(f"You now have {self.player_score} points!")
    #         else:
    #             print(f"You now have {self.player_score} points.")
    #     else:
    #         print("Invalid question format. Cannot determine correct answer.")

    # def get_computer_score(self, correct_answer):
    #     if correct_answer is not None:
    #         computer_answer = random.choice(['option1', 'option2', 'option3'])
    #         print(f"Computer's answer: {computer_answer}, Correct: {computer_answer.lower() == correct_answer.lower()}")
    #         if computer_answer.lower() == correct_answer.lower():
    #             self.computer_score += 1
    #             print(f"Computer now has {self.computer_score} points!")
    #         else:
    #             print(f"Computer now has {self.computer_score} points.")
    #     else:
    #         print("Invalid question format. Cannot determine correct answer.")
    
    def get_player_score(self, player_answer, correct_answer):
        print(f"Player Answer: {player_answer}")
        if correct_answer is not None:
            print(f"Correct Answer: {correct_answer}")
            if player_answer == correct_answer:
                self.player_score += 1
                print(f"Correct! You now have {self.player_score} points!")
            else:
                print(f"Sorry, the correct answer is {correct_answer}. You still have {self.player_score} points.")
        else:
            print("Invalid question format. Cannot determine the correct answer.")

    def get_computer_score(self, correct_answer):
        if correct_answer is not None:
            computer_answer = random.choice([correct_answer, correct_answer, correct_answer])
            print(f"Computer's answer: {computer_answer}, Correct: {computer_answer == correct_answer}")
            if computer_answer == correct_answer:
                self.computer_score += 1
                print(f"Computer now has {self.computer_score} points!")
            else:
                print(f"Computer now has {self.computer_score} points.")
        else:
            print("Invalid question format. Cannot determine the correct answer.")

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
    with open(file_path, 'r', encoding='utf-8') as f:
        for line_number, line in enumerate(f, start=1):
            try:
                game = TriviaGame(line.strip())
            except ValueError as e:
                print(f"Error on line {line_number}: {e}")
            else:
                game.display_question()
                timer.start()
                if game.answer is not None:
                    score_keeper.get_computer_score(game.answer)
                else:
                    player_answer = game.get_answer()
                    timer.end()
                    score_keeper.get_player_score(player_answer, game.answer)

                score_keeper.display_score()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Trivia Game')
    parser.add_argument('file_path', help='Path to the file containing trivia questions.')
    args = parser.parse_args()
    file_path = args.file_path

    score_keeper = ScoreKeeper()
    timer = Timer()

    run_game(file_path)

    score_keeper.determine_winner()