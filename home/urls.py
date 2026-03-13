from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home, name='home'),

    #REALIZAR CADASTRO
    path('realizar_cadastro/', views.RealizarCadastro, name='realizar_cadastro'),
    path('cadastro/', views.cadastrar , name='cadastro'),
    #LOGIN
    path('login/', views.login, name='login'),

    #AGENDAMENTO
    path('agendar/', views.agendar, name='agendar'),
    path('agenda-barbeiro-htmx/',views.agenda_barbeiro_htmx,name='agenda_barbeiro_htmx'),
    path('confirmar-agendamento/', views.confirmar_agendamento, name='confirmar_agendamento'),
    path('meus-agendamentos/', views.ver_agendamentos, name='meus_agendamentos'),
    path('cancelar-agendamento/<int:agendamento_id>/', views.cancelar_agendamento,name='cancelar_agendamento'),
]