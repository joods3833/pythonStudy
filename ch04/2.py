#왕실의 나이트
# 수평으로 두 칸 이동 후 수직으로 한 칸
# 수직으로 두 칸 이동 후 수평으로 한 칸
# 8*8 행렬 모양
# 위:1 아래:8 왼쪽:a 오른쪽:h

#입력 예시
#a1
#출력예시 나이트가 이동 할 수 있는 경우의 수 출력
#2

#현재 나이트의 위치 입력 받기
input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2,-1), (-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2), (-1,-2)]

count = 0

for step in steps:
    next_row = row + step[0]
    next_col = col + step[1]

    if next_row >= 1 and next_row <=8 and next_col >= 1 and next_col <= 8:
        count +=1

print(count)