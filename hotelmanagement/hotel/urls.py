from django.urls import path
from . import views
urlpatterns=[
    path('hotel/',views.hotel,name='hotel'),
    path('hotel/About/',views.about,name='about'),
    path('hotel/Room/',views.roominfo,name='roominfo'),
    path('hotel/booking/',views.booking,name='booking'),
    path('hotel/Contact/',views.contact,name='contact'),
]