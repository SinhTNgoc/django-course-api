from pyexpat import model
from re import U
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

# Base


class ModalBase(models.Model):
    subject = models.CharField(max_length=225, null=False)
    image = models.ImageField(upload_to="courses/%Y/%m", default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    # override tostring
    def __str__(self):
        return self.subject

    class Meta:
        abstract = True


class User(AbstractUser):
    avatar = models.ImageField(upload_to='uploads/%Y/%m')


class Category(models.Model):
    name = models.CharField(max_length=200, null=False, unique=True)

    def __str__(self):
        return self.name


class Course(ModalBase):
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)  # Khi xoa Category --> Course van con ton tai va dc set gia tri null

    class Meta:
        unique_together = ('subject', 'category')
        ordering = ['-id']


class Lesson(ModalBase):
    course = models.ForeignKey(
        Course, related_name='lessons', on_delete=models.CASCADE)
    tags = models.ManyToManyField(
        'Tag', related_name='lessons', blank=True, null=True)
    content = models.TextField()

    class Meta:
        unique_together = ('subject', 'course')


class Tag(model.Model):
    name = models.CharField(max_length=50, unique=True)
