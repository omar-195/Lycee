def maxChiffre(suite, ch):
    m = 0
    for i in range(len(suite)):
        if m < int(suite[i]) and ch.find(suite[i]) != -1:
            m = int(suite[i])
    return str(m)


def calculeChiffre(ch, m):
    s = 0
    for i in range(len(ch)):
        if ch[i] == m:
            s = s+1
    return str(s)


def RobinsonSuite(n):
    suite = "0"
    for i in range(1, n):
        ch = ""
        for j in range(len(suite)):
            m = maxChiffre(suite, ch)
            ch = calculeChiffre(ch, m)+m
        suite = ch
    return suite


print(RobinsonSuite(3))
