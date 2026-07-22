# Binary Search
arr=[1,2,3,4,5];l,h=0,4;k=4
while l<=h:
 m=(l+h)//2
 if arr[m]==k: print(m);break
 elif arr[m]<k:l=m+1
 else:h=m-1
