from django.contrib import admin
from django.urls import path, include

from geodjangoPWA_app.views import HotelListView, HotelDetailView, HotelUpdateView, HotelDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('geodjangoPWA_app.urls')),
    path('', include('pwa.urls')),
    path('api/v1/', include('geodjangoPWA_app.urls')),
    path('api/v1/hotels/', HotelListView.as_view(), name='hotel-list'),
    path('api/v1/hotels/<int:pk>/', HotelDetailView.as_view(), name='hotel-detail'),
    path('api/v1/hotels/<int:pk>/update/', HotelUpdateView.as_view(), name='hotel-update'),
    path('api/v1/hotels/<int:pk>/delete/', HotelDeleteView.as_view(), name='hotel-delete'),
]
