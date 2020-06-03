second = 0

for i in range(1, 60):
    for j in range(1, 60):
        if i == 3 or i == 33:
            second = second + i*60 + j
        if j == 3 or j == 33:
            second = second + i*60 + j
print(second)
