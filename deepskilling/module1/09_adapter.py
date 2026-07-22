class OldPrinter:
    def old_print(self): print('Old Printer')
class Adapter:
    def __init__(self,p): self.p=p
    def print(self): self.p.old_print()
Adapter(OldPrinter()).print()
