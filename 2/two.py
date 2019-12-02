import copy


class Intcode:
    def __init__(self, state):
        self.state = state
        self.counter = 0

    def read(self, pointer):
        return self.state[pointer]

    def write(self, pointer, value):
        self.state[pointer] = value

    def execute(self):
        i = self.state[self.counter]
        if i == 99:
            return False
        if i == 1:
            ap = self.state[self.counter+1]
            bp = self.state[self.counter+2]
            cp = self.state[self.counter+3]
            self.write(cp, self.read(ap) + self.read(bp))
            return True
        if i == 2:
            ap = self.state[self.counter+1]
            bp = self.state[self.counter+2]
            cp = self.state[self.counter+3]
            self.write(cp, self.read(ap) * self.read(bp))
            return True

    def step(self):
        self.counter += 4

    def run(self):
        while self.execute() is True:
            self.step()


def raw_run(state):
    intcode = Intcode(state)
    intcode.run()
    return intcode.state


def run(state, noun, verb):
    state = copy.deepcopy(state)
    state[1] = noun
    state[2] = verb
    return raw_run(state)[0]


def find(state, target):
    for noun in range(0, 99):
        for verb in range(0, 99):
            if run(state, noun, verb) == target:
                return 100 * noun + verb
