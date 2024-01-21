import sys
import subprocess
import importlib.metadata

def get_python_info():
    print("Python Version:")
    print(sys.version)
    print("\n")

    print("Python Executable Path:")
    print(sys.executable)
    print("\n")

    print("Python System Path:")
    for path in sys.path:
        print(path)
    print("\n")

    print("List of Installed Packages:")
    installed_packages = sorted(["%s==%s" % (dist.metadata['Name'], dist.version) for dist in importlib.metadata.distributions()])
    for package in installed_packages:
        print(package)

def get_pip_info():
    try:
        pip_output = subprocess.check_output([sys.executable, '-m', 'pip', 'list'])
        print("\nPip Packages:")
        print(pip_output.decode())
    except subprocess.CalledProcessError as e:
        print("Error occurred while trying to list pip packages:", e)

if __name__ == "__main__":
    get_python_info()
    get_pip_info()
