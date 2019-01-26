# ----------------------------------------------------------------#
# Title: Push ups
# Change Log: (Who, When, What)
# D.Rodriguez, 2019-01-13, New file 
# ----------------------------------------------------------------#

# Given a non-empty string like "Code" return a string like "CCoCodCode".
# string_splosion('Code') → 'CCoCodCode'
# string_splosion('abc') → 'aababc'
# string_splosion('ab') → 'aab'


# TODO: Don't understand requirements
def string_splosion(str):
    
    my_list = list(str)
    my_string = ""
    print(my_list)

    for x in range(len(my_list)):
        print (x, my_list[x])
        # for y in range(x):
        #     my_string = my_string + my_list[y]

    return 0


print(string_splosion('Code'))
# print(string_splosion('abc'))
# print(string_splosion('ab'))

