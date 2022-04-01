def unknown_sort(ls):

    def find_max_index(sub_ls):
        i_, k_ = 0, sub_ls[0]
        for index, j_ in enumerate(sub_ls):
            if k_ < j_:
                i_, k_ = index, j_
        return i_

    for i in reversed(range(1, len(ls))):
        v = find_max_index(ls[0:i + 1])
        ls[v], ls[i] = ls[i], ls[v]

    return ls

if __name__ == "__main__":
    import timeit
    print(timeit.timeit(lambda: unknown_sort([5, 3, 1, 2, 6, 9]), number=1_000_000))

