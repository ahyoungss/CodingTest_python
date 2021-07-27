#상하좌우

n = int(input())#공간의 크기를 나타내는 n 입력받기

data = input().split() #a가 이동할 계획서 내용

x = 1
y = 1

for i in data:
  if data[i] == 'L':
    if y == 1:
      i += 1
    else: y -= 1
  elif data[i] == 'R':
    if y == 5:
      i += 1
    else: y += 1
  elif data[i] == 'U':
    if x == 1:
      i += 1
    else: x -= 1
  elif data[i] == 'D':
    if x == 5:
      i += 1
    else: x+= 1

print( x, y )