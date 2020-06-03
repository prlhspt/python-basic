ze = 0
on = 0
tw = 0
th = 0
fo = 0
fi = 0
si = 0
se = 0
ei = 0
ni = 0


for i in range(1, 1000):
    sp = str(i)
    for j in sp:
        if int(j) == 0:
            ze += 1
        elif int(j) == 1:
            on += 1
        elif int(j) == 2:
            tw += 1
        elif int(j) == 3:
            th += 1
        elif int(j) == 4:
            fo += 1
        elif int(j) == 5:
            fi += 1
        elif int(j) == 6:
            si += 1
        elif int(j) == 7:
            se += 1
        elif int(j) == 8:
            ei += 1
        else:
            ni += 1

print(ze, on, tw, th, fo, fi, si, se, ei, ni)