from entity.Matches import Matches

#create match controller
class CreateMatchController:
    def CreateMatchController(self, HomeOwnerID:int, ServiceID:int, Price:float,)->bool:
        return Matches().CreateMatch(HomeOwnerID, ServiceID, Price,)