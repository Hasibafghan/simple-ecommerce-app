from django.urls import path
from . import views
from . import forms
urlpatterns = [
    path('' , views.products , name='products'),
    path('about/' , views.about_us , name='about'),
    path('login/' , views.login_user , name='login'),
    path('logout/' , views.logout_user , name='logout'),
    path('signup/' , views.signup_user , name='signup'),
    path('detail/<int:pk>/' , views.product_detail , name='detail'),
    path('category/<str:category_name>/' , views.category_products , name='category'),
]
