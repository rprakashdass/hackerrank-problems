if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    lar, slar = float('-inf'), float('-inf')
    for a in arr:
        if a > lar:
            slar = lar
            lar = a
        elif a > slar and a < lar:
            slar = a
    
    print(slar)
