import copy
import math


class Instruction:
    def __init__(self, value, name, inputs, outputs, execute):
        self.value = value
        self.name = name
        self.inputs = inputs
        self.outputs = outputs
        self.execute = execute

    @classmethod
    def decode(cls, instruction):
        return instruction % 100

    def get_parameter_modes(self, instruction):
        return [
            math.floor(instruction / (math.pow(10, i+2))) % 10
            for i
            in range(self.inputs)
        ]

    def get_parameters(self, intcode):
        modes = self.get_parameter_modes(intcode.read(intcode.counter))
        params = []
        arg_pointer = intcode.counter + 1
        for i in range(self.inputs):
            value = intcode.read(arg_pointer)
            if not modes[i]:
                value = intcode.read(value)

            params.append(value)
            arg_pointer += 1

        for i in range(self.outputs):
            params.append(intcode.read(arg_pointer))
            arg_pointer += 1

        return params


class Intcode:

    def __init__(self, state):
        self.state = copy.deepcopy(state)
        self.counter = 0
        self.outputs = []

        self.opcodes = {
            1: Instruction(1, 'add', 2, 1, self.add),
            2: Instruction(2, 'multiply', 2, 1, self.multiply),
            3: Instruction(3, 'store', 0, 1, self.store),
            4: Instruction(4, 'output', 1, 0, self.output),
            5: Instruction(5, 'jump-if-true', 2, 0, self.jump_if_true),
            6: Instruction(6, 'jump-if-false', 2, 0, self.jump_if_false),
            7: Instruction(7, 'less-than', 2, 1, self.less_than),
            8: Instruction(8, 'equals', 2, 1, self.equals),
            99: Instruction(99, 'finish', 0, 0, self.finish),
        }

    def read(self, pointer):
        return self.state[pointer]

    def write(self, pointer, value):
        self.state[pointer] = value

    def add(self, a, b, c):
        self.write(c, a + b)
        self.counter += 4
        return True

    def multiply(self, a, b, c):
        self.write(c, a * b)
        self.counter += 4
        return True

    def store(self, a):
        value = self.inputs.pop(0)
        self.write(a, value)
        self.counter += 2
        return True

    def output(self, a):
        self.outputs.append(a)
        self.counter += 2
        return True

    def jump_if_true(self, a, b):
        if a:
            self.counter = b
        else:
            self.counter += 3
        return True

    def jump_if_false(self, a, b):
        if not a:
            self.counter = b
        else:
            self.counter += 3
        return True

    def less_than(self, a, b, c):
        if a < b:
            self.write(c, 1)
        else:
            self.write(c, 0)
        self.counter += 4
        return True

    def equals(self, a, b, c):
        if a == b:
            self.write(c, 1)
        else:
            self.write(c, 0)
        self.counter += 4
        return True

    def finish(self):
        return False

    def execute(self):
        opcode = Instruction.decode(self.state[self.counter])
        instruction = self.opcodes[opcode]
        parameters = instruction.get_parameters(self)
        return instruction.execute(*parameters)

    def run(self, inputs):
        self.inputs = inputs
        while self.execute() is True:
            pass
        return self.outputs
