def DivisibilitePar9(n):
    n = str(n)
    s = 0
    while n != "":
        s = s + int(n[0])
        n = n[1:]
        if s >= 9:
            s = s - 9
    return s == 0


def DivisiblePar9Recursive(n, s):
    if n != "":
        s = s + int(n[0])
        if s >= 9:
            s = s - 9
        return DivisiblePar9Recursive(n[1:], s)
    else:
        return s == 0


n = int(input("Donner un entier: "))
if DivisibilitePar9(n):
    print(n, "est divisible par 9")
else:
    print(n, "n'est pas divisible par 9")
# Recursive
# if DivisiblePar9Recursive(str(n), 0):
    # print(n, "est divisible par 9")
# else:
    # print(n, "n'est pas divisible par 9")
