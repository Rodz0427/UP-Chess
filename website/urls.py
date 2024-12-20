from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('player/<int:pk>', views.player_profile, name='player'),
    path('remove_player/<int:pk>', views.remove_player, name='remove_player'),
    path('add_player/', views.add_player, name='add_player'),
    path('update_player/<int:pk>', views.update_player, name='update_player'),


]