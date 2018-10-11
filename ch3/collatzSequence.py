def collatz(number):
    if number % 2 == 0:
        return number / 2
    elif number % 2 == 1:
        return (number * 3) + 1

#Ask user to enter a number and validate the input
print('Please enter a number')
while True:
    try:
        userNumber = int(input())
        break
    except ValueError:
        print('Invalid argument, please enter a number')

#Execute collatz function
result = collatz(userNumber)
while True:
    print(result)
    result = int(collatz(result))
    if result == 1:
        print(result)
        break
    