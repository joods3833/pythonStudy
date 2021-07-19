#거스름돈 문제
n = int(input())
#동전갯수
count = 0

coin_types = [500,100,50,10]

for coin in coin_types:
    count += n//coin #1260//500 == 2 #동전개수 500원짜리 두개 증가
    n %= coin #남은 돈 계산

print(count)