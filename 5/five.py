import copy


class Instruction:
    def __init__(self, execute, inputs, outputs):
        self.execute = execute
        self.inputs = inputs
        self.outputs = outputs

    @classmethod
    def decode(cls, instruction):
        return instruction % 100

    def get_parameters(self, intcode):
        instruction = intcode.read(intcode.counter)
        params = []
        arg_pointer = intcode.counter + 1
        for i in range(self.inputs):
            value = intcode.read(arg_pointer)
            if not int(instruction / (10 ** (i + 2))) % 10:
                value = intcode.read(value)

            params.append(value)
            arg_pointer += 1

        for i in range(self.outputs):
            value = intcode.read(arg_pointer)
            params.append(value)
            arg_pointer += 1

        return params


class Intcode:

    def __init__(self, state):
        self.state = copy.deepcopy(state)
        self.counter = 0
        self.outputs = []

        self.opcodes = {
            1: Instruction(self.add, 2, 1),
            2: Instruction(self.multiply, 2, 1),
            3: Instruction(self.store, 0, 1),
            4: Instruction(self.output, 1, 0),
            5: Instruction(self.jump_if_true, 2, 0),
            6: Instruction(self.jump_if_false, 2, 0),
            7: Instruction(self.less_than, 2, 1),
            8: Instruction(self.equals, 2, 1),
            99: Instruction(self.finish, 0, 0),
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
        self.counter = b if a else self.counter + 3
        return True

    def jump_if_false(self, a, b):
        self.counter = b if not a else self.counter + 3
        return True

    def less_than(self, a, b, c):
        value = 1 if a < b else 0
        self.write(c, value)
        self.counter += 4
        return True

    def equals(self, a, b, c):
        value = 1 if a == b else 0
        self.write(c, value)
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
