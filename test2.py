import re
import argparse
import time
import random

class TriviaGame:
    def __init__(self, line):
        question_pattern = r"Q(?P<qnum>\d+): (?P<question>.+)$"
        answer_pattern = r"A(?P<anum>\d+): (?P<answer>.+)$"

        question_match = re.match(question_pattern, line)
        answer_match = re.match(answer_pattern, line)

        if question_match:
            self.q_number = int(question_match.group('qnum'))
            self.question = question_match.group('question')
            self.answer = None  # Set answer to None for questions
        elif answer_match:
            self.a_number = int(answer_match.group('anum'))
            self.answer = answer_match.group('answer')  # Set answer for answers
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
            return input("Your answer: ").strip()

class Score:
    def __init__(self, human = True):
        self.player_score = 0
        self.human = human
        self.pronoun = "Player" if human else "Computer"
        
    def __str__(self):
        return f"{self.player_score}"
    
    def __lt__(self, other):
        return self.player_score < other.player_score
                   
    def __gt__(self, other):
        return self.player_score > other.player_score
    
    def __sub__(self, other):
        return self.player_score - other.player_score

    def get_score(self, player_answer, correct_answer):
        print(f"{self.pronoun} Answer: {player_answer}")
        if correct_answer is not None:
            if player_answer and player_answer.lower() == correct_answer.lower():
                self.player_score += 1
                print(f"{self.pronoun} now has {self.player_score} points!")
            else:
    
                print(f"{self.pronoun} now has {self.player_score} points.")
        else:
            print("Invalid question format. Cannot determine correct answer.")


class ScoreKeeper:
    """Class to keep the score between the player and computer
    
    Attributes:
        player_score (int): The players score
        computer_score (int): The computers score
    """
    def __init__(self):
<<<<<<< HEAD
        self.player_score = Score()
        self.computer_score = Score(human = False)
        
=======
        """Initializes the instances of the ScoreKeeper class. Scores set to 0"""
        
        self.player_score = 0
        self.computer_score = 0

    def get_player_score(self, player_answer, correct_answer):
        """Updates the players score
        
        Args:
            player_answer (str): Players answer to question
            correct_answer (str): Computers answer to question
        
        Side effects:
            Prints to say if the players score is correct or not
        """
        
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
        """Updates the computers score
        
        Args:
            correct_answer (str): Correct answer to the question
        
        Side effects:
            Print to say if the computers score is correct or not
        """
        
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

>>>>>>> c86e8ad91f9474a46bc86dbf934500d570406b62
    def display_score(self):
        """Displays the score between the player and the computer"""
       
        print(f"Player: {self.player_score} | Computer: {self.computer_score}")

    def determine_winner(self):
<<<<<<< HEAD
        margin = abs(self.player_score - self.computer_score)
=======
        """
        Determines the winner between the player and computer, and prints 
        the score
        """
        
>>>>>>> c86e8ad91f9474a46bc86dbf934500d570406b62
        if self.player_score > self.computer_score:
            print(f"Congratulations! You win by {margin} points!")
        elif self.player_score < self.computer_score:
            print(f"Sorry, the computer wins by {margin} points.")
        else:
            print("It's a tie!")
            
    def get_score(self, player_answer, correct_answer, human):
        if human:
            self.player_score.get_score(player_answer, correct_answer)
        else:
            self.computer_score.get_score(player_answer, correct_answer)
        
        



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
        
        timer.start()
        print("Started Timer")
        player_answer = question.get_answer()
        print(f"{player_answer!r}")
        timer.end()
        print("Ended timer")
        
        computer_answer = random.choice(['beep boop', answer.answer])
        print(f"Correct Answer: {answer.answer.lower()}")
        score_keeper.get_score(player_answer, answer.answer, human = True)
        score_keeper.get_score(computer_answer, answer.answer, human = False)
        score_keeper.display_score()

    score_keeper.determine_winner()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Trivia Game')
    parser.add_argument('file_path', help='Path to the file containing trivia questions.')
    args = parser.parse_args()
    file_path = args.file_path

    run_game(file_path)
