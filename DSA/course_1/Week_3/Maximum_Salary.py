from functools import cmp_to_key


def compare(a, b):
  aFirst = int(str(a) + str(b))
  bFirst = int(str(b) + str(a))
  return bFirst - aFirst


def Maximum_Salary(numbers_str):
    number_int = list(map(int, numbers_str))

    result = [str(numbers_str) for numbers_str in sorted(number_int, key=cmp_to_key(compare))]
    ans = ''.join(result)
    return ans
    

if __name__ == '__main__':
    n = input()
    numbers = list(input().split())
    print(Maximum_Salary(numbers))
