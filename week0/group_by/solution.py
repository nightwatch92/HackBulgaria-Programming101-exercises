from itertools import *

def group_by(func, seq):
    ds = list()
    fs = []
    seq = sorted(seq, key = func)
    for k, g in groupby(seq, func):
        # print(k,g)
        ds.append(list(g))
        fs.append(k)
    # return fs, ds
    dict_ = {}
    for x,y in enumerate(ds):
        dict_.setdefault(x,[]).append(y)
    return dict_