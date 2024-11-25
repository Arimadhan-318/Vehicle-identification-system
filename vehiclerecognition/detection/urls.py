from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('upload-image/', views.upload_image_view, name='upload_image'),
    path('contact/',views.contact_view,name='contact'),
    path('', views.home_view, name='home')
]