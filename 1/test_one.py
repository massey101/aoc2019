import one


class TestCalculateFuel:

    def test1(self):
        assert one.calculate_fuel(12) == 2

    def test2(self):
        assert one.calculate_fuel(14) == 2

    def test3(self):
        assert one.calculate_fuel(1969) == 654

    def test4(self):
        assert one.calculate_fuel(100756) == 33583

    def test_total(self):
        module_masses = [12, 14, 1969, 100756]
        assert one.calculate_total_fuel(module_masses) == 34241
