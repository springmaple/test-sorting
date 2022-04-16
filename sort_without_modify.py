def sort_and_return(ls):
    ls_s = []
    for v in ls:
        i = 0
        while i < len(ls_s) and ls_s[i] < v:
            i += 1
        ls_s.insert(i, v)
    return ls_s


if __name__ == "__main__":
    print(sort_and_return([1, 2, 45, 123, 5, 1, 23, 1, 51, 23, ]))
