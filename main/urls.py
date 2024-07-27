from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.index, name='home'),
    path('hakkimizda/', views.hakkimizda, name='hak'),
    path('bungalov/<int:pk>/', views.bungalov_detail, name='bungalov_detail'),
    path('gizlilik/', views.gizlilik, name='giz'),
    path('kurallar/', views.kurallar, name='kurallar'),
    path('villa/', views.villa, name='villa'),
    path('villa/<int:id>/', views.villa_detail, name='villa_detail'),
    path('bungalov/', views.bungalov, name='bg'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)