array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
  if start >= end: return
  pivot = start
  left = start+1
  right = end
  while left <= right:
    #피벗보다 큰 데이터를 찾을 때까지 반복
    while left <= end and array[left] <= array[pivot]