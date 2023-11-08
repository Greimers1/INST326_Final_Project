import re

"""
"""
class TriviaGame:
    """ Represents a game. 
    """
    
    def regex(text):
        pattern  = r"""Q(?P<q_number>\d+): (?P<question>.*?[?])\nA(?P<a_number>
                            \d+): (?P<answer>.*?)$"""
        matches = re.search(pattern, text)
        for match in matches:
            q_number = match.group('q_number')
            question = match.group('question')
            a_number = match.group('a_number')
            answer = match.group('answer')
    def read_file(file):
        return None



class Driver : 
    """Represents a driver in the car. 
    """
    
class Road:
    """Represents the road that is driven on
    """
    
class Route: 
    """ Represents the route that must be taken to reach the destination.
    """
    