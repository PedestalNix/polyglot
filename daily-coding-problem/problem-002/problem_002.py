import functools
from operator import mul

def solution(numbers):
    product = functools.reduce(mul, numbers)
    return [product//numbers[i] if numbers[i] != 0
                               else functools.reduce(mul, numbers[:i] + numbers[i+1:])
            for i in range(len(numbers))]

def solution_beta(numbers):
    return [functools.reduce(mul, numbers[:i] + numbers[i+1:]) for i in range(len(numbers))]
