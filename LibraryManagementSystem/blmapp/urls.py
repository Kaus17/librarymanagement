from django.contrib import admin
from django.urls import path
from .views import homepageview, addbookview, addbook, editbook

urlpatterns = [
    path('', homepageview),
    path('add-book/', addbookview),
    path('addbook/', addbook),
    path('edit-book/', editbookview),
    path('edit-book/', editbook),
]
