from rest_framework.serializers import ModelSerializer
from apps.courses.models import Course, Category, Tag


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "description",
            "created_at",
            "author",
            "banner",
            "category",
            "reward_stars",
            "is_active",
            "is_published",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
