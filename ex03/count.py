import string
import sys


def text_analyzer(Givenstring=""):
    '''This function counts the number of upper characters, lower characters, punctuation and spaces in a given text.'''
    text = Givenstring
    while(True):
        if (text==""):
            print("No Text Given")
        elif (not isinstance(text, str)):#is a string
            print("AssertionError: argument is not a string")
            break
        else:
            space = 0 #space number
            upper = 0 #upperCase number
            lower = 0 #lowerCase number
            puncm = 0 #punctuam marks number
            i = 0
            while(i < len(text)):
                if (text[i].isalpha() and text[i].isupper()):
                    upper += 1
                elif (text[i].isalpha() and text[i].islower()):
                    lower += 1
                elif (text[i] in string.punctuation):
                    puncm += 1
                elif (text[i] == ' '):
                    space += 1
                i+=1
            print("The text contains ", i, " character(s):\n-",
                  upper, " upper letter(s)\n-",
                  lower, " lower letter(s)\n-",
                  puncm, " punctuation mark(s)\n-",
                  space, " space(s)")
            break
        text = input(">>>")

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        text_analyzer("")
    else:
        text_analyzer(sys.argv[1])