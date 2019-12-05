def find_adjacent(password):
    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            return True
    return False


def increasing(password):
    for i in range(1, len(password)):
        if int(password[i]) < int(password[i-1]):
            return False

    return True


def valid(password):
    if len(password) != 6:
        return False

    if find_adjacent(password) is False:
        return False

    if not increasing(password):
        return False

    return True


def find_adjacent2(password):
    adjacents = {}
    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            if password[i] in adjacents:
                adjacents[password[i]] += 1
            else:
                adjacents[password[i]] = 1

    return 1 in adjacents.values()


def valid2(password):
    if valid(password) is False:
        return False

    if find_adjacent2(password) is False:
        return False

    return True
