class Model:
    def __init__(self,n): self.name=n
class View:
    def display(self,m): print(m.name)
View().display(Model('Priya'))
