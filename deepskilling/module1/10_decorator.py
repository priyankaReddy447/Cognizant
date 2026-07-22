class Coffee:
    def cost(self): return 100
class Milk:
    def __init__(self,c): self.c=c
    def cost(self): return self.c.cost()+20
print(Milk(Coffee()).cost())
