from django.urls import path
from django.contrib.auth import views as auth_views

from qa import views

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('question/<int:pk>/', views.question_detail, name='question_detail'),
    path('ask/', views.ask_question, name='ask_question'),
    path('login/', auth_views.LoginView.as_view(template_name='qa/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
 ]