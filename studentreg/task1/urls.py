from django.urls import path,include
from task1 import views


urlpatterns = [
   path('',views.index,name='index'),
   path('login', views.login_view, name='login'),
   path('dashboard/', views.dashboard, name='dashboard'),
   path('logout/', views.logout_view, name='logout'),
   path('profile/',views.profile,name='profile'),
   path('register',views.register,name='register'),
   path('adminlog',views.adminlog,name='adminlog'),
   path('regview',views.regview,name='regview'),

   path('view/<int:id>/', views.reg_detail, name='reg_detail'),
   path('edit/<int:id>', views.edit, name='edit'),
   path('updateinfo', views.updateinfo, name='updateinfo'),
   path('deleteinfo/<int:id>', views.deleteinfo, name='deleteinfo'),



]






   
