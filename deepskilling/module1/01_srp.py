class Report:
    def __init__(self,content): self.content=content
class ReportPrinter:
    def print_report(self,r): print(r.content)
report=Report("Sales increased by 20%"); ReportPrinter().print_report(report)
