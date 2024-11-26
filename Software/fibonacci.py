numbersOfInputs = int(input())

numbers = []

for i in range(numbersOfInputs):
    numbers.append(int(input()))


maximum = max(numbers)


def fibon(num):
    if num in numbers:

    if num == 1: return 0
    if num == 2: return 1
    return fibon(num-1)+fibon(num-2)

print(fibon(maximum))