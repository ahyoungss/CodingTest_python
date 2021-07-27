# 볼링공 고르기

n,m = map(int, input().split()) #볼링공 개수와 최대 무게 설정

weight = list(map(int,input().split()))  #무게 리스트로 받기
weight.sort()

result = (int) (n*(n-1)/2) #
count=0
for i in range(n-1):
  if( weight[i+1] == weight[i]):
    count += 1

print(result-count)