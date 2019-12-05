import four

puzzle_input = (152085, 670283)

valid = [
    1
    if four.valid(str(i))
    else 0
    for i
    in range(puzzle_input[0], puzzle_input[1])
]
print(sum(valid))

valid2 = [
    1
    if four.valid2(str(i))
    else 0
    for i
    in range(puzzle_input[0], puzzle_input[1])
]
print(sum(valid2))
