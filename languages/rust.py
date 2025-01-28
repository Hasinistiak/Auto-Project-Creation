import subprocess
import time
import os

directory = "/home/masked/Dev"

windows_path = subprocess.check_output(['wslpath', '-w', directory]).decode().strip()


def create_rust_project(name):

    subprocess.run(['cargo', 'new', name], cwd = directory)

    new_directory = os.path.join(directory, name)
    
    subprocess.run(['code', '.'], cwd=new_directory)