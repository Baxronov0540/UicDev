from django.urls import path

from apps.courses.apis import (
    CourseListApiView,
    CourseCreateApiView,
    CourseUpdateApiView,
    CourseDetaileApiView,
    CourseDeleteApiView,
    CategoryListApiView,
    CategoryCreateApiView,
    CategoryUpdateApiView,
    CategoryDetaileApiView,
    CategoryDeleteApiView,
    TagListApiView,
    TagCreateApiView,
    TagUpdateApiView,
    TagDetaileApiView,
    TagDeleteApiView,
)


urlpatterns = [
    path("courses", CourseListApiView.as_view(), name="courses"),
    path("course/create", CourseCreateApiView.as_view(), name="course-create"),
    path("course/update/<int:pk>", CourseUpdateApiView.as_view(), name="course-update"),
    path("course/detaile/<int:pk>", CourseDetaileApiView.as_view(), name="course-detaile"),
    path("course/delete/<int:pk>", CourseDeleteApiView.as_view(), name="course-delete"),
    path("categories", CategoryListApiView.as_view(), name="categories"),
    path("categories/create", CategoryCreateApiView.as_view(), name="categories-create"),
    path("categories/update/<int:pk>", CategoryUpdateApiView.as_view(), name="categories-update"),
    path("categories/detaile/<int:pk>", CategoryDetaileApiView.as_view(), name="categories-detaile"),
    path("categories/delete/<int:pk>", CategoryDeleteApiView.as_view(), name="categories-delete"),
    path("tags", TagListApiView.as_view(), name="tags"),
    path("tags/create", TagCreateApiView.as_view(), name="tags-create"),
    path("tags/update/<int:pk>", TagUpdateApiView.as_view(), name="tags-update"),
    path("tags/detaile/<int:pk>", TagDetaileApiView.as_view(), name="tags-detaile"),
    path("tags/delete/<int:pk>", TagDeleteApiView.as_view(), name="tags-delete"),
]
