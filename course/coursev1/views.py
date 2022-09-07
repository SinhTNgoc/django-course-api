from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.decorators import action
from .models import Category, Course
from .serializers import CategorySerialize, CourseSerialize, LessonSerializer
from .paginate import BasePaginate
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerialize


class CourseViewSet(viewsets.ViewSet, generics.ListAPIView):
    serializer_class = CourseSerialize
    pagination_class = BasePaginate

    # override queryset
    def get_queryset(self):
        courses = Course.objects.filter(active=True)

        q = self.request.query_params.get('q')
        if q is not None:
            courses = courses.filter(subject__icontains=q)

        request_id = self.request.query_params.get('category_id')
        if request_id is not None:
            courses = courses.filter(category_id=request_id)

        return courses

    @action(methods=['get'], detail=True, url_path='lessons')
    def get_lessons(self, request, pk):
        # course = Course.objects.get(pk=pk)
        course = self.get_object()
        lessons = course.lessons.filter(active=True)

        kw = request.query_params.get('kw')
        if kw is not None:
            lessons = lessons.filter(subject__icontains=kw)

        return Response(LessonSerializer(lessons, many=True).data, status=status.HTTP_200_OK)


# /lessons/{lesson_id}

