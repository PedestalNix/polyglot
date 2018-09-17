def greatest_sum(numbers):
    if len(numbers) <= 2:
        return max(0, *numbers)
    sums = [0, 0] + numbers[:2]
    for n in numbers[2:]:
        sums.append(max(
            0,       # if n <= 0 and so were previous sums
            n,       # if previous sums were <= 0
            n+sums[1],
            n+sums[2],
            sums[1], # if n < 0 either this
            sums[2], #          or this
        ))
        sums.pop(0)

    return max(sums[-2:])

def main():
    assert greatest_sum([2, 4, 6, 2, 5]) == 13
    assert greatest_sum([5, 1, 1, 5]) == 10
    assert greatest_sum([-1, -2]) == 0
    assert greatest_sum([1, 2]) == 2
    assert greatest_sum([1]) == 1

if __name__ == '__main__':
    main()
