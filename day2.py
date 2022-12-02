from enum import Enum

from get_inputs import GetInputs


class RockPaperScissors(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

    @classmethod
    def from_letter(cls, letter):
        match letter:
            case "A" | "X":
                return cls.ROCK
            case "B" | "Y":
                return cls.PAPER
            case "C" | "Z":
                return cls.SCISSORS
            case _:
                raise SyntaxError("unexpected input")

    def compare(self, other):
        return (self.value - other.value) % 3

    def __lt__(self, other):
        return self.compare(other) == 2

    def __gt__(self, other):
        return self.compare(other) == 1

    def __eq__(self, other):
        return self.compare(other) == 0


class ParseInput:
    def __init__(self, input_line):
        self.inputs = input_line.split()
        self.them = RockPaperScissors.from_letter(self.inputs[0])
        # part 1
        self.us = RockPaperScissors.from_letter(self.inputs[1])
        # part 2
        self.us = self.pick_rps()

    def score_points(self):
        score = self.us.value + 1
        if self.us > self.them:
            score += 6
        elif self.us == self.them:
            score += 3
        return score

    def pick_rps(self):
        match self.inputs[1]:
            case "X":
                return RockPaperScissors((self.them.value - 1) % 3)
            case "Y":
                return RockPaperScissors(self.them.value)
            case "Z":
                return RockPaperScissors((self.them.value + 1) % 3)


data = GetInputs(2).lines()
total_score = 0
for line in data:
    total_score += ParseInput(line).score_points()
print(total_score)
