from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self): ...
class Rectangle(Shape):
    def __init__(self,l,w): self.l=l; self.w=w
    def area(self): return self.l*self.w
class Circle(Shape):
    def __init__(self,r): self.r=r
    def area(self): return 3.14*self.r*self.r
for s in [Rectangle(4,5),Circle(3)]: print(s.area())
