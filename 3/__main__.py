import sys
import three


filename = sys.argv[1]

with open(filename) as f:
    input_data = []
    for line in f:
        input_data.append(line.strip().split(','))

print(three.get_distance_to_closest_cross(input_data))
print(three.get_wire_distance_to_closest_cross(input_data))
