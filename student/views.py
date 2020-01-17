from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Problem, Run, Student
from .choices import LanguageChoice
import time
from .utils import write_content, Execution


def student_login(request):
    has_error = request.GET.get('error', None)
    return render(request, 'student_login.html', {'error': bool(has_error)})


def student_register(request):
    
    return render(request, 'student_register.html')

def on_register(request):
    register = Student(
        name= request.POST['username'],
        password= request.POST['password'],
        email= request.POST['email'],
        bio= request.POST['bio'],
    )

    register.save()

    return redirect('/student')


def check_login(request):
    username = request.POST['username']
    password = request.POST['password']

    try:
        student = Student.objects.get(name=username, password=password)
        request.session['logged_in'] = True
        request.session['student_name'] = student.name
        request.session['student_id'] = student.id
        return redirect('/student/problems')
    except ObjectDoesNotExist as e:
        return redirect('/student?error=true')

# Create your views here.


def problem_list(request):
    problems = Problem.objects.all()
    student = None
    if request.session.has_key('logged_in'):
        student = dict(request.session)
        print(student)
    return render(request, 'problem_list.html', {'problems': problems, 'student': student})


def problem_single(request, problem_id):
    try:
        problem = Problem.objects.filter(id=problem_id).get()
        lang = [language.value for language in LanguageChoice]
    except ObjectDoesNotExist as e:
        raise Http404()
    return render(request, 'problem_single.html', {'problem': problem, 'languages': lang})


def problem_solve(request, problem_id):
    language = request.POST['language']
    code = request.POST['code']

    # Fetch details about the problem
    try:
        problem = Problem.objects.filter(id=problem_id).get()
    except ObjectDoesNotExist as e:
        raise Http404()

    # Decide on filenames
    _language = list(
        filter(
            lambda _language: _language.value['key'] == language,
            [__language for __language in LanguageChoice]
        )
    )[0].value
    extension = _language['extension']
    execute = _language['execution']
    current_timestamp = int(time.time())
    db_input = f"{problem.id}-{current_timestamp}.in"
    code_location = f"{problem.id}-{current_timestamp}.{extension}"

    write_content(code_location, code)
    write_content(db_input, problem.test_case)

    execution: Execution = execute(code_location, db_input)

    # Check if execution is successful
    # If unsuccessful return error
    if not execution.status:
        return JsonResponse(execution._asdict())

    # Create new run
    run = Run(
        language=_language['key'],
        problem=problem,
        code=open(f"./code/{code_location}", 'r').read(),
        status=problem.output.splitlines() == execution.response.splitlines()
    )

    run.save()

    return redirect('/student/problems/runs')


def run_list(request):
    runs = Run.objects.all()
    return render(request, 'run_list.html', {'runs': runs})

def logout(request):
    request.session.flush()
    return redirect('/student/')

"""

def message_wrapper(*args, **kwargs):
    verb = args['verb']
    def inner(func, args):
        a = args['a']
        b = args['b']
        
        f_resp = func(a, b)
        
        return f"{verb} of {a} {b} is {f_resp}"
    return inner


@message_wrapper(verb = 'Addition')
def add(a, b): return a+b
@message_wrapper(verb = 'Subtraction')
def sub(a, b): return abs(a-b)
@message_wrapper(verb = 'Multiplication')
def mul(a, b): return m*b
@message_wrapper(verb = 'Division')
def div(a, b): return a/b



add(5, 10)


"Addition of {a}, {b} is {ans}"

for i in range(int(input())):
    print("Odd" if int(input())%2 else "Even")
"""
