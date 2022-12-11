def fibo_suite(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibo_suite(n - 1) + fibo_suite(n - 2)


print(fibo_suite(int(input("Donner un entier: "))))
