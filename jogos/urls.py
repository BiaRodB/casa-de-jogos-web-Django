from django.urls import path
from . import views 

urlpatterns = [
    path('', views.login_user, name='login_user'),
    path('cadastro/', views.cadastrar_cli, name='cadastrar_cli'),
    path('autenticar_usuario', views.autenticar_usuario, name='autenticar_usuario'),
    path('create_user', views.create_user,name='create_user'),
    path('home', views.home,name='home'),
    path('apostar', views.aposta,name='apostar'),
    path('mega_sena',views.mega_sena,name='mega_sena'),
    path('listar',views.listar,name='listar'),
    path('carteira',views.carteira,name='carteira'),
    path('jogo_bicho',views.jogo_bicho,name='jogo_bicho'),
    path('Sbicho',views.Sbicho,name='Sbicho'),
    path('perfil',views.perfil,name='perfil'),
    path('listarb',views.listarb,name='listarb'),
    path('listar_perf',views.listar_perf,name='listar_perf'),
    path('res_b',views.res_b,name='res_b'),
    path('depositar',views.depositar,name='depositar'),
    path('listarjb',views.listarjb,name='listarjb'),
    path('somar',views.somar,name='somar'),


    #logaut
    path('logaut_user',views.logaut_user,name='logaut_user'),
    
]