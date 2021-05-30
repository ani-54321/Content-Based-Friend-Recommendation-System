from os import name
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.startpage, name='start'),
    path('signup/', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('signup/login', views.login, name='slogin'),
    path('home', views.myprofile, name='home'),
    path('myprofile', views.myprofile, name='myprofile'),
    path('signup/myprofile', views.myprofile, name='myprofile'),
    path('conrej', views.conrej, name="conrej"),
    path('signup/conrej', views.conrej, name="conrej"),
    path('rejects', views.rejects, name='rejects'),
    path('con_req', views.connection_reqs, name='con_req'),
    path('connections', views.your_connection, name='connections'),
    path('logout', views.logout, name='logout'),
    path('graph_connections', views.suggestions_from_graph, name='graph_connections'),
    path('graphs', views.engraph_me, name='graphs'),
]
