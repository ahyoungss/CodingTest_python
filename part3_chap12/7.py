#럭커 스트레이트
n = input() #점수 입력받기

half = len(n)//2

result1=0
result2=0
for i in range(half):
  result1 += int(n[i])
for i in range(half,len(n)):
  result2 += int(n[i])

if result1 == result2: print('LUCKY')
else : print('READY')