def Func(x):
    return 2 ** (x * (-1)) - (10 - 0.5 * x ** 2)

def main():
    x_0, eps, q = map(int, input().split())
    a = eps * (1 - q) / q
    x = x_0
    while abs(p) > a:
        y = Func(x)
        p = x - y
        x = y
    print(x)

if __name__ == "__main__":
    main()