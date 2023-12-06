import re
import argparse
import time
import random
import matplotlib.pyplot as plt
import seaborn as sns

class TriviaGame:
    """
    By Adam Blum
    
    Class representing the QuizGame itself
    
    Attributes:
        q_number (int): The corresponding number to a question
        question (str): The question being aksed
        a_number (int): The corresponding number to an answer
        answer (str):  The answer to the question
    
    """
    
    def __init__(self, line):
        """
        By Ahmed Elhag
        
        Initializes the instances of the TriviaGame class. Sets the questions
        and answers to the related question
        
        Args:
            line (any): Incremented line of the file
        
        Side effects:
            Initializes attributes
        
        """
         
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
        
        """
        Displays the question and 
        answer to the question (after the answers are inputted)  
        
        Side Effects:
            Self explanatory
        """
        
        if self.question:
            print(f"Question {self.q_number}: {self.question}")
        elif self.answer:
            print(f"Answer {self.a_number}: {self.answer}")

    def get_answer(self):
        """Takes in the user's asnwers
        
        Returns:
            The user's input (answer)
          """  
        
        return input("Your answer: ").strip()

class Score:
    """
    Class keeps track of the overall score (Called by ScoreKeeper to seperate
    human and computer)
    
    
    Attributes:
        player_score (int): score of the player
        human (bool): Whether the player is human or not, default is True
        pronoun (string): Either "Player" or "Computer" depending 
                          on the human variable.
        
    """
    def __init__(self, human = True):
        """
        By David Mariona
        
        Initializes Score of the the players, sets values to 0 and assume 
        the player is human
        
        Args: 
            human(bool): Whether player is human or not, default is True
        
        Side effects:
            initializes attributes
        """
        self.player_score = 0
        self.human = human
        self.pronoun = "Player" if human else "Computer"
        
    def __str__(self):
        """Informal representation of the Score"""
        return f"{self.player_score}"
    
    def __lt__(self, other):
        """
        By Ahmed Elhag
        
        Defines the less than operator
        """
        return self.player_score < other.player_score
                   
    def __gt__(self, other):
        """Defines the greater than operator"""
        return self.player_score > other.player_score
    
    def __sub__(self, other):
        """Defines the subtraction operator"""
        return self.player_score - other.player_score

    def get_score(self, player_answer, correct_answer):
        """
        Increases the score of the player that has gotten the correct answer
        
        
        Args:
            player_answer (any): Answer of the player for the question
            correct_answer (any): the correct answer of the question
            
        
        Side Effects: Prints whether the player got the answer right, and 
                      increases their score if they did
        """
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
    """
    
    Class to keep the score between the player and computer
    
    Attributes:
        player_score (int): The players score
        computer_score (int): The computers score
    """
    def __init__(self):
        """
        By Kaiya Pankey
        
        Initializes the instances of the ScoreKeeper class. Scores set to 0
        
        Side Effects:
            Initializes variables
        """
        
        self.player_score = Score()
        self.computer_score = Score(human = False)
        
    def display_score(self):
        """Displays the score between the player and the computer"""
        
        print(f"Player: {self.player_score} | Computer: {self.computer_score}")

    def determine_winner(self):
        """
        By David Mariona
        
        Determines the winner between the player and computer, and prints 
        the score
        
        Side Effects:
            Prints the winner of the game, and by how mnany points
        """
        
        margin = abs(self.player_score - self.computer_score)
        
        if self.player_score > self.computer_score:
            print(f"Congratulations! You win by {margin} points!")
        elif self.player_score < self.computer_score:
            print(f"Sorry, the computer wins by {margin} points.")
        else:
            print("It's a tie!")
        
            
    def get_score(self, player_answer, correct_answer, human):
        """Uses Score.get_player_score() to increment the 
        
        Args:
            player_answer (any): answer of the human or computer
            correct_answer (any): correct answer for the current question
            human (bool): Whether player is human or not
        
        Side effects:
            Increases the score of the computer or human if they got the 
            question right"""
        if human:
            self.player_score.get_score(player_answer, correct_answer)
        else:
            self.computer_score.get_score(player_answer, correct_answer)
        
    def display_score_plot(self):
        """
        By Ammar Amir
        
        Displays a bar plot of the scores between the player and the computer.
        
        Side Effects:
            Displays a bar plot of the scores between the player & computer
            
        """
        scores = {'Player': self.player_score.player_score, 'Computer': self.computer_score.player_score}
        sns.barplot(x=list(scores.keys()), y=list(scores.values()))
        plt.title('Score Comparison')
        plt.xlabel('Player')
        plt.ylabel('Score')
        plt.show()
        



class Timer:
    """
    By Adam Blum
    
        Class that represents the timer used for the quiz
        
        Attributes:
            start_time (float): Time when the question is shown
            end_time (float): The time at which the user enters an answer
    
    
    """
    def __init__(self):
        """
        Initializes the Timer
        
        Attributes:
            start_time (float): Time when the question is shown
            end_time (float): The time at which the user enters an answer
        
        Side effects:
            Initializes attributes as None
        """
        self.start_time = None
        self.end_time = None

    def start(self):
        """
        Starts the Timer and stores the beginning time in the attribute
        
        Attributes:
            start_time (float): Time when the question is shown
        
        Side effects:
            Changes start_time
        """
        self.start_time = time.time()

    def end(self):
        """
        Ends the Timer and stores the ending time in the attribute
        
        Attributes:
            end (float): Time when the question is answered
        
        Side effects:
            Changes end_time
        """
        self.end_time = time.time()
        time_passed = self.end_time - self.start_time
        print(f"Time elapsed: {round(time_passed, 2)} seconds")

def run_game(file_path):
    """
    By Adam Blum: With statement
    & Kaiya Pankey: Incorporation of sequence unpacking (for question,answer...)
    
    
    Runs the game
    
    Args:
        file_path (str): Command line argument of a QA file
        
    Side effects:
        Combination of previous side effects, as 
        this makes the entire game occur in terminal
    
    """
    questions = []
    answers = []

    #
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
    input("Social Security Number Or UUID: ")
    for question, answer in zip(questions, answers):
        
        timer.start()
        print("Started Timer")
        question.display_question()
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
    score_keeper.display_score_plot()


if __name__ == "__main__":
    """
    By Amaar Amir
    
    Parses command line arguments
    
    """
    parser = argparse.ArgumentParser(description='Trivia Game')
    parser.add_argument('file_path', help='Path to the file containing trivia questions.')
    args = parser.parse_args()
    file_path = args.file_path

    run_game(file_path)
