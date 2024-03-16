from .views import *
from django.urls import path
from . import views

urlpatterns = [
    path('Account/', AccountListCreateView.as_view()),
    path('Account/<int:id>/', AccountRetrieveUpdateDestroyView.as_view() ),
    path('Account/login/', AccountloginView.as_view() ),
]