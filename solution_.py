from timeit import timeit
from time import time
import numpy as np

# rq, cq = map(int, input().split())
# motif = np.array([list(map(int, input().split())) for _ in range(rq)])

# rp, cp = map(int, input().split())
# mosaic = np.array([list(map(int, input().split())) for _ in range(rp)])
rq, cq = 2, 2
motif = np.array([[1, 0], [0, 1]])
rp, cp = 3, 4
mosaic = np.array([[1, 2, 1, 2], [2, 1, 1, 1], [2, 2, 1, 3]])

# print(motif)
# print(mosaic)


def find_occurrences(motif, mosaic):
    possibilities = 0
    matching_pos = []

    for i in range(rp - rq + 1):
        for j in range(cp - cq + 1):
            mosaic_part = mosaic[i:i + rq, j:j + cq]
            # print(i, j, mosaic_part)
            if (np.where((motif == mosaic_part) | motif == 0, motif, mosaic_part) == motif).all():
                matching_pos.append((i, j))
                possibilities += 1

    return possibilities, matching_pos


a = time()
possibilities, matching_pos = find_occurrences(motif, mosaic)
# timetaken = timeit(lambda: find_occurrences(motif, mosaic))
# print("Time taken to find motif occurrences:", timetaken, "seconds")
print("Time taken to find motif occurrences:", time() - a, "seconds")
print(possibilities)
for i, j in matching_pos:
    print(i + 1, j + 1)
