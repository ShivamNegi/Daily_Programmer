from copy import deepcopy


def input_arr(arr, n):
    for i in range(n):
        li = raw_input().split()
        a = [x for x in li]
        arr.append(a)


def display(arr):
    print
    for a in arr:
        for no in a:
            print no, "  ",
        print


def rotate90(arr):
    dup = deepcopy(arr)
    l = len(arr)
    for i in range(l):
        for j in range(l):
            arr[j][l - i - 1] = dup[i][j]

if __name__ == '__main__':
    n = int(raw_input("Enter n: "))
    arr = []
    input_arr(arr, n)
    display(arr)
    print "Rotated 90"
    rotate90(arr)
    display(arr)
    print "Rotated 180"
    rotate90(arr)
    display(arr)
