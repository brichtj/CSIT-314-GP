from entity.Service import Service
class CreateServiceController:

    def createServiceController(self, CategoryID: int,Title: str,Description: str,CleanerID: int,Price: float,ImageLink: str):
        
        return Service().createService(CategoryID,Title,Description,CleanerID,Price,ImageLink)
    
class ViewServiceController:
    def ViewServiceController(self,ServiceID:int,updateViewCount:bool)->Service:
        return Service().viewService(ServiceID,updateViewCount)
    
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
# Req3.1 Search Service
##################################################################################



class HomeOwnerSearchServiceController:
    def SearchService(self, mode: int, data: str):
        return Service.SearchService(mode, data)

##################################################################################
# Req3.2 View Service
##################################################################################


class HomeOwnerViewServiceController:
    def ViewServiceByID(self, ServiceID: str):
        return Service.ViewServiceByID(ServiceID)



##################################################################################
# Req3.5 View Shortlist Service
##################################################################################


class HomeOwnerViewShortlistedServiceController:

    def ViewShortlistedServiceByID(self, ServiceID: str):
        return Service().ViewServiceByID(ServiceID)

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
