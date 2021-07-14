n,m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))

    for a in data:
        min_value = min(data)
        result = max(a,min_value)

print(result)