from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
 path('register/', views.register, name= 'register'),
 path('', views.home, name= 'home'),
 path("checkout/<int:product_id>/", views.checkout, name="checkout"),
 path("success/", views.success, name="success"),

]
