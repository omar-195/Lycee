from numpy import array


def SuiteRebinson(n):
    T = array([0]*10)
    U = 0
    print("U 0", U)
    for i in range(1, n):
        ch = str(U)
        res = ""
        for j in range(len(ch)):
            T[int(ch[j])] = T[int(ch[j])] + 1
        for k in range(9, -1, -1):
            if T[k] != 0:
                res = res + str(T[k]) + str(k)
        U = str(res)
        print("U"+str(i) + " = "+U)


SuiteRebinson(int(input("Donner n: ")))
