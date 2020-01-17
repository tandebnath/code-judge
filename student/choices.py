import enum
from collections import namedtuple
from .utils import execute_python

class LanguageChoice(enum.Enum):
    JAVA = {
        'verbose': 'Java',
        'key': 'java',
        'extension': 'java'
    }
    CPP = {
        'verbose': 'C/C++',
        'key': 'c_cpp',
        'extension': 'cpp'
    }
    PYTHON = {
        'verbose': 'Python3.6',
        'key': 'python',
        'extension': 'py',
        'execution': execute_python
    }



