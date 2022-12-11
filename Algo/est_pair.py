def est_pair(n):
    if n == 0:
        return True
    elif n == 1:
        return False
    else:
        return est_pair(n - 2)


print(est_pair(1995))
