from collections import defaultdict

def has_sum(numbers, target):
    for i in range(len(numbers)-1):
        for j in range(i, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return True
    else:
        return False

def has_sum_dict(numbers, target):
    d = defaultdict(int)
    for n in numbers:
        d[n] += 1
    for n in d:
        if n == target/2:
            if d[n] >= 2:
                return True
        elif (target - n) in d:
            return True
    else:
        return False
