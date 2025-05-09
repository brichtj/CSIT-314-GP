from entity.Service import Service
class CreateServiceController:

    def createServiceController(self, CategoryID: int,Title: str,Description: str,CleanerID: int,Price: float,ImageLink: str):
        
        return Service().createService(CategoryID,Title,Description,CleanerID,Price,ImageLink)
    
class ViewServiceController:
    def ViewServiceController(self,ServiceID:int)->Service:
        return Service().viewService(ServiceID)
    