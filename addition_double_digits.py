import random
import time
import sys
 #timeit.timeit("random.sample(range(10,100),2)",number = 50,setup = 'import random')

def double_digit_addition():
    a,b = random.sample(range(10,100),2)
    return (a,b,a+b)

def one_question(f = double_digit_addition):
    a,b,sum = f()
    _initial = time.time()
    x = input(f"provide the sum of {a} and {b}\n")
    try:
        isinstance(int(x),int)
        x = int(x)
    except:
        sys.exit()
    _final = time.time()
    return (x==sum,_final-_initial)

def addition_problem(f = double_digit_addition):
    a=[one_question(f) for x in range(10)]
    _correct,_time = map(sum,list(zip(*a)))
    print (f"{_correct} answers took {_time} seconds")
    print(list(zip(*a))[0])

if __name__ == "__main__":
    addition_problem()
