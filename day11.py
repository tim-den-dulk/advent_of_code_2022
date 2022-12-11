import re
from get_inputs import GetInputs


class Monkey:

    monkeylist = []
    worry_mod = 1

    def __init__(self, input_string):
        self.id = int(input_string[0][7])
        items = re.findall("[0-9]+", input_string[1])
        self.items = list(map(int, items))
        self.operation = input_string[2].split("=")[1]
        self.test = int(re.search("[0-9]+", input_string[3])[0])
        self.if_true = int(re.search("[0-9]+", input_string[4])[0])
        self.if_false = int(re.search("[0-9]+", input_string[5])[0])
        assert self.id != self.if_true and self.id != self.if_false
        self.activity = 0
        self.monkeylist.append(self)
        Monkey.worry_mod *= self.test

    @classmethod
    def get_monkey(cls, id):
        for monkey in cls.monkeylist:
            if monkey.id == id:
                return monkey

    def turn(self):
        self.activity += len(self.items)
        for item in self.items:
            old = item
            worry = eval(self.operation)
            # worry = worry // 3
            worry = worry % self.worry_mod
            try:
                if worry % self.test == 0:
                    self.get_monkey(self.if_true).items.append(worry)
                else:
                    self.get_monkey(self.if_false).items.append(worry)
            except:
                print("monkey not found")
        self.items = []

    def __gt__(self, other):
        return self.id > other.id

    def __repr__(self):
        return (
            "Monkey "
            + str(self.id)
            + ": "
            + str(self.items)
            + " ## "
            + str(self.activity)
        )


data = GetInputs(11).lines()
for i in range(0, len(data), 7):
    Monkey(data[i : i + 6])
monkey_list = Monkey.monkeylist
monkey_list.sort()
turns = 10000
for _ in range(turns):
    for monkey in monkey_list:
        monkey.turn()

res = []
for monkey in monkey_list:
    res.append(monkey.activity)
res.sort(reverse=True)
print(res[0] * res[1])
