# 큰 수의 법칙 

# n,m,k를 공백으로 구분하여 입력 (n은 데이터 개수, m은 몇번 더할지, k는 최대 몇번까지 더할 수 있는지)
n,m,k = map(int, input().split())

data = list(map(int,input().split())) 

data.sort()
print(data)

first = data[n-1]
second = data[n-2]

result = 0
while True:
    for i in range(k):
      if m==0 : break
      result += first
      m -= 1
    if m == 0:
      break
    result += second
    m-= 1

print(result)
        