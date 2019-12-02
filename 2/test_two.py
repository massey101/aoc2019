import two


class TestIntcode:

    def test1(self):
        input_codes = [1, 0, 0, 0, 99]
        assert two.raw_run(input_codes) == [2, 0, 0, 0, 99]

    def test2(self):
        input_codes = [2, 3, 0, 3, 99]
        assert two.raw_run(input_codes) == [2, 3, 0, 6, 99]

    def test3(self):
        input_codes = [2, 4, 4, 5, 99, 0]
        assert two.raw_run(input_codes) == [2, 4, 4, 5, 99, 9801]

    def test4(self):
        input_codes = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        assert two.raw_run(input_codes) == [30, 1, 1, 4, 2, 5, 6, 0, 99]

    def test_run(self):
        input_codes = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        assert two.raw_run(input_codes) == [30, 1, 1, 4, 2, 5, 6, 0, 99]

    def test_fund(self):
        input_codes = [1, 0, 0, 5, 2, 5, 6, 0, 99]
        assert two.find(input_codes, 30) == 2
