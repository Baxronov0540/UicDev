from django.urls import path
from apps.common.views import CountryListView,RegionListView

urlpatterns=[
    path("countries",CountryListView.as_view(),name="countries"),
    path("regions",RegionListView.as_view(),name="regions")
]