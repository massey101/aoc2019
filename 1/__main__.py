import sys
import one


filename = sys.argv[1]

with open(filename) as f:
    module_masses = [int(line) for line in f]
    print(one.calculate_total_fuel(module_masses))
