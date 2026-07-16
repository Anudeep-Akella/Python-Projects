from abc import ABC, abstractmethod
import random


class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0,0)
        self.path = [self.position]
    
    def make_move(self):
        move = random.choice(self.moves)
        new_position = (self.position[0] + move[0], self.position[1] + move[1])
        self.path.append(new_position)
        return new_position
    
    @abstractmethod
    def level_up(self):
        pass


class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Up, Down, Right, Left

    def level_up(self):
        self.moves.append((1, 1))  # Diagonal move
        self.moves.append((-1, -1))
        self.moves.append((-1, 1))
        self.moves.append((1, -1))