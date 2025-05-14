
from .Service.ServiceBoundary import router as service_boundary
from .UserProfile.UserProfileBoundary import router as user_profile_boundary
from .User.UserBoundary import router as user_boundary
from .Category.CategoryBoundary import router as category_boundary
from .Shortlist.ShortlistBoundary import router as Shortlist_boundary
from .Matches.MatchBoundary import router as match_boundary

#User Admin
__all__ = ["match_boundary","service_boundary","user_profile_boundary","user_boundary","category_boundary","Shortlist_boundary"]
