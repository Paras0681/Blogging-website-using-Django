from django.urls import path
from .views import UserRegisterView
urlpatterns = [
    path('registration/register/', UserRegisterView.as_view(), name='register'),
]
