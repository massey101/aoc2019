import five


def test_immediate_multiply():
    input_data = [1002, 4, 3, 4, 33]
    intcode = five.Intcode(input_data)
    intcode.run([])
    assert intcode.state[4] == 99


def test_input_output1():
    input_data = [3, 3, 104, 10, 99]
    intcode = five.Intcode(input_data)
    assert intcode.run([1]) == [1]


def test_input_output2():
    input_data = [3, 3, 104, 10, 99]
    intcode = five.Intcode(input_data)
    assert intcode.run([5]) == [5]


def test_position_mode_equal_to_true():
    input_data = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
    intcode = five.Intcode(input_data)
    assert intcode.run([8]) == [1]


def test_position_mode_equal_to_false():
    input_data = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
    intcode = five.Intcode(input_data)
    assert intcode.run([10]) == [0]


def test_position_mode_less_than_true():
    input_data = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
    intcode = five.Intcode(input_data)
    assert intcode.run([5]) == [1]


def test_position_mode_less_than_false():
    input_data = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
    intcode = five.Intcode(input_data)
    assert intcode.run([8]) == [0]


def test_immediate_mode_equal_to_true():
    input_data = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
    intcode = five.Intcode(input_data)
    assert intcode.run([8]) == [1]


def test_immediate_mode_equal_to_false():
    input_data = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
    intcode = five.Intcode(input_data)
    assert intcode.run([18]) == [0]


def test_immediate_mode_less_than_true():
    input_data = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
    intcode = five.Intcode(input_data)
    assert intcode.run([5]) == [1]


def test_immediate_mode_less_than_false():
    input_data = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
    intcode = five.Intcode(input_data)
    assert intcode.run([10]) == [0]


def test_position_mode_jumping_not_equal_true():
    input_data = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
    intcode = five.Intcode(input_data)
    assert intcode.run([1]) == [1]


def test_position_mode_jumping_not_equal_false():
    input_data = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
    intcode = five.Intcode(input_data)
    assert intcode.run([0]) == [0]


def test_immediate_mode_jumping_not_equal_true():
    input_data = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
    intcode = five.Intcode(input_data)
    assert intcode.run([1]) == [1]


def test_immediate_mode_jumping_not_equal_false():
    input_data = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
    intcode = five.Intcode(input_data)
    assert intcode.run([0]) == [0]


def test_comparison_less_than():
    input_data = [
        3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
        1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
        999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99
    ]
    intcode = five.Intcode(input_data)
    assert intcode.run([7]) == [999]


def test_comparison_equal():
    input_data = [
        3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
        1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
        999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99
    ]
    intcode = five.Intcode(input_data)
    assert intcode.run([8]) == [1000]


def test_comparison_greater_than():
    input_data = [
        3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
        1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
        999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99
    ]
    intcode = five.Intcode(input_data)
    assert intcode.run([9]) == [1001]
