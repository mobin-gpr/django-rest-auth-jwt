from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import (
    RegisterAPIView,
    EmailVerificationAPIView,
    ResendEmailVerificationAPIView,
    ChangePasswordAPIView,
    ResetPasswordAPIView,
    SetPasswordAPIView,
    ProfileAPIView,
)

urlpatterns = [
    path(
        "register/", RegisterAPIView.as_view(), name="register"
    ),  # Register a new user endpoint
    path(
        "confirm_email/<str:token>/",
        EmailVerificationAPIView.as_view(),
        name="confirm_email",
    ),  # Confirm email by token endpoint
    path(
        "resend_confirm_email/",
        ResendEmailVerificationAPIView.as_view(),
        name="resend_confirm_email",
    ),  # Resend confirm email endpoint
    path(
        "change_password/",
        ChangePasswordAPIView.as_view(),
        name="change_password",
    ),  # Change user password endpoint
    path(
        "reset_password/",
        ResetPasswordAPIView.as_view(),
        name="reset_password",
    ),  # Reset user password endpoint
    path(
        "set_password/<str:token>",
        SetPasswordAPIView.as_view(),
        name="set_password",
    ),  # Set user password after reset password endpoint
    path("profile/", ProfileAPIView.as_view(), name="profile"),  # User profile endpoint
    # JWT endpoints
    path("jwt/token/", TokenObtainPairView.as_view(), name="get_token"),
    path("jwt/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("jwt/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
