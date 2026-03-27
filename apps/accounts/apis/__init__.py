from .serializers import EducationSerializer, AuthorSerializer
from .views import (
    EducationCreateApiViews,
    EducationDeleteApiViews,
    EducationDetailApiViews,
    EducationListApiViews,
    EducationUpdateAPiViews,
    AuthorCreateApiViews,
    AuthorDeleteApiViews,
    AuthorDetailApiViews,
    AuthorListApiViews,
    AuthorUpdateApiViews,
)

__all__ = [
    "EducationSerializer",
    "EducationCreateApiViews",
    "EducationDeleteApiViews",
    "EducationDetailApiViews",
    "EducationListApiViews",
    "EducationUpdateAPiViews",
    "AuthorListApiViews",
    "AuthorCreateApiViews",
    "AuthorDetailApiViews",
    "AuthorUpdateApiViews",
    "AuthorDeleteApiViews",
    "AuthorSerializer",
]
