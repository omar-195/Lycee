def inver1(ch):
    if len(ch) == 1 or len(ch) == 0:
        return ch
    else:
        return ch[len(ch)-1] + inver1(ch[:len(ch)-1])


def inver2(ch):
    if len(ch) == 1 or len(ch) == 0:
        return ch
    else:
        return inver2(ch[1:]) + ch[0]


def inver3(ch, n, ch2):
    if n < 0:
        return ch2
    # elif n == 1:
        # ch2 += ch[0]
        # return ch2
    else:
        ch2 += ch[n]+inver3(ch, n-1, ch2)
        return ch2


print(inver3("MohsenImcheIr9ad", len("MohsenImcheIr9ad")-1, ""))
