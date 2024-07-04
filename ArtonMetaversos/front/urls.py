from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('registrar/', views.registrar, name='registrar'),
    path('dashboard/', views.dashboard_home, name='dashboard_home'),
    path('dashboard/manage_games/', views.manage_games, name='manage_games'),
    path('dashboard/profile/', views.profile, name='profile'),
    path('dashboard/settings/', views.settings, name='settings'),
    path('dashboard/raca/criar/', views.criar_raca, name='criar_raca'),
    path('dashboard/raca/lista/', views.lista_racas, name='lista_racas'),
    path('dashboard/raca/<int:raca_id>/', views.detalhes_raca, name='detalhes_raca'),
]
