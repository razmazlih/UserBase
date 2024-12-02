from django.urls import path
from .views import (
    UserProfileView,
    CreateUserView,
    ChangePasswordView,
    ChangeUsernameView,
)

urlpatterns = [
    path("profile/", UserProfileView.as_view(), name="user-profile"),
    path("register/", CreateUserView.as_view(), name="user-register"),
    path("change-password/", ChangePasswordView.as_view(), name="change-password"),
    path("change-username/", ChangeUsernameView.as_view(), name="change-username"),
]
