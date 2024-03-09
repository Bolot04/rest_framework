from django.urls import path
from . import views
from .views import RegistrationAPIView, ConfirmUserAPIView, LoginAPIView, LogoutAPIView

# from users.views import (
#     RegistrationAPIView,
#     ConfirmUserAPIView,
#     AuthorizationAPIView,
#     LogoutAPIView
# )
#
# urlpatterns = [
#     path('users/registration/', views.registration_api_view),
#     path('users/confirm/', views.confirm_user_api_view),
#     path('users/login/', views.login_api_view),
#     path('users/logout/', views.logout),
# ]

urlpatterns = [
    path('users/registration/', RegistrationAPIView.as_view()),
    path('users/confirm/', ConfirmUserAPIView.as_view()),
    path('users/authorization/', LoginAPIView.as_view()),
    path('users/logout/', LogoutAPIView.as_view())
]