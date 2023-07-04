from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('users', views.UserListView.as_view()),
    path('users/create', views.UserCreateView.as_view()),
    path('users/<int:pk>', views.UserDetailView.as_view()),
    path('users/<int:pk>/update', views.UserUpdateView.as_view()),
    path('users/<int:pk>/delete', views.UserDeleteView.as_view()),
]
