def Func(x):
    return 2 ** (x * -1) - (10 - 0.5 * x ** 2)

def main():
    while b - a > eps:
        a, b, eps = map(int, input().split())
        c = (a + b) / 2
        if Func(a) * Func(c) < 0:
            b = c
        else:
            a = c
    x = (a + b) / 2
    delta = (b - a) / 2
    print(x, delta)

if __name__ == "__main__":
    main()