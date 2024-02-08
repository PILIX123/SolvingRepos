from multiprocessing import Pool
import itertools


def f(args):
    a, b = args
    if (0.1494 < a/b < 0.15):
        return (a, b)


l1 = [53]
l2 = [320.00 + i * 0.01 for i in range(int((400.00-320.00) / 0.01))]

if __name__ == "__main__":
    with Pool(7) as p:
        ttt = p.map(f, itertools.product(l1, l2))
        print([t for t in ttt if t is not None])
