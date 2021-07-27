#만들 수 없는 금액
n = int(input()) #동전의 개수 입력받기

coin = list(map(int,input().split()))  #동전리스트로 받기
coin.sort()

num = 0
result = 0

for i in coin:
  num += 1
  if coin[i] == num : continue
  elif coin[i] + coin[i+1]
 

