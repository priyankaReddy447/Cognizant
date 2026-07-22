# Merge Sort
from pprint import pprint

def ms(a):
 if len(a)<=1:return a
 m=len(a)//2;L=ms(a[:m]);R=ms(a[m:]);o=[]
 while L and R:o.append((L if L[0]<R[0] else R).pop(0))
 return o+L+R
pprint(ms([5,3,1,4]))
