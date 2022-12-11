def DivisibilitePar11(n):
    s = 0
    while n != "":
        s = s + int(n[len(n)-2:])
        n = n[:len(n)-2]
        if n == "" and len(str(s)) != 2:
            n = str(s)
            s = 0
    while s >= 11:
        s = s - 11
    return s == 0


def DivisiblePar11Recursive(n, s):
    if n != "":
        s = s + int(n[len(n)-2:])
        n = n[:len(n)-2]
        if n == "" and len(str(s)) != 2:
            n = str(s)
            s = 0
        return DivisiblePar11Recursive(n, s)
    else:
        while s >= 11:
            s = s - 11
        return s == 0


n = int(input("Donner un entier: "))
if DivisibilitePar11(str(n)):
    print(n, "est divisible par 11")
else:
    print(n, "n'est pas divisible par 11")
# Recursive
# if DivisiblePar11Recursive(str(n), 0):
#     print(n, "est divisible par 11")
# else:
#     print(n, "n'est pas divisible par 11")
