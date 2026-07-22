from abc import ABC,abstractmethod
class Database(ABC):
    @abstractmethod
    def connect(self): ...
class MySQL(Database):
    def connect(self): print('Connected')
class App:
    def __init__(self,db): self.db=db
    def start(self): self.db.connect()
App(MySQL()).start()
