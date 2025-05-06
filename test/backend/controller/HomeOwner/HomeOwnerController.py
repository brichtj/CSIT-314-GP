from entity.HomeOwner import HomeOwner
from entity.Service import Service
from entity.Matches import Matches


class HomeOwnerCreationController:

    def HomeOwnerCreationController(self, username, email, phone, address):
        homeOwner = HomeOwner(username, email, phone, address)
        return homeOwner.createUser()

##################################################################################
# Search Service
##################################################################################


class HomeOwnerSearchServiceController:

    def SearchServiceByTitle(Title: str):
        return Service.SearchServiceByTitle(Title)

    def SearchServiceByCategoryName(CategoryName: str):
        return Service.SearchServiceByCategoryName(CategoryName)

    def SearchServiceByCategoryID(CategoryID: str):
        return Service.SearchServiceByCategoryID(CategoryID)

    def SearchServiceByCleanerID(CleanerID: str):
        return Service.SearchServiceByCleanerID(CleanerID)

##################################################################################
# View Service
##################################################################################


class HomeOwnerViewServiceController:

    def ViewServiceByID(ServiceID: str):
        return Service.ViewServiceByID(ServiceID)

##################################################################################
# Save/Shortlist Service
##################################################################################


class HomeOwnerShorlistServiceController:

    def ShortlistServiceByID(ServiceID: str, HomeOwnerID: str):
        return HomeOwner.ShortlistServiceByID(ServiceID, HomeOwnerID)

##################################################################################
# Search Shortlist Service
##################################################################################


class HomeOwnerViewShortListController:

    def ViewShortlistByHomeOwnerID(HomeOwnerID: str):
        return HomeOwner.ViewShortListByHomeOwnerID(HomeOwnerID)

##################################################################################
# View Shortlist Service
##################################################################################


class HomeOwnerViewShortlistedServiceController:

    def ViewShortlistedServiceByID(ServiceID: str):
        return Service.ViewServiceByID(ServiceID)

##################################################################################
# View Account
##################################################################################


class HomeOwnerViewAccountController:

    def ViewAccount(HomeOwnerID: str):
        return HomeOwner.ViewAccount(HomeOwner)

##################################################################################
# Update Account
##################################################################################


class HomeOwnerUpdateAccountController:

    def UpdateAccount(HomeOwnerID: str, newUserName, newEmail, newPhone, newAddress):
        return HomeOwner.UpdateAccount(HomeOwnerID, newUserName, newEmail, newPhone, newAddress)

##################################################################################
# Suspend Account
##################################################################################


class HomeOwnerSuspendAccountController:

    def SuspendAccount(HomeOwnerID):
        return HomeOwner.SuspendAccount(HomeOwnerID)

##################################################################################
# View History
##################################################################################


class HomeOwnerViewHistoryController:
    def ViewHistory(HomeOwnerID):
        return Matches.ViewHomeOwnerHistory(HomeOwnerID)

##################################################################################
# Search History
##################################################################################


class HomeOwnerSearchHistoryController:
    def SearchHistoryByServiceID(HomeOwnerID, ServiceID):
        return Matches.SearchHomeOwnerHistoryByServiceID(HomeOwnerID, ServiceID)
