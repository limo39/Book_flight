from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('flight/', views.flight, name='flight'),
    path('book-flight/', views.book_flight, name='book_flight'),
]
 #path('book-flight/<int:flight_id>/', views.book_flight, name='book_flight'),