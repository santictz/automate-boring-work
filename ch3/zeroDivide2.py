def spam(divideBy):
    return 42 / divideBy
try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1)) #Once exception throwed, the program will not continue in the try
except ZeroDivisionError:
    print('Invalid argument')