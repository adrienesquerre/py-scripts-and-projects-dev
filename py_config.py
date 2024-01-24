import sys
import subprocess
import importlib.metadata

def get_python_info():
    print("Python Version:") # version of Python that's running the script
    print(sys.version)
    print("\n")

    print("Python Executable Path:") # file system path to the Python interpreter executable that's running the script
    print(sys.executable)
    print("\n")

    print("Python System Path:") # Lists the directories Python will search in for modules and packages. This is the sys.path
    for path in sys.path:
        print(path)
    print("\n")

    print("List of Installed Packages:")  # Python packages installed (visible to the current Python interpreter) along with their versions
    installed_packages = sorted(["%s==%s" % (dist.metadata['Name'], dist.version) for dist in importlib.metadata.distributions()])
    for package in installed_packages:
        print(package)

def get_pip_info():
    try:
        pip_output = subprocess.check_output([sys.executable, '-m', 'pip', 'list']) # Executes the command pip list using the subprocess module to get a list of installed pip packages
        print("\nPip Packages:")
        print(pip_output.decode())
    except subprocess.CalledProcessError as e:
        print("Error occurred while trying to list pip packages:", e)

if __name__ == "__main__":
    get_python_info()
    get_pip_info()

# Different Python Interpreters:
# If you run this script using different Python interpreters
# (for example, system Python vs. a Python version installed through Homebrew or a virtual environment),
# you'll see different paths, versions, and installed packages.