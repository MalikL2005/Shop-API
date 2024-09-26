from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('shop', views.view_shop_items.as_view(), name='view_shop_items'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('sign-up/validate/', views.validate_sign_up, name='validate_sign-up'),
    path('cart', views.view_cart , name='cart'),
    path('cart/add_item/<int:pk>', views.add_item_to_cart),
]