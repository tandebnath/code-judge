import subprocess
from collections import namedtuple

Execution = namedtuple('Execution', ['status', 'response'])


def write_content(filename, content: str):
    base_location = 'code/'
    with open(f'{base_location}{filename}', 'w', newline='\n') as myfile:
        myfile.write(content)


def execute_python(python_file, input_file_location) -> Execution:
    """
    Executes python code over input location and returns the output from the program
    :param python_file: Location of python file with code
    :param input_file_location: Location of input file
    :return:
    """
    execution_command = f"python3 ./code/{python_file}".split(' ')
    execution_status = True
    try:
        execution_response = subprocess.check_output(execution_command, stdin=open(f"./code/{input_file_location}", 'r'), stderr=subprocess.PIPE).decode('utf-8')
    except subprocess.CalledProcessError as e:
        execution_status = False
        execution_response = e.stderr.decode('utf-8')
    return Execution(
        execution_status,
        execution_response
    )

# javac source.java
# java ClassName > 

# g++ source.c/souce.cpp
# ./source > out