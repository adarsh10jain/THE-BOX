from django.urls import path
from . import views



urlpatterns = [

    path('',views.index,name="Shophome"),
    path('about/',views.about,name="About"),
    path('contact/',views.contact,name="Contact"),
    path('categories/',views.categories,name="categories"),
    path('search/',views.search,name="Search"),
    path('productview/<int:myid>',views.productview,name="Productview"),
    path('cart/',views.cart,name="Cart"),

]
