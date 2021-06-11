import string

alphabet = string.ascii_lowercase


def get_stat(text: list) -> list:
    stat = [0 for _ in alphabet]
    full_sum = 0
    for x in text:
        for sym in x:
            if sym in alphabet:
                stat[alphabet.index(sym)] += 1
                full_sum += 1
    for i in range(len(stat)):
        x = stat[i]
        if x == 0:
            continue
        stat[i] = x / full_sum
    return stat


def find_model_distance(shift: int, first_stat: list, second_stat: list) -> int:
    if len(first_stat) != len(alphabet) or len(second_stat) != len(alphabet):
        raise ValueError('Wrong stat')
    distance = 0
    for i in range(len(alphabet)):
        distance += abs(first_stat[(i + shift) % len(first_stat)] - second_stat[i])
    return distance
