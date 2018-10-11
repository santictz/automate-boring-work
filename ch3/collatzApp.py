import collatzSequence
print('Please enter a number')
while True:
    try:
        number = int(input())
        break
    except ValueError:
        print('Invalid argument, please enter a number')


