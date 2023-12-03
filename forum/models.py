from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here o tablas. En el nombre de las clases la primera mayus. Domain _ Las cosas que maneja algo.
class Teacher(models.Model):
    name = models.CharField(max_length = 200)
    rol = models.CharField(max_length = 400)

    def __str__(self):
        return str(self.name)

class Student(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return str(self.name)

class Post(models.Model):
    title = models.CharField(max_length = 200)
    Content = models.TextField()
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    published_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.title)
    
"""class Commenters(models.Model):
    author_student = models.ForeignKey(Student, on_delete=models.CASCADE)
    author_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        names_people = f'{self.author_student} {self.author_teacher}'
        return str(names_people)
"""

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_at = models.DateTimeField(default=timezone.now)
    votes_good = models.IntegerField(default=0)
    votes_bad = models.IntegerField(default=0)

    #Con que palabras claves yo puedo expresar los votos en el ORM de Django.

    def __str__(self):
        return str(self.content)
    



    