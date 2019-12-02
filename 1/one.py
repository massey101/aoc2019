import math


def calculate_fuel(module_mass):
    return math.floor(module_mass / 3) - 2


def calculate_total_fuel(module_masses):
    return sum([
        calculate_fuel(module_mass)
        for module_mass
        in module_masses
    ])
