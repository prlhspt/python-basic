d = 0
e = 0

b = 0
c = []
for i in range(100, 500):
    for j in range(500, 1000):
            # 6자리
            if i*j >= 100000:
                a = str(i*j)
                if a[0] == a[5] and a[1] == a[4] and a[2] == a[3]:
                    if b < (i*j):
                        b = (i*j)
                        d = i
                        e = j

            # 5자리
            else:
                a = str(i*j)
                if a[0] == a[4] and a[1] == a[3]:
                    if b < (i * j):
                        b = (i * j)
                        d = i
                        e = j

print(b, d, e)
