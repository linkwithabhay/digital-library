from django.urls import path

from .views import (
  home,
)

app_name = 'library'

urlpatterns = [
  path('', home, name='home')
]
