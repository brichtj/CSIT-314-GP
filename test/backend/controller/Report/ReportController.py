
from entity.Report import Report


class GetReportController:

    def getReportController(self,mode:str)->list[Report]:
        return Report.getReport(mode)