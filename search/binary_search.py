def binary_search(arr,x):
  low=0
  high = len(arr)-1
  mid = 0
  while(low<=high):
    mid = (low+high)//2
    if(arr[mid]==x):
      return mid
    elif(arr[mid]>x):
      high = mid-1
    else:
      low = mid+1
   
  return -1

arr = [2,44,56,23,34,5,54]
arr.sort()
result = binary_search(arr,23)
if(result == -1):
  print("No. not present")
else:
  print("Number is present{}".format(result))
