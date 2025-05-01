from django.urls import path 
from . import views 

urlpatterns =[
    path('',views.index,name='index'),
    path('menu/',views.menu,name='menu'),
    path('about/',views.about,name='about'),
    path('book/',views.book,name='book'),
    path('rating/',views.rating,name='rating'),
    path('login',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
]