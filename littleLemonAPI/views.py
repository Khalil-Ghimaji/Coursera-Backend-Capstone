from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView

from littleLemonAPI.models import Menu, Booking
from littleLemonAPI.serializers import MenuSerializer, BookingSerializer


# Create your views here.
class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingView(ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class SingleBookingView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
