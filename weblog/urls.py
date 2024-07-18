from django.urls import path
from . import views
from . import forms

app_name = 'weblog'
urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name = 'blog'),
    path('home/', views.home, name= 'home'),
    path('register/',views.register,name='register'),  
    path('login/', views.user_login_view, name='login'),
    path('users/', views.user_list, name='user_list'),
    path('add_blog/', views.blog_view, name='add_blog'),
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('blog/<int:id>/', views.blog_detail, name='blog_detail'),
    path('blog/update/<int:pk>/',views.blog_update_view,name="blog-update"),
    path('delete/<int:pk>/', views.blog_delete_view, name='blog-delete'),
    path('logout/', views.logout_view, name='logout'),
]

