
import sys


def checkMapping(s1, s2):
    """
    This method takes two strings and checks for a one-to-one mapping
    param s1: Holds the first string
    param s2: Holds the second string
    return: True if there is a one-to-one mapping, False otherwise
    """

    return False

if __name__=="__main__":
    # try block makes sure there are at least two arguments
    try:
        s1 = sys.argv[1] # holds first argument as a s1
        s2 = sys.argv[2] # holds second argument as a s2
    except IndexError:
        print("Not enough arguments")
