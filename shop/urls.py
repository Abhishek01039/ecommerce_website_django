
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='shopHome'),
    path('about/', views.about, name='About'),
    path('contact/', views.contact, name='Contact'),
    path('prodview/<int:id>', views.prodView, name="productView"),
    path("checkout/", views.checkout, name="Checkout"),
    path("search/", views.search, name="Search"),
    path("tracker/", views.tracker, name="Tracker")
]