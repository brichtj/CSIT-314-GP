from entity.Matches import Matches
from Classes.CustomMatch import CustomMatch
from Classes.SimpleMatch import SimpleMatch

#create match controller
class CreateMatchController:
    def CreateMatchController(self, HomeOwnerID:int, ServiceID:int, Price:float,)->bool:
        return Matches.CreateMatch(HomeOwnerID, ServiceID, Price,)

class ViewMatchController:
    def ViewMatchController(self, serviceID: int)->CustomMatch:
        return Matches.ViewMatch(serviceID)
    
class SearchMatchCleanerController:
    def SearchMatchCleanerController(self, searchTerm:str,CleanerID:int)->list[SimpleMatch]:
        return Matches.SearchMatchCleaner(searchTerm,CleanerID)
    
class SearchMatchHomeOwnerController:
    def SearchMatchHomeOwnerController(self, searchTerm:str,HomeOwnerID:int)->list[SimpleMatch]:
        return Matches.SearchMatchHomeOwner(searchTerm,HomeOwnerID)