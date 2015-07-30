'https://raw.githubusercontent.com/nvictus/python101/master/raven.txt'



def word_frequency_table(filepath):
    """
    Counts the number of occurrences of each unique word
    in a file.

    Input
    -----
    filepath: str
        Path to a text file.

    Output
    ------
    Prints words and their frequencies.

    """

    # Create a dictionary to keep a tally of words
    counter = {}

    # Read in the file and count words, removing punctuation
    fh = open(filepath, 'r')
    for line in fh:
        words = line.strip().split()

        for word in words:
            word = word.strip(",.!?\'\"-;:").lower()
            try:
                counter[word] += 1
            except KeyError:
                counter[word] = 1
    fh.close()

    # Sort the words in decending order of frequency
    word_counts = sorted(counter.items(), key=lambda x: x[1], reverse=True)

    # Write the frequency table to a file
    f_out = open('word_count.txt', 'w')
    for word, number in word_counts:
        f_out.write("{}: {}\n".format(word, number))
    f_out.close()







if __name__ == '__main__':
    word_frequency_table('raven.txt')
        




