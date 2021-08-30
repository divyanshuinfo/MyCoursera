def filler(num):
    while len(num) < 4:
        num += num[-1]
    return num


def solution(numbers):
    numbers.sort(key=filler, reverse=True)

    return ''.join(numbers)


n = input()
numbers = list(input().split())

print(solution(numbers))
