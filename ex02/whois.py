import sys
#check if a number is even or odd
len = len(sys.argv)
if (len == 1):
    sys.exit()
elif ( len > 2):
    print('AssertionError: more than one argument are provided')
    sys.exit()
elif (not sys.argv[1].isdigit()):
    print('AssertionError: argument is not an integer')
    sys.exit()
nb = sys.argv[1]

if nb == '0':
    print('I\'m Zero.')
elif (int(nb) % 2 != 0):
    print("I'm Odd.")
else:
    print("I'm Even.")