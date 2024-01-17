from timeit import timeit
from time import time_ns as time


def check_submatrix(mosaic, x, y, motif):
    # Check if the submatrix starting from (x, y) matches the motif
    for i in range(len(motif)):
        for j in range(len(motif[0])):
            if motif[i][j] != 0 and mosaic[x + i][y + j] != motif[i][j]:
                return False
    return True


def find_motif_occurrences(mosaic, motif):
    n, m = len(mosaic), len(mosaic[0])
    r, c = len(motif), len(motif[0])
    occurrences = []

    for i in range(n - r + 1):
        for j in range(m - c + 1):
            if check_submatrix(mosaic, i, j, motif):
                # Adjusting to 1-based indexing
                occurrences.append((i + 1, j + 1))

    return occurrences


if __name__ == "__main__":
    # ... (Your input code for motif and mosaic here) ...
    # no of rows and cols in motif
    print("Enter the number of rows and columns of motif:", end=" ")
    r, c = map(int, input().split())
    # motif input
    motif = []
    for i in range(r):
        print(f"Enter the colors in row {i+1}:", end=" ")
        temp = list(map(int, input().split()))
        motif.append(temp)

        # no of rows and columns in mosaic
    print("Enter the number of rows and columns of mosaic:", end=" ")
    n, m = map(int, input().split())

    # mosaic input
    mosaic = []
    for i in range(n):
        print(f"Enter the colors in row {i+1}:", end=" ")
        temp = list(map(int, input().split()))
        mosaic.append(temp)

        # Example usage:
    a = time()
    occurrences = find_motif_occurrences(mosaic, motif)
    # time_taken = timeit(lambda: find_motif_occurrences(mosaic, motif))
    # print("Time taken to find motif occurrences:", time_taken, "seconds")
    print("Time taken to find motif occurrences:", time() - a, "seconds")
    print("The number of motif occurrences in mosaic are:", len(occurrences))
    print("And their starting positions are:")
    for x, y in occurrences:
        print(x, y)
