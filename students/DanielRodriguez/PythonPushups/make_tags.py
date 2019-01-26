# ----------------------------------------------------------------#
# Title: Pushups
# Change Log: (Who, When, What)
# D.Rodriguez, 2019-01-13, New file
# ----------------------------------------------------------------#

# The web is built with HTML strings like "<i>Yay</i>" which draws
# Yay as italic text. In this example, the "i" tag makes <i> and </i>
# which surround the word "Yay". Given tag and word strings, create the
# HTML string with tags around the word, e.g. "<i>Yay</i>".
#

# make_tags('i', 'Yay') → '<i>Yay</i>'
# make_tags('i', 'Hello') → '<i>Hello</i>'
# make_tags('cite', 'Yay') → '<cite>Yay</cite>'


def make_tags(tag, word):
    return "<" + tag + ">" + word + "</" + tag + ">"


print(make_tags('i', 'Hello'))

