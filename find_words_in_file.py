punctuation_remove = ",.!?"
punctuation_space = "'"

def find_3_letter_words(filename):
    """
    Find all the 3 letter words starting with a B in a file
    :param filename:
    :return:none
    """
    with open(filename) as f:
        # go line by line
        for line in f:
            # replace punctuation in each line
            for p in punctuation_remove:
                line = line.replace(p,"")
            for p in punctuation_space:
                line = line.replace(p, "")
            words = line.split()
            # iterate over the list of words
            for word in words:
                if len(word) == 3 and word[0].lower()== "b":
                    print(word)

find_3_letter_words("input.txt")