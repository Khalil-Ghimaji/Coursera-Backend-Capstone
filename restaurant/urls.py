from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view(), name='menu-list-create'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-detail-update-delete'),
]
