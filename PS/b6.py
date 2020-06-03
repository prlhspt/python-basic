N = int(input('합제곱-제곱합 할 값 : '))
sum = 0
mat = 0
for i in range(1, N+1):
    sum = sum + i**2
    mat = mat + i
mat = mat ** 2

print(mat - sum)