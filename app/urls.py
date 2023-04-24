from django.urls import path
from . import views
from .views import add_airplane

urlpatterns = [
    path('', views.home, name='home'),
    path('flight/', views.flight, name='flight'),
    path('book-flight/', views.book_flight, name='book_flight'),
    path('add_airplane/', add_airplane, name='add_airplane'),
    path('select-flight/', views.select_flight, name='select_flight'),
    path('flight_detail/', views.flight_detail, name='flight_detail'),
]
