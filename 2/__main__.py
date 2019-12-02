import sys
import two


filename = sys.argv[1]

with open(filename) as f:
    program = [int(num) for num in f.read().split(',')]
    print(program)

print(two.run(program, 12, 2))
print(two.find(program, 19690720))
