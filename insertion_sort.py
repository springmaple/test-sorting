def insertion_sort(ls):
    """Standard insertion sort"""
    for i in range(1, len(ls)):
        v, j = ls[i], i - 1
        while j >= 0 and ls[j] > v:
            ls[j + 1] = ls[j]
            j -= 1
        ls[j + 1] = v


if __name__ == "__main__":
    import timeit
    print(timeit.timeit(lambda: insertion_sort([5, 3, 1, 2, 6, 9]), number=1_000_000))
