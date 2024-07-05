#define URL route for index() view
from django.urls import path, include
from . import views
from .views import MenuItemView, SingleMenuItemView
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'bookings', views.BookingViewSet)

urlpatterns = [
   
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('', include(router.urls)),
]