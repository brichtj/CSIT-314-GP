from entity.Shortlist import Shortlist
from entity.Service import Service

class ShortListServiceController:
    def ShortListServiceController(self, serviceID:int, HomeOwnerID:int)->bool:
        return Shortlist.shortListService(serviceID, HomeOwnerID)

class SearchShortListController:
    def SearchShortListForHomeOwnerController(self, HomeOwnerID:int,Title:str)->list[Service]:
        return Shortlist.searchShortlistForHomeOwner(HomeOwnerID,Title)