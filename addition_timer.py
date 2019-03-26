import random
import time
import sys
# timeit.timeit("random.sample(range(10,100),2)"
# ,number = 50,setup = 'import random')


def single_addition(start=10, end=100):
    a, b = random.sample(range(start, end), 2)
    return (a, b, a+b)


def one_question(start, end, f=single_addition):
    a, b, sum = f(start, end)
    _initial = time.time()
    x = input(f"provide the sum of {a} and {b}\n")
    try:
        isinstance(int(x), int)
        x = int(x)
    except ValueError:
        sys.exit("wrong value entered")
    _final = time.time()
    return (x == sum, _final - _initial)


def addition_problem(f=single_addition, digits=2):
    if digits == 2:
        start, end = 10, 100
    elif digits == 3:
        start, end = 100, 1000
    else:
        raise ValueError
    a = [one_question(start, end, f) for x in range(10)]
    _correct, _time = map(sum, list(zip(*a)))
    print(f"{_correct} answers took {_time} seconds")
    print(list(zip(*a))[0])


if __name__ == "__main__":
    addition_problem(digits=3)
