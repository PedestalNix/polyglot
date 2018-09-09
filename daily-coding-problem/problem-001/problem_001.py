def has_sum(numbers, target):
    for i in range(len(numbers)-1):
        for j in range(i, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return True
    else:
        return False

def has_sum_dict(numbers, target):
    d = {}
    for i, n in enumerate(numbers):
        d[n] = d.get(n, []).append(i)
    for n in d:
        if n == target/2 and len(d[n]) >= 2:
            return True
        else:
            if (target - n) in d:
                return True
    else:
        return False
