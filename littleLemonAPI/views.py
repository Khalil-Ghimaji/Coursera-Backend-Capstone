from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from littleLemonAPI.models import Menu, Booking
from littleLemonAPI.serializers import MenuSerializer, BookingSerializer


# Create your views here.
class MenuItemView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class SingleBookingView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
