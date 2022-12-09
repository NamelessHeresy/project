from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('category/', category, name='category'),
    path('category/<int:cat_id>', category, name='category'),
    path('login/', login, name='login'),
    path('goods/<int:goods_id>', goods, name='goods'),
]
Handler404 = pageNotFound
