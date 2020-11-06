a = 0
b = 0
c = []
for i in range(2000, 5001):
    a = 0
    b = i
    c.clear()
    for j in range(4):
        if ((b % 10) % 2) == 0:
            a += 1
            c.append((b % 10))
        b //= 10
    c.reverse()
    if a == 4:
        print(i, end = ':')
        for j in range(len(c)):
            if j != 3:
                print(c[j], end=',')
            else:
                print(c[j])