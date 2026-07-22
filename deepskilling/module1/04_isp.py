from abc import ABC,abstractmethod
class Printer(ABC):
    @abstractmethod
    def print_doc(self): ...
class Scanner(ABC):
    @abstractmethod
    def scan_doc(self): ...
class MultiFunctionPrinter(Printer,Scanner):
    def print_doc(self): print('Printing')
    def scan_doc(self): print('Scanning')
d=MultiFunctionPrinter(); d.print_doc(); d.scan_doc()
