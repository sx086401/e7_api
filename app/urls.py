from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('users', views.user_list_create_view),
    path('users/<int:pk>', views.user_detail_view),
    path('users/<int:pk>/update', views.user_update_view),
    path('users/<int:pk>/delete', views.user_delete_view),
    path('characters', views.character_list_create_view),
    path('characters/<int:pk>', views.character_detail_view),
    path('characters/<int:pk>/update', views.character_detail_view),
    path('states', views.state_list_create_view),
    path('states/<int:pk>/update', views.state_update_view),
    path('states/<int:pk>/delete', views.state_delete_vew)
]
