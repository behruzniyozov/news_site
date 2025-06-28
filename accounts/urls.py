from django.urls import path
from accounts.api_endpoints import *

urlpatterns = [
    path('login/', SessionLoginAPIView.as_view(), name='login'),
    path('logout/', SessionLogoutAPIView.as_view(), name='logout'),
    path('register/', UserRegisterRequestView.as_view(), name='register'),
    path('register/confirm/<str:token>/', UserRegisterConfirmView.as_view(), name='register_confirm'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('profile/delete/', ProfileDeleteView.as_view(), name='profile_delete'),
    path('password/reset/', PasswordResetRequestView.as_view(), name='password_reset'),
    path('password/reset/confirm/<str:token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]