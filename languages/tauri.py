import subprocess
import os
import pexpect

directory = "/home/masked/Dev"

windows_path = subprocess.check_output(['wslpath', '-w', directory]).decode().strip()


def create_tauri_project(name):

    child = pexpect.spawn(
        f'npm create tauri-app@latest {name} -- --template react --manager npm --flavor javascript --name {name}',
        cwd=directory,
        encoding='utf-8',
    )

    child.expect("Identifier.*›")
    child.sendline(f"com.{name}.app")

    child.wait()

    new_directory = os.path.join(directory, name)
    subprocess.run(['code', '.'], cwd=new_directory)
