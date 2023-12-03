from django.contrib import admin
from .models import Post, Comment, Teacher, Student

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Teacher)
admin.site.register(Student)