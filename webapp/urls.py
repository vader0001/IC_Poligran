from django.contrib import admin
from django.urls import path
import webapp.views as views


urlpatterns = [
    path('', views.welcome),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('admin/', admin.site.urls),
    path('catalog', views.ItemListView.as_view(), name='item-list'),
    path('item/<int:pk>', views.ItemDetailView.as_view(), name='item-detail'),
    path('order_item/<int:pk>', views.OrderItemView, name='item-order'),
    path('order/<int:pk>', views.OrderDetailView.as_view(), name='order-detail'),
    path('orders', views.OrderListView.as_view(), name='order-list'),
]