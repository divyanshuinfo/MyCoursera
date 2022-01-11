from math import inf


def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return sequence


def recur(n):
    steps = []
    steps.append(n)

    while n > 0:
        first_value = inf
        second_value = inf
        third_value = inf
        first_value2 = inf
        second_value2 = inf
        third_value2 = inf
        if n % 3 == 0:
            first_value = n // 3
            first_value2 = len(optimal_sequence(first_value))

        if n % 2 == 0:
            second_value = n // 2
            second_value2 = len(optimal_sequence(second_value))

        if first_value == inf and second_value == inf:
            n = n - 1
            steps.append(n)
            continue
        else:
            third_value = n - 1
            third_value2 = len(optimal_sequence(third_value))

        d = min(first_value2, second_value2, third_value2)

        if d == second_value2:
            steps.append(second_value)
            n = second_value
        elif d == first_value2:
            steps.append(first_value)
            n = first_value
        elif d == third_value2:
            steps.append(third_value)
            n = third_value

    return len(steps)-2, reversed(steps[:-1])


def recur2(n):
    steps = []
    good_solution = optimal_sequence(n)
    for i in range(len(good_solution)-1):
        g = good_solution[i]
        v1, v2, v3 = inf, inf, inf
        a1, a2, a3 = inf, inf, inf
        b1, b2, b3 = inf, inf, inf
        v1 = g - 1
        a1 = optimal_sequence(v1)
        b1 = len(a1)
        if g % 3 == 0:
            v2 = g // 3
            a2 = optimal_sequence(v2)
            b2 = len(a2)
        if g % 2 == 0:
            v3 = g // 2
            a3 = optimal_sequence(v3)
            b3 = len(a3)
            
        d = min(b1, b2, b3)
        if d == b2 and v2 != good_solution[i+1]:
            good_solution[i+1:] = optimal_sequence(v2)
        elif d == b3 and v3 != good_solution[i+1]:
            good_solution[i+1:] = optimal_sequence(v3)
        elif d == b1 and v1 != good_solution[i+1]:
            good_solution[i+1:] = optimal_sequence(v1)
        
    return len(good_solution), reversed(good_solution)
    

def compute(n):

    a, b = recur2(n)
    return [a, list(b)]


if __name__ == "__main__":
    n = int(input())
    a, b = compute(n)
    print(a)
    for g in b:
        print(g, end=" ")
