import re

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
    def __init__(self, player_score, computer_score):
        self.player_score = 0
        self.computer_score = 0 
        
    def get_player_score(self):
        return self.player_score
    
    def get_computer_score(self):
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
                print(f"Congrats the player won!! The final score was: \n Player: {pscore}\nComputer: {cscore}")
            else: 
                 print(f"Sorry the computer won :( The final score was: \n Player: {pscore}\nComputer: {cscore}")
                 
        else:
            # This will print if the game is still going and the display_score function is called
            print(f"The score is: \n Player: {pscore}\nComputer: {cscore}")
        

