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



def execute_java(java_file, input_file_location) -> Execution:
    # Generate java compile command
    # javac {filename}
    # If error return Execution with error then only
    # If successful, generate command for java run
    # java ClassName
    # If error return Execution with error then only
    # Else return True, with response from execution

    execution_command = f"javac ./code/{java_file}".split(' ')
    execution_status = True
    try:
        execution_response = subprocess.check_output(execution_command, stderr=subprocess.PIPE).decode('utf-8')
    except subprocess.CalledProcessError as e:
        return Execution(
            False, e.stderr.decode('utf-8')
        )

    execution_command = f"java -cp ./code Solution".split(' ')
    execution_status = True
    try:
        execution_response = subprocess.check_output(execution_command, stdin=open(f"./code/{input_file_location}", 'r'), stderr=subprocess.PIPE).decode('utf-8')
    except subprocess.CalledProcessError as e:
        return Execution(
            False, e.stderr.decode('utf-8')
        )
    return Execution(
        execution_status,
        execution_response
    )

def execute_cpp(cpp_file, input_file_location) -> Execution:
    # Generate java compile command
    # javac {filename}
    # If error return Execution with error then only
    # If successful, generate command for java run
    # java ClassName
    # If error return Execution with error then only
    # Else return True, with response from execution

    execution_command = f"g++ -o ./code/a.out ./code/{cpp_file}".split(' ')
    execution_status = True
    try:
        execution_response = subprocess.check_output(execution_command, stderr=subprocess.PIPE).decode('utf-8')
    except subprocess.CalledProcessError as e:
        return Execution(
            False, e.stderr.decode('utf-8')
        )

    execution_command = f"./code/a.out".split(' ')
    execution_status = True
    try:
        execution_response = subprocess.check_output(execution_command, stdin=open(f"./code/{input_file_location}", 'r'), stderr=subprocess.PIPE).decode('utf-8')
    except subprocess.CalledProcessError as e:
        return Execution(
            False, e.stderr.decode('utf-8')
        )
    return Execution(
        execution_status,
        execution_response
    )

