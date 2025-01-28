import subprocess
import time
import os

directory = "/home/masked/Dev"

windows_path = subprocess.check_output(['wslpath', '-w', directory]).decode().strip()


def create_py_project(name):

    subprocess.run(["mkdir", name], cwd=directory)

    new_directory = os.path.join(directory, name)

    subprocess.run(['python3', '-m', 'venv', 'venv'], cwd=new_directory)

    subprocess.run(['touch', 'main.py'], cwd=new_directory)
    
    subprocess.run(['code', '.'], cwd=new_directory)
