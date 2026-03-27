# Create your views here.
from rest_framework.generics import (
    GenericAPIView,
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
)
from rest_framework.response import Response
from rest_framework import status

from apps.courses.models import Course, Category, Tag
from apps.courses.apis import CourseSerializer, CategorySerializer, TagSerializer


class CourseListApiView(GenericAPIView):
    def get_queryset(self):
        courses = (
            Course.objects.select_related("author", "banner", "category").prefetch_related("course_tags__tag").all()
        )
        return courses

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CourseSerializer(queryset, many=True)

        return Response({"courses": serializer.data}, status=status.HTTP_200_OK)

class CourseCreateApiView(GenericAPIView):
    serializer_class=CourseSerializer
    def post(request,*args,**kwargs):
        data=request.data
        serializer=CourseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data},status=status.HTTP_201_CREATED)
        return Response({"message":serializer.errors},status=status.HTTP_400_BAD_REQUEST)

class CourseUpdateApiView(UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetaileApiView(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDeleteApiView(DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CategoryListApiView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryCreateApiView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryUpdateApiView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetaileApiView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDeleteApiView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagListApiView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagCreateApiView(CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagUpdateApiView(UpdateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetaileApiView(RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDeleteApiView(DestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
