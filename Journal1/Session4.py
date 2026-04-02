import random
class Coot:
    def __init__(self, name):
        self.name = name
        self.arm_len_cm = round(random.uniform(58.4, 63.5), 2)
        self.leg_len_in = round(random.uniform(2.0, 2.2), 2)
        self.num_eyes = 2
        self.has_tail = True
        self.is_furry = False

    def __str__(self):
        return f"{self.name} (class Coot) \nhas an arm length of {self.arm_len_cm} cm, \na leg length of {self.leg_len_in} in, \n{self.num_eyes} eyes, \n{'a tail' if self.has_tail else 'no tail'}, \nand is {'furry' if self.is_furry else 'not furry'}."

Fredrick = Coot("Fredrick")
print(Fredrick)