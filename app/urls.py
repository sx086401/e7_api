from django.urls import path
from .views import UserView

app_name = 'app'

urlpatterns = [
    path('users/', UserView.as_view(), name='user_list'),
    path('users/', UserView.as_view(), name='create_user'),
]
