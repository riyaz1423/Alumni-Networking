from django.urls import path
from . import views
from django.contrib.auth.views import LoginView 

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit-alumni/', views.edit_alumni, name='edit_alumni'),
    path('logout/', views.logout_view, name='logout'),
    path("admin/dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("post-news/", views.post_news, name="post_news"),  # Ensure this exists
    path("post-vacancy/", views.post_vacancy, name="post_vacancy"),
    path("delete-news/<int:news_id>/", views.delete_news, name="delete_news"),
    path("delete-vacancy/<int:vacancy_id>/", views.delete_vacancy, name="delete_vacancy"),
    path("alumni-login/", views.alumni_login, name="alumni_login"),
    path('login/', views.login_view, name='login'),
    path('all-alumni/', views.all_alumni, name='all_alumni'),
]