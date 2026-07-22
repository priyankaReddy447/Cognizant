class Real:
    def display(self): print('Displaying')
class Proxy:
    def __init__(self): self.r=None
    def display(self):
        if not self.r: self.r=Real(); self.r.display()
Proxy().display()
