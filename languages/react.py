import subprocess
import time
import os

directory = "/home/masked/Dev"

windows_path = subprocess.check_output(['wslpath', '-w', directory]).decode().strip()


def create_react_project(name):

    subprocess.run(f'echo "y" | npx create-react-app {name}', shell=True, cwd=directory)

    new_directory = os.path.join(directory, name)
    
    subprocess.run(['code', '.'], cwd=new_directory)