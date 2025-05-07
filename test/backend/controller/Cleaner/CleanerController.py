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
# Req4.1 View Total Views of Services
##################################################################################


class CleanerViewServiceTotalViewsController:
    def ViewTotalViewbyID(self, ServiceID):
        return Service().ViewTotalViewbyID(ServiceID)

##################################################################################
# Req4.2 View Total Shortlisted Count of Services
##################################################################################


class CleanerViewServiceShortlistedCountController:

    def ViewTotalShortlistedCountByID(self, ServiceID):
        return Service().ViewTotalShortlistedCountByID(ServiceID)

##################################################################################
# Req5.1 View History
##################################################################################


class CleanerViewHistoryController:
    def ViewHistory(self, CleanerID):
        return Matches().ViewCleanerHistory(CleanerID)

##################################################################################
# Req5.2 Search History
##################################################################################


class CleanerSearchHistoryController:
    def SearchHistoryByServiceID(self, CleanerID, ServiceID):
        return Matches().SearchCleanerHistoryByServiceID(CleanerID, ServiceID)
