# -------------------------------------------------------------------------------------------------------------------- #
# Title: Triagrams
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-02-05, Initial release
# D. Rodriguez, 2019-02-14, Added string post-processing
# -------------------------------------------------------------------------------------------------------------------- #

import random
# import string

# -- Data -- #
# str_data_raw = 'I wish I may I wish I might'

# str_data_raw = 'As I '\
#            'passed the well-remembered door, which must always be associated '\
#            'in my mind with my wooing, and with the dark incidents of the '\
#            'Study in Scarlet, I was seized with a keen desire to see Holmes '\
#            'again, and to know how he was employing his extraordinary powers'

# str_data_raw = 'One night--it was on the twentieth of March, 1888--I was ' \
#             'returning from a journey to a patient (for I had now returned to '\
#             'civil practice), when my way led me through Baker Street. As I '\
#             'passed the well-remembered door, which must always be associated '\
#             'in my mind with my wooing, and with the dark incidents of the '\
#             'Study in Scarlet, I was seized with a keen desire to see Holmes '\
#             'again, and to know how he was employing his extraordinary powers. '\
#             'His rooms were brilliantly lit, and, even as I looked up, I saw '\
#             'his tall, spare figure pass twice in a dark silhouette against '\
#             'the blind. He was pacing the room swiftly, eagerly, with his head '\
#             'sunk upon his chest and his hands clasped behind him. To me, who '\
#             'knew his every mood and habit, his attitude and manner told their '\
#             'own story. He was at work again. He had risen out of his '\
#             'drug-created dreams and was hot upon the scent of some new '\
#             'problem. I rang the bell and was shown up to the chamber which '\
#             'had formerly been in part my own.'

# str_data_raw = "Between us there was, as I have already said somewhere, the bond of " \
#            "the sea. Besides holding our hearts together through long periods of " \
#            "separation, it had the effect of making us tolerant of each other's " \
#            'yarns--and even convictions. The Lawyer--the best of old fellows--had, '\
#            'because of his many years and many virtues, the only cushion on deck,'\
#            'and was lying on the only rug. The Accountant had brought out already a '\
#            'box of dominoes, and was toying architecturally with the bones. Marlow '\
#            'sat cross-legged right aft, leaning against the mizzen-mast. He had '\
#            'sunken cheeks, a yellow complexion, a straight back, an ascetic aspect, '\
#            'and, with his arms dropped, the palms of hands outwards, resembled an '\
#            'idol. The director, satisfied the anchor had good hold, made his way '\
#            'aft and sat down amongst us. We exchanged a few words lazily. Afterwards '\
#            'there was silence on board the yacht. For some reason or other we did '\
#            'not begin that game of dominoes. We felt meditative, and fit for nothing '\
#            'but placid staring. The day was ending in a serenity of still and '\
#            'exquisite brilliance. The water shone pacifically; the sky, without a '\
#            'speck, was a benign immensity of unstained light; the very mist on the '\
#            'Essex marsh was like a gauzy and radiant fabric, hung from the wooded '\
#            'rises inland, and draping the low shores in diaphanous folds. Only the '\
#            'gloom to the west, brooding over the upper reaches, became more sombre '\
#            'every minute, as if angered by the approach of the sun.'


# # Gets random index - Not needed if using random.choice(list)
# def random_int(upper):
#     return random.randint(0, upper - 1)


# Remove punctuation from input string
# TODO: Import text file
def import_book():
    filename = 'sherlock - excerpt.txt'
    objFile = open(filename, 'r')
    str_data_raw = objFile.read()
    objFile.close()
    return str_data_raw


def remove_punctuation(str_data_raw):
    str_data = str_data_raw\
        .replace('.', ' ')\
        .replace(',', ' ')\
        .replace('--', ' ')\
        .replace(';', ' ') \
        .replace('"', ' ') \
        .replace(':', ' ')

    # TODO: Use .tranlate() method to clean up input string
    # str_data.translate()
    return str_data


def build_triagram(str_data):
    lst_words = str_data.split()
    dict_triagram = {}
    lst_all_keys = []

    # TODO: Use tuples instead of strings for dictionary keys?
    # Build Triagram dictionary
    for i in range(len(lst_words) - 2):
        # Generate dictionary keys
        str_key = ' '.join((lst_words[i], lst_words[i + 1]))
        lst_value = lst_words[i + 2]

        # If new key (i.e. word pairing)
        if str_key not in dict_triagram.keys():
            dict_triagram[str_key] = [lst_value]

        # Existing word pairing
        else:
            dict_triagram[str_key].append(lst_value)

    # Get all keys in a list for easier random selection via index
    for key in dict_triagram.keys():
        lst_all_keys.append(key)

    # Begin building triagram by randomly selecting initial key word pair and value
    # Use random.choice(list) to select initial values instead of calling function
    str_key = random.choice(lst_all_keys)
    # int_key_id = random_int(len(lst_all_keys))
    # str_key = lst_all_keys[int_key_id]

    # int_val_id = random_int(len(dict_triagram[str_key]))
    # str_value = dict_triagram[str_key][int_val_id]
    str_value = random.choice(dict_triagram[str_key])

    # Initial result string
    str_result = str_key + ' ' + str_value
    str_key = ' '.join(str_result.split()[-2:])

    # Looping until word pair is not a dictionary key
    # TODO: Loop until pre-defined length of text
    try:
        while dict_triagram[str_key]:
            # Use last 2 words of result string as key word pair for next iteration
            # Randomly select Value
            # int_val_id = random_int(len(dict_triagram[str_key]))
            # str_value = dict_triagram[str_key][int_val_id]
            str_value = random.choice(dict_triagram[str_key])

            # Next string
            str_result += ' ' + str_value
            str_key = ' '.join(str_result.split()[-2:])
    except KeyError:
        pass # print('The substring ', str_key, 'is not a key.')

    return str_result, str_key


def word_wrapper(str_data):
    int_sentence_length = 10
    lst_data = str_data.split()
    str_result = ''
    for i in range(0, len(lst_data), int_sentence_length):
        str_result += ' '.join(lst_data[i: i + int_sentence_length]) + '\n'

    return str_result


if __name__ == "__main__":
    str_data_raw = import_book()
    str_data = remove_punctuation(str_data_raw)
    str_result, str_key = build_triagram(str_data)

    # Print resulting triagram
    print('Dictionary key "', str_key, '" could not be found. Ending triagram processing.\n', sep='')
    print('Resulting Text:')

    str_final = word_wrapper(str_result)
    print(str_final.capitalize())
