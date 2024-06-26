from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

#     config/urls
#     path('api/v1/users/', include('users.urls')),

urlpatterns = [
    path("", views.Users.as_view()),
    path("myinfo/", views.MyInfo.as_view()),

    # Authentication
    path("getToken/", obtain_auth_token),
    path("login/", views.Login.as_view()),
    path("logout/", views.Logout.as_view()),

    path("login/jwt/", views.JWTLogin.as_view()),  # jwt login
    # path("login/jwt", JWTLogin.as_view()),  # jwt login

    path("login/jwt/info/", views.UserDetailView.as_view()),


]