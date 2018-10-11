import sys
while True:
    print('Type ex to exit')
    response = input()
    if response == 'ex':
        sys.exit() #the only way to exit this program is with the exit function of sys module
    print('You typed ' + response + '.')