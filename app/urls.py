from django.urls import path
from .views import UserListView, CreateUserView

app_name = 'app'

urlpatterns = [
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/', CreateUserView.as_view(), name='create_user'),
]
