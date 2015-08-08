
def word_frequency_table(filepath, outpath=None):
    """
    Counts the number of occurrences of each unique word in a file.

    Input
    -----
    filepath: str
        Path to a text file.
    outpath: str
        File to write statistics to.
        Defaults to printing word frequencies to screen.

    """
    # Create a dictionary to keep a tally of words
    counter = {}

    # Read in the file and count words, removing punctuation
    fh = open(filepath, 'r')
    for line in fh:
        words = line.strip().split()

        for word in words:
            word = word.strip(",.!?\'\"-;:").lower()
            if word:
                try:
                    counter[word] += 1
                except KeyError:
                    counter[word] = 1
    fh.close()

    # Sort the words in decending order of frequency
    word_counts = sorted(counter.items(), key=lambda x: x[1], reverse=True)

    if outpath is None:
        # Print the frequency table to stdout
        for word, number in word_counts:
            print("{}: {}".format(word, number))
    else:
        # Write the frequency table to a file
        # (We could also have used the print function here!)
        f_out = open(outpath, 'w')
        for word, number in word_counts:
            f_out.write("{}: {}\n".format(word, number))  # Note the explicit newline character!
        f_out.close()


if __name__ == '__main__':
    import os

    if not os.path.exists('raven.txt'):
        import requests
        r = requests.get('https://raw.githubusercontent.com/nvictus/python101/master/projects/00-intro/raven.txt')
        with open('raven.txt', 'w') as f:
            f.write(r.text)

    word_frequency_table('raven.txt', outpath='raven-wordcount.txt')
        

