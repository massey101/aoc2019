import sys
import five


filename = sys.argv[1]

with open(filename) as f:
    program = [int(num) for num in f.read().split(',')]

intcode = five.Intcode(program)
print(intcode.run([1]))

intcode = five.Intcode(program)
print(intcode.run([5]))
