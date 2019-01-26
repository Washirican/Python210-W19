#----------------------------------------------------------------#
# Title: Pushups
# Change Log: (Who, When, What)
# D.Rodriguez, 2019-01-13, New file 
#----------------------------------------------------------------#

# Given a string, return a new string where the first and last chars have been exchanged.
# front_back('code') → 'eodc'
# front_back('a') → 'a'
# front_back('ab') → 'ba'

def front_back(str):
# print(str)
    if len(str) <= 0:
        return ""
    else:
        myList = list(str)
        # print(myList)
        # print(len(myList))
        #
        # print(myList[0])
        # print(myList[len(myList)-1])

        temp = myList[0]
        myList[0] = myList[len(myList)-1]
        myList[len(myList) - 1] = temp
    
        # print(myList)
        str2 = ""
        for x in myList:
            # print(x)
            str2 = str2 + x

        return str2

print(front_back('code'))
print(front_back('a'))
print(front_back('ab'))