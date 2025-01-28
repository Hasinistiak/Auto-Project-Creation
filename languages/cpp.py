import subprocess
import time
import os

directory = "/home/masked/Dev"

windows_path = subprocess.check_output(['wslpath', '-w', directory]).decode().strip()


def create_cpp_project(name):

    subprocess.run(["mkdir", name], cwd=directory)

    new_directory = os.path.join(directory, name)

    subprocess.run(['mkdir', 'src', 'include', 'build'], cwd=new_directory)

    subprocess.run(['touch', 'src/main.cpp', 'include/myheader.h'], cwd=new_directory)
    
    subprocess.run(['code', '.'], cwd=new_directory)