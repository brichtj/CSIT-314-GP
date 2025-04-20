from app.entity.Category import Category
from app.entity.Service import Service
from app.entity.Matches import Matches

from datetime import datetime


try:
    #time = datetime(2025, 4, 16, 0, 48, 32, 61283)
    test = Service(2)
    test.update_LikeCount()
    test.update_ViewCount()
    test.update_MatchCount()
    print(test.to_dict())
except Exception as e:
    print(e)