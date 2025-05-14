from entity.Service import Service, customService
class CreateServiceController:

    def createServiceController(self, CategoryID: int,Title: str,Description: str,CleanerID: int,Price: float,ImageLink: str):
        
        return Service().createService(CategoryID,Title,Description,CleanerID,Price,ImageLink)
    
class ViewServiceController:
    def ViewServiceController(self,ServiceID:int,updateViewCount:bool,HomeOwnerID:int = None)->customService:
        return Service().viewService(ServiceID,updateViewCount,HomeOwnerID)
    
class UpdateServiceController:
    def UpdateServiceController(self,CategoryID:int,Title:str,Description:str,price:float,ImageLink:str, ServiceID:int,CleanerID:int)->bool:
        return Service().updateService(CategoryID,Title,Description,price,ImageLink,ServiceID,CleanerID)

class DeleteServiceController:
    def DeleteServiceController(self,ServiceID:int,CleanerID:int)->bool:
        return Service().deleteService(ServiceID,CleanerID)
    
class SearchServiceCleanerIDController:
    def SearchServiceCleanerIDController(self,Title:str,CleanerID:int)->list[Service]:
        return Service().searchServiceByCleanerID(Title,CleanerID)
    
#req 4.1 view views of service
class ViewTotalViewbyIDController:
    def ViewTotalViewbyIDController(self,ServiceID:int)->int:
        return Service.ViewTotalViewbyID(ServiceID)
    
#req 4.2 view shortlisted count of service
class ViewTotalShortlistedCountByIDController:
    def ViewTotalShortlistedCountByIDController(self,ServiceID:int)->int:
        return Service.ViewTotalShortlistedCountByID(ServiceID)

##################################################################################
# Req3.1 Search Service
#################################################################################

class HomeOwnerSearchServiceController:
    def SearchService(self, mode: int, searchTerm: str)->list[Service]:
        return Service.SearchService(mode, searchTerm)


##################################################################################
# Req3.7View Account
##################################################################################


class HomeOwnerViewAccountController:

    def ViewAccount(self, HomeOwnerID: str):
        return HomeOwner().ViewAccount(HomeOwnerID)

##################################################################################
# Req3.8 Update Account
##################################################################################


class HomeOwnerUpdateAccountController:

    def UpdateAccount(self, HomeOwnerID: str, newUserName, newEmail, newPhone, newAddress):
        return HomeOwner().UpdateAccount(HomeOwnerID, newUserName, newEmail, newPhone, newAddress)

##################################################################################
# Req3.9 Suspend Account
##################################################################################


class HomeOwnerSuspendAccountController:

    def SuspendAccount(self, HomeOwnerID):
        return HomeOwner().SuspendAccount(HomeOwnerID)

##################################################################################
# Req6.1 View History
##################################################################################


class HomeOwnerViewHistoryController:
    def ViewHistory(self, HomeOwnerID):
        return Matches().ViewHomeOwnerHistory(HomeOwnerID)

##################################################################################
# Req6.2 Search History
##################################################################################


class HomeOwnerSearchHistoryController:
    def SearchHistoryByServiceID(self, HomeOwnerID, ServiceID):
        return Matches().SearchHomeOwnerHistoryByServiceID(HomeOwnerID, ServiceID)
