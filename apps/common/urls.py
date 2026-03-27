from django.urls import path
from apps.common.apis import (
    CountryCreateApiViews,
    CountryDeleteApiViews,
    CountryDetailApiViews,
    CountryListAPiViews,
    CountryUpdateApiViews,
    RegionCreateApiViews,
    RegionDeleteApiViews,
    RegionDetailApiViews,
    RegionListApiViews,
    RegionUpdateApiViews,
)

urlpatterns = [
    path("country/list/", CountryListAPiViews.as_view(), name="countries"),
    path("country/create/", CountryCreateApiViews.as_view(), name="country-create"),
    path("country/<int:id>/", CountryUpdateApiViews.as_view(), name="country-update"),
    path("country/<int:id>/", CountryDetailApiViews.as_view(), name="country-detail"),
    path("country/<int:id>/", CountryDeleteApiViews.as_view(), name="country-delete"),
    path("region/list", RegionListApiViews.as_view(), name="regions"),
    path("region/<int:id>/", RegionDetailApiViews.as_view(), name="region-detail"),
    path("region/<int:id>/", RegionDeleteApiViews.as_view(), name="region-delete"),
    path("region/<int:id>/", RegionUpdateApiViews.as_view(), name="region-update"),
    path("region/create", RegionCreateApiViews.as_view(), name="region-create"),
]
