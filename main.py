import math


def is_prime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True


def crypto(data):
    primes = []
    for index, sym in enumerate(data):
        if is_prime(index) and sym != ' ':
            primes.append(sym)

    return primes


print(crypto(('0Zzz', '1Xxx', '2Www', '3Kkk', '4Fff', '5Qqq', '6Yyy', '7Iii', '8Ooo', '9Nnn', '10Ccc')))
print(crypto('This is a text with some words in it!'))
print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(crypto({11: 'A', 22: 'B', 33: 'C', 44: 'D', 55: 'E', 66: 'F', 77: 'G', 88: 'H', 99: 'J'}))
