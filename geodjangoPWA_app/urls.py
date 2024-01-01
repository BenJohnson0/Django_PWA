from django.urls import path

from .views import (
    ListCreateGenericViews,
    HotelUpdateRetrieveView,
    HotelListView,
    HotelDetailView,
    HotelUpdateView,
    HotelDeleteView,
    map_view,
)

urlpatterns = [
    path('hotels/', ListCreateGenericViews.as_view(), name='hotel-list-create'),
    path('hotels/<int:pk>/', HotelUpdateRetrieveView.as_view(), name='hotel-update-retrieve'),
    path('hotels/<int:pk>/update/', HotelUpdateView.as_view(), name='hotel-update'),
    path('hotels/<int:pk>', HotelDeleteView.as_view(), name='hotel-delete'),
    path('hotels/all/', HotelListView.as_view(), name='hotel-list'),
    path('hotels/<int:pk>/detail/', HotelDetailView.as_view(), name='hotel-detail'),
    path("map/", map_view, name="map"),
]
