#모험가 길드

# 모험가 수 n 입력받기
n = int(input())

#각 모험가의 공포드의 값 입력
data = list(map(int,input().split())) 
data.sort()

result = 0 # 그룹 수
count = 0 #모험가의 수

for i in data:
  count += 1
  if count >= i:
    result += 1
    count = 0

print(result)