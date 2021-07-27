#문자열 뒤집기
s = input() #문자열 입력받기

count_0 = 0
count_1 = 0

for i in range(0,len(s)-1):
  if s[i] != s[i+1]:
    if s[i]==0:
      count_0 += 1
    if s[i]==1:
      count_1 += 1
  if s[i] == s[i+1]:
    continue

if count_0 >= count_1:
  print(count_0)
else:
  print(count_1)
    