# Singly Linked List
class N:
 def __init__(s,d): s.d=d;s.n=None
h=N(1);h.n=N(2);t=h
while t:print(t.d);t=t.n
