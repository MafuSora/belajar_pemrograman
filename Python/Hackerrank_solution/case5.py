if __name__ == '__main__':
    n = int(raw_input())
    for i in range(0, n, 1):
        if n % 2 == 1:
            print(i*i)
        elif n % 2 == 0:
            print(i)
