from django.urls import path
from .views import RegisterView, LoginView, BusListCreateView, BusDetailView, BookingView, UserBookingView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('buses/', BusListCreateView.as_view(), name='bus-list'),
    path('buses/<int:pk>/', BusDetailView.as_view(), name='bus-detail'),
    path('book/', BookingView.as_view(), name='book-seat'),
    path('my-bookings/<int:user_id>/', UserBookingView.as_view(), name='user-bookings'),
]