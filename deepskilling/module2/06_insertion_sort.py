# Insertion Sort
a=[5,2,4,1]
for i in range(1,len(a)):
 k=a[i];j=i-1
 while j>=0 and a[j]>k:a[j+1]=a[j];j-=1
 a[j+1]=k
print(a)
