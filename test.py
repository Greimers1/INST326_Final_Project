import re
import argparse
import time
import random

class TriviaGame:
    def __init__(self, line):
        pattern = r"Q(\d+): (.*?[?])\s*\nA(\d+): (.*)$"
        match = re.search(pattern, line, re.IGNORECASE)
        if not match:
            raise ValueError(f"Invalid format for trivia question: {line}")
        
        self.q_number = int(match.group(1))
        self.question = match.group(2)
        self.a_number = int(match.group(3))
        self.answer = match.group(4)

    def display_question(self):
        print(f"Question {self.q_number}: {self.question}")

    def get_answer(self):
        return input("Your answer: ").strip()

class ScoreKeeper:
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0

    def get_player_score(self, player_answer, correct_answer):
        if player_answer == correct_answer:
            self.player_score += 1
            print(f"You now have {self.player_score} points!")
        else:
            print(f"You now have {self.player_score} points.")

    def get_computer_score(self, correct_answer):
        # Implement logic for computer's answer (random or predetermined)
        computer_answer = random.choice(['option1', 'option2', 'option3'])
        if computer_answer == correct_answer:
            self.computer_score += 1
            print(f"Computer now has {self.computer_score} points!")
        else:
            print(f"Computer now has {self.computer_score} points.")

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Trivia Game')
    parser.add_argument('file_path', help='Path to the file containing trivia questions.')
    args = parser.parse_args()
    file_path = args.file_path

    with open(file_path, 'r', encoding='utf-8') as f:
        games = [TriviaGame(line.strip()) for line in f]

    score_keeper = ScoreKeeper()
    timer = Timer()

    for game in games:
        game.display_question()
        timer.start()
        player_answer = game.get_answer()
        timer.end()

        score_keeper.get_player_score(player_answer, game.answer)
        score_keeper.get_computer_score(game.answer)
        score_keeper.display_score()

    score_keeper.determine_winner()