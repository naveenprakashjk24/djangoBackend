from django.urls import path, include
from .views import contractor_list, restricted, contractor_details, StagesApiView, StageDetailsApiview

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('restrict/', restricted),
    path('contractorlist/', contractor_list, name='cont-list'),
    path('contractordetails/<int:pk>/', contractor_details, name='cont-list'),
    path('stageslist/', StagesApiView.as_view()),
    path('stagedetails/<int:id>/', StageDetailsApiview.as_view()),
    ]


''' login/logout urls
register - auth/token/users/
login -  auth/token/login
logout - auth/token/logout

'''