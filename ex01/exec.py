
import sys

count = len(sys.argv)
print ('number of arguments is: ', count)

#reverse a word characters the world is  's' -1 start from the end and jump with a single character
#:: by default the loop start from the beginnig to the end
def reverse_slicing(s):
    return s[::-1]#::nb, nb of car to jump

if (count < 2):
    print('At least One argument must be given')
    sys.exit()

newReversedText = ""
str = ""

while (count != 1):
    count-=1
    str = sys.argv[count]
    newReversedText += reverse_slicing(str)
    newReversedText += ' '

print(newReversedText.swapcase())#swap upper to lower and lower to upper