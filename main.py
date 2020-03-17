import sys
 
def checkMapping(s1, s2):
    """
    This method takes two strings and checks for a one-to-one mapping 
    param s1: Holds the first string
    param s2: Holds the second string
    return: True if there is a one-to-one mapping, False otherwise
    """
    
    dict1 = {} # dict to hold each character in s1 as a key with the number of occurences as the value
    dict2 = {} # dict to hold each character in s2 as a key with the number of occurences as the value
 
    # for loops to iterate through s1 and s2, and populate dict1 and dict2
    for letter in s1:
        if letter not in dict1:
            dict1[letter] = 1
        else:
            dict1[letter] += 1
    for letter in s2:
        if letter not in dict2:
            dict2[letter] = 1
        else:
            dict2[letter] += 1
 
    # dictionary to hold number of occurences, in dict2, as a key
    # Example: food
    #           dict2 = { 'f': 1 , 'o': 2, 'd': 1 }
    #           dict_count2 = { '1': 2, '2': 1}
    dict_count2 = {}
    dict2_max = 0 # holds maximum number of occurences in dict2
 
    # for loop to iterate through dict2, and populate dict_count2
    for letter in dict2:
        if dict2[letter] > dict2_max:
            dict2_max = dict2[letter]
        if dict2[letter] not in dict_count2:
            dict_count2[dict2[letter]] = [letter]
        else:
            dict_count2[dict2[letter]].append(letter)
 
    for letter in dict1:
        corr_exist = False # condition to make sure 'letter' is mapped 
        # for loop to check closest map match based off 'letter' and its number of occurences
        for i in range(dict1[letter], dict2_max+1):
            if i in dict_count2:
                temp = dict_count2[i].pop(0) # holds letter that is mapped and removed
                # conditional to delete a key if its list if empty
                if not dict_count2[i]:
                    dict_count2.pop(i)
                # conditionals to create a new key for the removed letter based off the number of occurences left
                if i-dict1[letter] not in dict_count2:
                    dict_count2[i-dict1[letter]] = [temp]
                else:
                    dict_count2[i-dict1[letter]].append(temp)
                corr_exist = True
                break
        # conditional to check if 'letter' is mapped
        if not corr_exist:
            return False
    
    # the method can only reach this far if all letters in s1 were mapped to letters in s2
    return True
 
if __name__=="__main__":
    # try block makes sure there are at least two arguments
    try:
        s1 = sys.argv[1] # holds first argument as a s1
        s2 = sys.argv[2] # holds second argument as a s2
    except IndexError:
        print("Not enough arguments")
        exit(0)
 
    if checkMapping(s1,s2):
        print("true")
    else:
        print("false")