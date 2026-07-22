class Email:
    def send(self): print('Email Sent')
class Notify:
    def __init__(self,s): self.s=s
    def notify(self): self.s.send()
Notify(Email()).notify()
