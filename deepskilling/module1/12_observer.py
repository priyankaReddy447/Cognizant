class Sub:
    def update(self,m): print(m)
class Pub:
    def __init__(self): self.s=[]
    def subscribe(self,x): self.s.append(x)
    def notify(self,m): [i.update(m) for i in self.s]
p=Pub(); s=Sub(); p.subscribe(s); p.notify('Hello')
