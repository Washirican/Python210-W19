# ----------------------------------------------------------------#
# Title:
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-01-19, Revision notes
# ----------------------------------------------------------------#
# When squirrels get together for a party, they like to have cigars.
# A squirrel party is successful when the number of cigars is between
# 40 and 60, inclusive. Unless it is the weekend, in which case there
# is no upper bound on the number of cigars. Return True if the party
# with the given values is successful, or False otherwise.
#
# cigar_party(30, False) → False
# cigar_party(50, False) → True
# cigar_party(70, True) → True

# -- Data --#
# declare variables and constants


# -- Processing --#
def cigar_party(cigars, is_weekend):
    if is_weekend and cigars >= 40:
        return True
    elif not is_weekend and 40 <= cigars <= 60:
        return True
    else:
        return False


# -- Presentation (Input/Output) --#
print(cigar_party(50, False) )