from entity.Category import Category

class CreateCategoryController:

    def CreateCategoryController(self,Title:str,Description:str)->bool:
        
        return Category.createCategory(Title,Description)

class ViewCategoryController:

    def ViewCategoryController(self,CategoryID:int)->Category:

        return Category.viewCategory(CategoryID)
    
class UpdateCategoryController:
    def UpdateCategoryController(self,categoryID:int,Title:str,Description:str,Is_Active:bool)->bool:
        return Category.updateCategory(categoryID,Title,Description,Is_Active)
    
class SuspendCategoryController:
    def SuspendCategoryController(self,categoryID:int)->bool:
        return Category.suspendCategory(categoryID)
    
class SearchCategoryController:
    def SearchCategoryController(self,keyword:str)->list[Category]:
        return Category.searchCategory(keyword)