from entity.Cleaner import Cleaner
from entity.Service import Service
from entity.Matches import Matches


class CleanerCreationController:
    def register(self, username, password, email, phone, experience):
        cleaner = Cleaner(
            username=username,
            email=email,
            phone=phone,
            Experience=experience,
            input_password=password
        )
        return cleaner.create_account()

##################################################################################
# View Total Views of Services
##################################################################################


class CleanerViewServiceTotalViewsController:
    def ViewTotalViewbyID(ServiceID):
        return Service.ViewTotalViewbyID(ServiceID)

##################################################################################
# View Total Shortlisted Count of Services
##################################################################################


class CleanerViewServiceShortlistedCountController:

    def ViewTotalShortlistedCount(ServiceID):
        return Service.ViewTotalShortlistedCount(ServiceID)

##################################################################################
# View History
##################################################################################


class CleanerViewHistoryController:
    def ViewHistory(CleanerID):
        return Matches.ViewCleanerHistory(CleanerID)

##################################################################################
# Search History
##################################################################################


class CleanerSearchHistoryController:
    def SearchHistoryByServiceID(CleanerID, ServiceID):
        return Matches.SearchCleanerHistoryByServiceID(CleanerID, ServiceID)
