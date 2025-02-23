from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path("usuario/", views.usuario, name="usuario"),
    path("editar_usuario/", views.editar_usuario, name="editar_usuario"),
    # Customizando a view de login
    # Redireciona pra LOGIN_REDIRECT se o usuário logado
    # tentar acessar a página de Login
    path(
        'login/', 
        auth_views.LoginView.as_view(
            redirect_authenticated_user=True
        ),
        name='login'
    ),
    # O urlpatterns testa na sequência, então ele vai
    # achar o 'login/' customizado primeiro ali em cima
    # e desconsiderar o padrão que está abaixo.
    path("", include("django.contrib.auth.urls")),
]