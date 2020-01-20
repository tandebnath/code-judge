# %% 
def dp(message, tag='DEBUG'):
    print(tag, message)

# %%
def my_dec(verb):
    dp(verb)
    def inner(function):
        # dp(function.__name__)
        def wrapper(a, b):
            # dp(args)
            # dp(kwargs)
            a = 0 
            b = 0
            result = function(a, b)
            return f"{verb} is {result}"
        return wrapper
    return inner

# %%
@my_dec(verb='Addition')
def add(a, b): return a+b

@my_dec(verb='Subtraction')
def sub(a, b): return a-b


# %%
print(add(a=10, b=20))
print(sub(a=50, b=30))

# %%
"""
non-param decorator @dec on function f(x)
def dec(function):
    def inner(*args, **kwargs):
        return function(*args, **kwargs)
    return inner


parameterized @dec(a, b) on function f(x)

def dec(a, b):
    def func_wrapper(f):
        def inner(*a, *kw):
            return f(*a, *kw)
        return inner
    return func_wrapper

"""

# %%
def zero_safe(function):
    def wrapper(a, b):
        if not b: 
            return "Hobe na bhai"
        return function(a, b)
    return wrapper

@zero_safe
def division(a, b):
    return a/b

# %%
def sub_abs(function):
    def inner(a, b):
        if b>a: return function(b, a)
        return function(a, b)
    return inner

@sub_abs
def sub(a, b):
    return a-b

# %%
import time
def gen(n):
    for i in range(n):
        time.sleep(3)
        yield i

def normal(n):
    arr = []
    for i in range(n):
        time.sleep(3)
        arr.append(i)
    return arr


# %%
genx = (i + int(time.sleep(3)) for i in range(30))

# %%
for i in genx:
    print(i)

# %%
