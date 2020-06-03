def pizdec(n):
    if n in(1, 2):
        return 1
    return pizdec(n - 1) + pizdec(n - 2)
print(pizdec(20))



