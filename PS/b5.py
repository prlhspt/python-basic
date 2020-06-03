N = int(input("N 이하의 완전수 구하기 : "))

for i in range(1, N):
    sum = 0
    for j in range(1, i):
        if i % j == 0:
            sum = sum + j
    if sum == i:
        print(i)

