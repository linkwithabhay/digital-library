from django.urls import path

from .views import (
  home,
  CustomLoginView,
  CustomRegisterView,
  CustomLogoutView,
)

app_name = 'account'

urlpatterns = [
  path('', home, name='home'),
  path('login/', CustomLoginView.as_view(), name='login'),
  path('logout/', CustomLogoutView.as_view(), name='logout'),
  path('register/', CustomRegisterView.as_view(), name='register'),
]
