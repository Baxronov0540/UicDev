from rest_framework import serializers
from apps.courses.models import Course

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model=Course
        fields=["id","name","description","price","created_at","author","banner","category","reward_stars","is_active","is_published"]
