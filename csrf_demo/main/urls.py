from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.user_login),
    path('write/', views.write_post),
    path('attack/', views.csrf_attack)

]