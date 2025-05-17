
from entity.Report import Report


class GetReportController:

    def getReportController(self,mode:str)->Report:
        return Report.getReport(mode)