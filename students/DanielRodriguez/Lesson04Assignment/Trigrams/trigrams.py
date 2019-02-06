# -------------------------------------------------------------------------------------------------------------------- #
# Title: 
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-02-05, Initial release
# -------------------------------------------------------------------------------------------------------------------- #

# -- Data -- #
str_sentence = 'I wish I may I wish I might'
lst_words = str_sentence.split()

print(lst_words)
lst_word_pairs = []
for i in range(len(lst_words) - 1):
    # print(i, lst_words[i: i + 2], lst_words[i], ' '.join((lst_words[i], lst_words[i + 1])))
    # print(type(' '.join((lst_words[i], lst_words[i + 1]))))
    if lst_words[i: i + 2] not in lst_word_pairs:
        lst_word_pairs.append(' '.join((lst_words[i], lst_words[i + 1])))
        # print(type(lst_word_pairs))
# print(lst_word_pairs)
for pairs in lst_word_pairs:
    print(pairs)

# -- Processing -- #
# perform tasks


# -- Presentation (Input/Output) -- #
# get user input
# send program output