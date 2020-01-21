from django.contrib import admin

# Register your models here.
from student.models import Problem, Student, Run


class AdminRun(admin.ModelAdmin):
    list_display = ('problem', 'language', 'student', 'status')
    list_filter = ('problem', 'language', 'student', )


class AdminStudent(admin.ModelAdmin):
    list_display = ('name', 'email')


class AdminProblem(admin.ModelAdmin):
    list_display = ('title', 'description')


admin.site.register(Problem, AdminProblem)
admin.site.register(Student, AdminStudent)
admin.site.register(Run, AdminRun)
