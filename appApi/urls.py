from django.urls import path, include
from .views import *

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('restrict/', restricted)
    ]


''' login/logout urls
register - auth/token/users/
login -  auth/token/login
logout - auth/token/logout

'''