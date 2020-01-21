import enum
from collections import namedtuple
from .utils import execute_python, execute_java, execute_cpp


class LanguageChoice(enum.Enum):
    JAVA = {
        'verbose': 'Java',
        'key': 'java',
        'extension': 'java',
        'execution': execute_java
    }
    CPP = {
        'verbose': 'C/C++',
        'key': 'c_cpp',
        'extension': 'cpp',
        'execution': execute_cpp
    }
    PYTHON = {
        'verbose': 'Python3.6',
        'key': 'python',
        'extension': 'py',
        'execution': execute_python
    }


class ExecutionStatusType(enum.Enum):

    COMPILE_ERROR = {
        'verbose': 'Compilation Error',
        'key': 'compile_error'
    }
    EXECUTION_ERROR = {
        'verbose': 'Execution Error',
        'key': 'execution_error'
    }
    INCORRECT_ANSWER = {
        'verbose': 'Incorrect Answer',
        'key': 'incorrect_answer'
    }
