from entity.HomeOwner import HomeOwner
from entity.Service import Service
from entity.Matches import Matches


class HomeOwnerCreationController:

    def HomeOwnerCreationController(self, username, email, phone, address):
        homeOwner = HomeOwner(username, email, phone, address)
        return homeOwner.createUser()

##################################################################################
# Req3.1 Search Service
##################################################################################


class HomeOwnerSearchServiceController:
    def SearchServiceByMode(self, mode: int, data: str):
        if (mode == 1):
            result = Service().SearchServiceByCategoryName(data)
        if (mode == 2):
            result = Service().SearchServiceByCategoryID(data)
        if (mode == 3):
            result = Service().SearchServiceByCleanerID(data)

        result = Service().SearchServiceByTitle(data)

        return result

##################################################################################
# Req3.2 View Service
##################################################################################


class HomeOwnerViewServiceController:
    def ViewServiceByID(self, ServiceID: str):
        return Service().ViewServiceByID(ServiceID)

##################################################################################
# Req3.3 Save/Shortlist Service
##################################################################################


class HomeOwnerShorlistServiceController:

    def ShortlistServiceByID(self, ServiceID: str, HomeOwnerID: str):
        return HomeOwner().ShortlistServiceByID(ServiceID, HomeOwnerID)

##################################################################################
# Req3.4 Search Shortlist Service
##################################################################################


class HomeOwnerViewShortListController:

    def ViewShortlistByHomeOwnerID(self, HomeOwnerID: str):
        return HomeOwner().ViewShortListByHomeOwnerID(HomeOwnerID)

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
