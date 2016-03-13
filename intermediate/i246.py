from string import ascii_uppercase as l


def separate(no, d):
    if not no.find('0'):
        li = ""
        for n in no:
            li += d[int(n)]
        print li


def pairdisp(no, d):
    i = 0
    for i in range(len(no) - 1):
        if no[i] != '0':
            li = ""
            flag = True
            for k, n in enumerate(no):
                if k == i:
                    pass
                elif k < len(no) - 1:
                    if no[k + 1] == '0':
                        n = int(no[k]) * 10 + int(no[k + 1])
                        if n > 26:
                            flag = False
                            break
                        else:
                            li += d[int(n)]
                elif k == i + 1:
                    n = int(no[k - 1]) * 10 + int(no[k])
                    if n > 26:
                        flag = False
                        break
                    else:
                        li += d[int(n)]
                else:
                    li += d[int(n)]
            if flag:
                print li


def main():
    no = raw_input()
    d = dict(zip(range(1, 27), l))
    d[0] = ""

    separate(no, d)
    pairdisp(no, d)


if __name__ == '__main__':
    main()
