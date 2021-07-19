#문제의 조건

n,m = map(int, input().split())

d = [[0]*m for _ in range(n)]

#현재캐릭터 위치, 방향 입력
x,y,direction = map(int,input().split())
d[x][y] = 1 #현재 좌표 방문 처리

array = []
for i in range(n):
    array.append(list(map(int ,input().split())))

#북동남서 정의
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3 #문제에서 북:0 동:1 남:2 서:3 로 정의했다

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)