n = int(input())
matrix = []

for _ in range(n):
    raw = list(map(int, input().split()))
    matrix.append(raw)

road = 0
for i in range(n):
    for j in range(i+1, n):
        if matrix[i][j] == 1:
            road += 1
print(road)
