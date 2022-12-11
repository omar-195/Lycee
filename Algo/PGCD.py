def PGCD(a, b):
    if a == b:
        return a
    else:
        if a > b:
            return PGCD(a-b, b)
        else:
            return PGCD(a, b-a)


print(PGCD(5, 3))
