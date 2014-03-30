def is_decreasing(seq):

    for x,y in zip(seq, seq[1:]):
        if x <= y:
            return False
    return True