from random import randint  # use randint(a, b) to generate a random number between a and b # noqa

number = randint(1, 10)  # store random number in here, each time through
i = 0  # i should be incremented by one each iteration

while number != 5:
    number = randint(1, 10)
    i += 1