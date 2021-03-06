import copy
from random import Random

from prefixes import *


def completed_number(prefix, length, generator) -> str:

    while len(prefix) < (length - 1):
        digit = str(generator.choice(range(10)))
        prefix.append(digit)
    numbers_sum = 0
    pos = 0
    reversed_prefix = []
    reversed_prefix.extend(prefix)
    reversed_prefix.reverse()

    while pos < length - 1:
        odd = int(reversed_prefix[pos]) * 2
        if odd > 9:
            odd -= 9
        numbers_sum += odd
        if pos != (length - 2):
            numbers_sum += int(reversed_prefix[pos + 1])
        pos += 2
    return ''.join(prefix)


def credit_card_number(generator, prefix_list, length):
    prefix = copy.copy(generator.choice(prefix_list))
    result = [completed_number(prefix=prefix, length=length, generator=generator)]
    return ''.join(result)


def generate_random_card_number() -> str:
    generator = Random()
    generator.seed()  # Seed from current time
    return credit_card_number(generator, BIN__PRIVAT_BANK, 16)
