s = input()

num = s[0]
set = 1

for i in range(1,len(s)):
  if(num != s[i]):
    set +=1
    num = s[i]

print(set//2)