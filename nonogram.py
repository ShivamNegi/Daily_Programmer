import numpy as np


def count_ones(inp, i):
    count = []
    c = 0
    for w in inp[i]:
        if w == '*':
            c += 1
        else:
            if c > 0:
                count.append(c)
            c = 0
    if c > 0:
        count.append(c)
    return count


def printing(rows, cols, max_len_cols, max_len_rows):
    # Printing cols
    narr = []

    for i in range(len(cols)):
        for j in range(max_len_cols - len(cols[i])):
            cols[i].append(0)
        cols[i].reverse()
        narr.append(cols[i])

    narr = np.array(narr)

    for i in range(max_len_cols):
        for j in range(max_len_rows):
            print " ",
        for j in range(len(narr)):
            if narr[j][i] == 0:
                print "  ",
            else:
                if narr[j][i] < 10:
                    print narr[j][i],"",
                else:
                    print narr[j][i],

        print



    for row in rows:
        for i in range(max_len_rows - len(row)):
            print " ",
        for no in row:
            print no,
        print


def main():
    inp = []
    sent = raw_input()

    while sent != '':
        inp.append(list(sent))
        sent = raw_input()

    arr = np.array(inp)
    rows = []
    for i in range(len(arr)):
        rows.append(count_ones(arr, i))

    cols = []
    for i in range(len(arr.transpose())):
        cols.append(count_ones(arr.transpose(), i))

    # Max length of rows, cols

    max_len_rows = 0
    max_len_cols = 0

    for col in cols:
        if len(col) > max_len_cols:
            max_len_cols = len(col)

    for row in rows:
        if len(row) > max_len_rows:
            max_len_rows = len(row)

    printing(rows, cols, max_len_cols, max_len_rows)


if __name__ == '__main__':
    main()
