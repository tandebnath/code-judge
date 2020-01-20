
"""
def user_is_entry_author(function):
    def wrap(request, *args, **kwargs):
        entry = Entry.objects.get(pk=kwargs['entry_id'])
        if entry.created_by == request.user:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
"""
from django.shortcuts import redirect

def is_login(function):
    def wrapper(request, *args, **kwargs):
        if not request.session.has_key('logged_in'):
            return redirect('/student')
        return function(request, *args, **kwargs)
    return wrapper


"""
arr = map(int, input().split())
for i in range(len(arr)):
    mp = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[mp]:
            mp = j
    arr[i], arr[mp] = arr[mp], arr[j]
print(arr)

def dec(function):
    def inner(*args, **kwargs):
        _args = []
        for a in args:
            if is_unsafe(a):
                _args.append(make_safe(a))
        return function(*_args, **kwargs)
    return inner

"""


# javac source.java
# java ClassName > 

# g++ source.c/souce.cpp
# ./source > out