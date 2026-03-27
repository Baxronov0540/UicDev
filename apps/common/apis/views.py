from rest_framework.generics import (
    GenericAPIView,
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
)
from rest_framework.response import Response
from rest_framework import status

from apps.common.models import Country, Region
from apps.common.apis.serializers import CountrySerializer, RegionSerializer


class CountryListAPiViews(ListAPIView):
    queryset = Country.objects.all().order_by("name")
    serializer_class = CountrySerializer


class CountryCreateApiViews(CreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryUpdateApiViews(UpdateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = "id"


class CountryDetailApiViews(DestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = "id"


class CountryDeleteApiViews(RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = "id"


class RegionListApiViews(ListAPIView):
    queryset = Region.objects.all().order_by("name")
    serializer_class = RegionSerializer


class RegionCreateApiViews(CreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class RegionUpdateApiViews(UpdateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class RegionDetailApiViews(RetrieveAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class RegionDeleteApiViews(DestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
