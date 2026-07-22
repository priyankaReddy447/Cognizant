class Light:
    def on(self): print('ON')
class Cmd:
    def __init__(self,l): self.l=l
    def execute(self): self.l.on()
Cmd(Light()).execute()
