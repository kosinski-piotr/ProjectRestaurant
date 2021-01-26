from django.urls import path
from . import views


urlpatterns = [
    path('RodzajDan',views.RodzajDanList.as_view(), name=views.RodzajDanList.name),
    path('RodzajDan/<int:pk>',views.RodzajDanDetail.as_view(), name=views.RodzajDanDetail.name),
    path('Dania', views.DaniaList.as_view(), name=views.DaniaList.name),
    path('Dania/<int:pk>', views.DaniaDetail.as_view(), name=views.DaniaDetail.name),
    path('Klients', views.KlientList.as_view(), name=views.KlientList.name),
    path('Klients/<int:pk>', views.KlientDetail.as_view(), name=views.KlientDetail.name),
    path('Zamowienia', views.ZamowienieList.as_view(), name=views.ZamowienieList.name),
    path('Zamowienia/<int:pk>', views.ZamowienieDetail.as_view(), name=views.ZamowienieDetail.name),
    path('users', views.UserList.as_view(), name=views.UserList.name),
    path('users/<int:pk>', views.UserDetail.as_view(), name=views.UserDetail.name),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
    ]
