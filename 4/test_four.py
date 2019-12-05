import four


def test1():
    input_data = '111111'
    assert four.valid(input_data) is True


def test2():
    input_data = '223450'
    assert four.valid(input_data) is False


def test3():
    input_data = '123789'
    assert four.valid(input_data) is False


def test4():
    input_data = '112233'
    assert four.valid2(input_data) is True


def test5():
    input_data = '123444'
    assert four.valid2(input_data) is False


def test6():
    input_data = '111122'
    assert four.valid2(input_data) is True
