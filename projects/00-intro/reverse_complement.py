"""
Various solutions to the reverse complement problem.

"""

def reverse_complement(seq):
    # Translate the string into its reverse complement
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

    # Convert the list into a string
    rc = ''
    for base in rc_list:
        rc += base

    return rc


def reverse_complement(seq):
    # Translate the string into its complement
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

    # Reverse the list in-place
    rc_list.reverse()

    # Convert the list into a string
    rc = ''
    for base in rc_list:
        rc += base

    return rc


def reverse_complement(seq):
    # Translate the string into its complement
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

    # Reverse the list in-place
    rc_list.reverse()

    # Convert the list into a string
    rc = ''.join(rc_list)

    return rc


def reverse_complement(seq):
    # Translate the string into its reverse complement
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

    # Convert the list into a string
    rc_list = ''.join(rc_list)

    return rc_list


def reverse_complement(seq):
    # Complementary base lookup table
    complement = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G',
    }

    # Translate the string into its reverse complement
    rc_list = []
    for base in reversed(seq.upper()):
        try:
            comp = complement[base]
        except KeyError:
            comp  = base
        rc_list.append(comp)

    # Convert to a string
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

    # Translate the string into its reverse complement
    rc_list = []
    for base in reversed(seq.upper()):
        comp = complement.get(base, base)
        rc_list.append(comp)

    # Convert to a string
    rc_list = ''.join(rc)

    return rc_list


def reverse_complement(seq):
    # Complementary base lookup table
    complement = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G',
    }
    
    # Translate the string into its reverse complement
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
    
    # Translate the string into its reverse complement
    return ''.join(complement.get(base, base) for base in reversed(seq))


def reverse_complement(seq):
    return ''.join({'A': 'T', 'T': 'A','G': 'C', 'C': 'G',
        }.get(base, base) for base in reversed(seq))


reverse_complement = lambda seq: ''.join({'A': 'T', 'T': 'A','G': 'C', 'C': 'G'}.get(base, base) for base in reversed(seq))




