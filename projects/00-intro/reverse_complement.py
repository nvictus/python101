"""
Various solutions to the reverse complement problem, in roughly increasing 
degree of Pythonicity.

"""

def reverse_complement(seq):
    # Iterate over the sequence in reverse by indexing and create a list of
    # complementary bases.
    rc_list = []
    for i in range(len(seq)-1, -1, -1):
        base = seq[i].lower()
        if base == 'a':
            comp = 't'
        elif base == 't':
            comp = 'a'
        elif base == 'g':
            comp = 'c'
        elif base == 'c':
            comp = 'g'
        else:
            comp = base
        rc_list.append(comp)

    # Convert the list into a string by incremental concatenation.
    rc = ''
    for base in rc_list:
        rc += base

    return rc


def reverse_complement(seq):
    # Iterate over the sequence and create a list of complementary bases.
    rc_list = []
    for base in seq.lower():
        if base == 'a':
            comp = 't'
        elif base == 't':
            comp = 'a'
        elif base == 'g':
            comp = 'c'
        elif base == 'c':
            comp = 'g'
        else:
            comp = base
        rc_list.append(comp)

    # Reverse the list in-place.
    rc_list.reverse()

    # Convert the list into a string by incremental concatenation.
    rc = ''
    for base in rc_list:
        rc += base

    return rc


def reverse_complement(seq):
    # Iterate over the sequence and create a list of complementary bases.
    rc_list = []
    for base in seq.lower():
        if base == 'a':
            comp = 't'
        elif base == 't':
            comp = 'a'
        elif base == 'g':
            comp = 'c'
        elif base == 'c':
            comp = 'g'
        else:
            comp = base
        rc_list.append(comp)

    # Reverse the list in-place.
    rc_list.reverse()

    # Convert the list into a string using the `join` method.
    rc = ''.join(rc_list)

    return rc


def reverse_complement(seq):
    # Iterate over the sequence in reverse by using the `reversed` builtin and 
    # create a list of complementary bases.
    rc_list = []
    for base in reversed(seq.lower()):
        if base == 'a':
            comp = 't'
        elif base == 't':
            comp = 'a'
        elif base == 'g':
            comp = 'c'
        elif base == 'c':
            comp = 'g'
        else:
            comp = base
        rc_list.append(comp)

    # Convert the list into a string using `join`.
    rc = ''.join(rc_list)

    return rc


def reverse_complement(seq):
    # Make a complementary base lookup table.
    complement = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G',
    }

    # Create the reverse complement list.
    # Use try-except to handle non-canonical bases (in this case, N's).
    rc_list = []
    for base in reversed(seq.upper()):
        try:
            comp = complement[base]
        except KeyError:
            comp  = base
        rc_list.append(comp)

    # Convert to a string using `join`.
    rc = ''.join(rc_list)

    return rc


def reverse_complement(seq):
    # Complementary base lookup table
    complement = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G',
    }

    # Create the reverse complement list.
    # Use `dict.get` instead of try-except.
    rc_list = []
    for base in reversed(seq.upper()):
        comp = complement.get(base, base)
        rc_list.append(comp)

    # Convert to a string using `join`.
    rc = ''.join(rc_list)

    return rc


def reverse_complement(seq):
    # Complementary base lookup table
    complement = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G',
    }
    
    # Use a list comprehension!
    rc_list = [complement.get(base, base) for base in reversed(seq)]
    return ''.join(rc_list)


def reverse_complement(seq):
    # Complementary base lookup table
    complement = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G',
    }
    
    # Even better: pass a generator comprehension to `join`!
    return ''.join(complement.get(base, base) for base in reversed(seq))



# The following are probably too terse, at the expense of readability.
def reverse_complement(seq):
    return ''.join({'A': 'T', 'T': 'A','G': 'C', 'C': 'G',
        }.get(base, base) for base in reversed(seq))

reverse_complement = lambda seq: ''.join({'A': 'T', 'T': 'A','G': 'C', 'C': 'G'}.get(base, base) for base in reversed(seq))

