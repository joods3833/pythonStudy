# 음료수 얼려먹기
# 입력예시
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000011111
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 00000001111000
# 11111111110011
# 11100011111111
# 11100011111111

# 출력예시
# 8

# 연결된 노드가 없을 때 아이스크림 하나 생성

#n,m 입력
n,m = map(int, input().split())
#2차원 리스트 입력
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
#dfs로 특정한 노드 방문 뒤 연결된 모든 노드 방문
def dfs(x,y):
    #범위이탈
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    #노드방문
    if graph[x][y] == 0:
        graph[x][y] = 1

        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False
#노드에 음료수 채우기
result = 0

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)