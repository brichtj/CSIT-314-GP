from entity.Service import Service
class CreateServiceController:

    def createServiceController(self, CategoryID: int,Title: str,Description: str,CleanerID: int,Price: float,ImageLink: str):
        
        return Service().createService(CategoryID,Title,Description,CleanerID,Price,ImageLink)
    
class ViewServiceController:
    def ViewServiceController(self,ServiceID:int)->Service:
        return Service().viewService(ServiceID)
    
class UpdateServiceController:
    def UpdateServiceController(self,CategoryID:int,Title:str,Description:str,price:float,ImageLink:str, ServiceID:int,CleanerID:int)->bool:
        return Service().updateService(CategoryID,Title,Description,price,ImageLink,ServiceID,CleanerID)

class DeleteServiceController:
    def DeleteServiceController(self,ServiceID:int,CleanerID:int)->bool:
        return Service().deleteService(ServiceID,CleanerID)
    
class SearchServiceCleanerIDController:
    def SearchServiceCleanerIDController(self,Title:str,CleanerID:int)->list[Service]:
        return Service().searchServiceByCleanerID(Title,CleanerID)
    
##################################################################################
# Req3.4 Search Shortlist Service
##################################################################################


class HomeOwnerViewShortListController:

    def ViewShortlistByHomeOwnerID(self, HomeOwnerID: str):
        return HomeOwner().ViewShortListByHomeOwnerID(HomeOwnerID)
