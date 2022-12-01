from django.urls import  path
from . import  views
from django.contrib.auth import views as auth_views
urlpatterns=[
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('login/',auth_views.LoginView.as_view(),name='login'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('admin/', views.data, name='admin'),
    path('addsuccess/', views.addsuccess, name='addsuccess'),
    path('updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
path ('register/',views.register,name='register'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout')
]