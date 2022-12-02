from django.urls import  path
from . import  views
from django.contrib.auth import views as auth_views
urlpatterns=[
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('admin/', views.data, name='admin'),
    path('addsuccess/', views.addsuccess, name='addsuccess'),
    path('updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('Login/', auth_views.LoginView.as_view(), name='login'),
    path ('register/',views.register,name='register'),
    path('Logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

]