t = int(input())


for i in range(t):
    n = input()
    if n.find(".") == -1:
        print(False)
        continue
    try:
        if float(n):
            print(True)
    except ValueError:
        print(False)
