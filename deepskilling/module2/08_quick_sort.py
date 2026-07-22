# Quick Sort

def qs(a):
 return a if len(a)<=1 else qs([x for x in a[1:] if x<=a[0]])+[a[0]]+qs([x for x in a[1:] if x>a[0]])
print(qs([3,6,1,2]))
