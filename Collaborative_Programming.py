import re
import argparse

"""
"""
class TriviaGame:
    """ Represents a game. 
    """ 
    
    def __init__(self, line):
        pattern  = r"""Q(?P<q_number>\d+): (?P<question>.*?[?])\nA(?P<a_number>
                            \d+): (?P<answer>.*?)$"""
        matches = re.search(pattern, line)
        for match in matches:
            q_number = match.group('q_number')
            question = match.group('question')
            a_number = match.group('a_number')
            answer = match.group('answer')
            
    def read_file(file):
        with open(file, 'r', encoding = "utf-8") as f:
            game = [TriviaGame(line.strip()) for line in f]
        return game
    





class ScoreKeeper:
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        
    def get_player_score(self, player_answer, correct_answer):
        """ Calculates the player's score
        
        Args:
            player_answer(str): the answer the player provided.
            correct_answer(str): the correct answer.
            
        Side effects:
            Changes the score for the player.
            
        Returns: 
            self.player_score(int): the player's updated score.
        """
    
        if player_answer == correct_answer:
            self.player_score += 1
            print (f"You now have {self.player_score} points!")
        else: 
            self.player_score += 0
            print (f"You now have {self.player_score} points")
                
        return self.player_score
    
    
    def get_computer_score(self, computer_answer, correct_answer):
        """ Calculates the computer's score
        
        Args:
            computer_answer(str): the answer the computer provided.
            correct_answer(str): the correct answer.
            
        Side effects:
            Changes the score for the computer.
            
        Returns: 
            computer.player_score(int): the computer's updated score.
        """
    
        if computer_answer == correct_answer:
            self.computer_score+= 1
            print (f"You now have {self.computer_score} points!")
        else: 
            self.computer_score += 0
            print (f"You now have {self.computer_score} points.")
        
        return self.computer_score
        
    def display_score(self, last_question):
        pscore = self.get_player_score
        cscore = self.get_computer_score
        
        if pscore < 0 or cscore < 0:
                print("Invalid scores")
                return
        
        # This will print the scores and the result if the game is over and last question is true
        if last_question == True:
            
            if pscore == cscore:
                print(f"You have tied. The final score was: \n Player: {pscore}\nComputer: {cscore}")
                return

            player_win = True if pscore > cscore else False
        
            if player_win:
                pwin = f"Congrats the player won!! The final score was: \n Player: {pscore}\nComputer: {cscore}"
                plose = f"Sorry the computer won :( The final score was: \n Player: {pscore}\nComputer: {cscore}"
                print (pwin if player_win else plose)
                 
        else:
            # This will print if the game is still going and the display_score function is called
            print(f"The score is: \n Player: {pscore}\nComputer: {cscore}")

class Timer: 
    def __init__(self): 
        self.start_time = None
        self.end_time = None
        
    def start(self): 
         self.start_time = timed()
    
    def end (self): 
        self.end_time = timed()
        while self.start_time is not None: 
            time_passed = self.end_time - self.start_time
            print (f"time elasped: {time_passed} seconds ") 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Trivia Game')
    parser.add_argument('file_path', help='Path to the file containing trivia questions.')
    args = parser.parse_args()
    file_path = args.file_path()  