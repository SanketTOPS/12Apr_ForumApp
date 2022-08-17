from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index),
    path('notes/',views.notes,name='notes'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('userlogout/',views.userlogout),
    path('updateprofile/',views.updateprofile),
    path('custom_error/',views.custom_error,name='custom_error'),
]

