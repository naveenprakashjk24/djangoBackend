from django.urls import path, include
# from .views import contractor_list, restricted, contractor_details, StagesApiView, StageDetailsApiview,ProjectstgMapping, ProjectStgmapUpdate
from .views import *

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('restrict/', restricted),
    path('cont-list/', contractor_list, name='cont-list'),
    path('cont-list/<int:pk>/', contractor_details, name='cont-list'),
    path('stageslist/', StagesApiView.as_view()),
    path('stageslist/<int:id>/', StageDetailsApiview.as_view()),
    path('stgmapping/', ProjectstgMapping.as_view()),
    path('stgmapping/<int:id>/', ProjectStgmapUpdate.as_view()),
    path('prjusermap/', ProjectuserMapping.as_view()),
    path('prjusermap/<int:id>/', ProjectuserMappingupdate.as_view()),
    path('dailyupdates/', DailyUpdatesView.as_view()),
    path('dailyupdates/<int:id>/', DailyUpdatesView.as_view()),

]


''' login/logout urls
register - auth/token/users/
login -  auth/token/login
logout - auth/token/logout

'''