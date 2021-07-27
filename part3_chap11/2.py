#곱하기 혹은 더하기
s = input() #문자열 입력받기

n = list(map(int,s)) #문자열 -> 정수로

result = n[0]

for i in range(1,len(n)):
  if(n[i-1] == 0):
    result += n[i]
  else:
    result *= n[i]
    
print(result)
