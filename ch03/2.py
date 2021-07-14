n,m,k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

maxData = data[n-1]
secData = data[n-2]

sum = 0
for i in range(1,m+1):
    if i%(k+1) != 0:
        sum += maxData
    else:
        sum += secData

print(sum)
