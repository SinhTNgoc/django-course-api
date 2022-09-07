from dataclasses import field
from urllib import request
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Category, Course, Lesson


class CategorySerialize(ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class CourseSerialize(ModelSerializer):
    image = SerializerMethodField()

    def get_image(self, obj):
      # get request in serializers from ViewSet
        request = self.context['request']
        name = obj.image.name
        if name.startswith('static/'):
            path = '/%s' % name
        else:
            path = '/static/%s' % name

      # add http://localhost:3000 to path
        return request.build_absolute_uri(path)

    class Meta:
        model = Course
        fields = ['id', 'subject', 'created_at', 'image', 'category']


class LessonSerializer(ModelSerializer):
   class Meta:
      model = Lesson
      fields = ['id','subject','image','created_at','updated_at','course']