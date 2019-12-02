import math


def calculate_fuel(module_mass):
    return math.floor(module_mass / 3) - 2


def calculate_total_fuel(module_masses):
    return sum([
        calculate_fuel(module_mass)
        for module_mass
        in module_masses
    ])


def calculate_fuels_fuel(fuel_mass):
    required_fuel_for_fuel = calculate_fuel(fuel_mass)
    if required_fuel_for_fuel <= 0:
        return fuel_mass

    return fuel_mass + calculate_fuels_fuel(required_fuel_for_fuel)


def calculate_adjusted_fuel(module_mass):
    fuel = calculate_fuel(module_mass)
    return calculate_fuels_fuel(fuel)


def calculate_adjusted_total_fuel(module_masses):
    return sum([
        calculate_adjusted_fuel(module_mass)
        for module_mass
        in module_masses
    ])
