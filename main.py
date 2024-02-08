from multiprocessing import Pool
import itertools


def f(args):
    a, b = args
    if (0.1215 < a/b < 0.1216):
        return (a, b)


l1 = [14.34, 15.34]
l2 = [115.00 + i * 0.01 for i in range(int((130.00-115.00) / 0.01))]

if __name__ == "__main__":
    with Pool(7) as p:
        ttt = p.map(f, itertools.product(l1, l2))
        print([t for t in ttt if t is not None])
