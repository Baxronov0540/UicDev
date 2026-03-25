from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
urlpatterns = [
    path("", include("apps.accounts.urls")),
    path("admin/", admin.site.urls),
    path("schema/docs/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="docs"),
    path("common/",include("apps.common.urls")),
    path("courses/",include("apps.courses.urls"))
]
