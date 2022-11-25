from django.contrib import admin
from django.urls import path

from example.views import listing_update, listing_retrieve, listing_create, listing_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listing_list),
    path('listing/<pk>/', listing_retrieve),
    path('listing/<pk>/edit/', listing_update),
    path('add-listing/', listing_create),
]
