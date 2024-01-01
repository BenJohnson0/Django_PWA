from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from . import app_settings
from .models import Hotel
from .serializers import HotelSerializer
from django.contrib.gis.geos import Point
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="location")


class ListCreateGenericViews(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def perform_create(self, serializer):
        address = serializer.initial_data["address"]
        g = geolocator.geocode(address)
        lat = g.latitude
        lng = g.longitude
        pnt = Point(lng, lat)
        serializer.save(location=pnt)


class HotelUpdateRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def perform_update(self, serializer):
        address = serializer.initial_data["address"]
        g = geolocator.geocode(address)
        lat = g.latitude
        lng = g.longitude
        pnt = Point(lng, lat)
        serializer.save(location=pnt)


class HotelListView(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class HotelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class HotelUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def perform_update(self, serializer):
        address = serializer.initial_data["address"]
        g = geolocator.geocode(address)
        lat = g.latitude
        lng = g.longitude
        pnt = Point(lng, lat)
        serializer.save(location=pnt)


class HotelDeleteView(generics.DestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


def service_worker(request):
    response = HttpResponse(
        open(app_settings.PWA_SERVICE_WORKER_PATH).read(), content_type="application/javascript"
    )
    return response


def manifest(request):
    return render(
        request,
        "manifest.json",
        {
            setting_name: getattr(app_settings, setting_name)
            for setting_name in dir(app_settings)
            if setting_name.startswith("PWA_")
        },
        content_type="application/json",
    )


def offline(request):
    return render(request, "offline.html")


def map_view(request):
    return render(request, 'map.html')
