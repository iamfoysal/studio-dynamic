from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('photo/<str:pk>', views.viewPhoto, name='photo'),
    path('add', views.addPhoto, name='add'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('portfolio_one', views.portfolio_one, name='portfolio_one'),
]