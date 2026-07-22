class Add:
    def execute(self,a,b): return a+b
class Mul:
    def execute(self,a,b): return a*b
print(Add().execute(5,3)); print(Mul().execute(5,3))
