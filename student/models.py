from django.db import models
from student.choices import LanguageChoice


# Create your models here.
class Problem(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    test_case = models.TextField()
    output = models.TextField()

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=255)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Run(models.Model):
    language = models.CharField(max_length=10, choices=[
        (language.value['key'], language.value['verbose']) for language in LanguageChoice
    ])
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, null=True, blank=True)
    status = models.BooleanField()
    code = models.TextField()

    def __str__(self):
        return f"{self.problem.title} - {self.language}"
