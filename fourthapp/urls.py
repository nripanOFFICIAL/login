
from django.urls import path
from fourthapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add/',views.add,name='add'),
    path('login/',views.login,name='login'),
    path('log/',views.log,name='log'),
    path('afterlog/',views.afterlog,name='afterlog'),
    path('logout/',views.logout,name='logout'),
]
