#----------------------------------------------------------------#
# Title: Pushups
# Change Log: (Who, When, What)
# D.Rodriguez, 2019-01-13, New file 
#----------------------------------------------------------------#

# Given a string, return a new string where "not " has been added to the front. 
# However, if the string already begins with "not", return the string unchanged.
# not_string('candy') → 'not candy'
# not_string('x') → 'not x'
# not_string('not bad') → 'not bad'

def not_string(str):
    if not str.startswith("not"):
        return "not " + str
    else:
        return str

  
print(not_string('candy'))
print(not_string('x'))
print(not_string('not bad'))