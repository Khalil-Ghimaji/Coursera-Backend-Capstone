from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('menu/', views.MenuItemView.as_view(), name='menu-list-create'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-detail-update-delete'),
    path('bookings/', views.BookingView.as_view(), name='booking-list-create'),
    path('bookings/<int:pk>/', views.SingleBookingView.as_view(), name='booking-detail-update-delete'),
    path('api-token-auth/', obtain_auth_token)

]