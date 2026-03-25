# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from apps.courses.models import Course
from apps.courses.serializers import CourseSerializer


class CourseListView(GenericAPIView):
    
    def get_queryset(self):
        courses=Course.objects.select_related("author","banner","category").prefetch_related("course_tags__tag").all()
        return courses

    def get(self,request,*args,**kwargs):
        queryset=self.get_queryset()
        serializer=CourseSerializer(queryset,many=True)

        return Response({"courses":serializer.data},status=status.HTTP_200_OK)


        