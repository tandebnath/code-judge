from django.contrib import admin

# Register your models here.
from student.models import Problem, Student, Run

admin.site.register(Problem)
admin.site.register(Student)
admin.site.register(Run)