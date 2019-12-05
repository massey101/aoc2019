class WireInstruction:
    directions = {
        'R': (+1, 0),
        'L': (-1, 0),
        'U': (0, +1),
        'D': (0, -1),
    }

    def __init__(self, instruction_str):
        self.direction = self.directions[instruction_str[0]]
        self.distance = int(instruction_str[1:])

    def step(self, coord):
        return (coord[0] + self.direction[0], coord[1] + self.direction[1])


class Wire:
    def __init__(self, instructions):
        # Don't include 0, 0 in history as we don't want to use it as an
        # intersection point
        self.history = []
        self.current = (0, 0)
        self.run_instructions(
            [WireInstruction(instruction) for instruction in instructions],
        )

    def run_instructions(self, instructions):
        for instruction in instructions:
            for i in range(instruction.distance):
                self.current = instruction.step(self.current)
                self.history.append(self.current)

    def intersections(self, wire):
        return set(self.history).intersection(set(wire.history))

    def distance(self, coord):
        return self.history.index(coord) + 1


def manhatten_distance(coord):
    return abs(coord[0]) + abs(coord[1])


def get_distance_to_closest_cross(input_data):
    wire1 = Wire(input_data[0])
    wire2 = Wire(input_data[1])
    distances = [
        manhatten_distance(coord)
        for coord
        in wire1.intersections(wire2)
    ]
    return min(distances)


def get_wire_distance_to_closest_cross(input_data):
    wire1 = Wire(input_data[0])
    wire2 = Wire(input_data[1])
    distances = [
        wire1.distance(coord) + wire2.distance(coord)
        for coord
        in wire1.intersections(wire2)
    ]
    return min(distances)
