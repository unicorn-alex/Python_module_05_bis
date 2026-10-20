import sys
import os
import site

def main() -> None:
    print("LABORATORY STATUS: ", end="")
    #o co chodzi
    if sys.prefix != sys.base_prefix:
        print("The laboratory is sealed\n")
        virtual_env = True
    else:
        print("You are working in the open\n")
        virtual_env = False
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: ", end="")
    if virtual_env is True:
        path_to_env = os.getenv("VIRTUAL_ENV")
        print(os.path.basename(path_to_env))
        print(f"Environment Path: {path_to_env}\n")
    else:
        print("None detected\n")

    if virtual_env is True:
        print('''SUCCESS: You are working in an isolated environment!
Safe to install reagents without affecting
the global system.

Reagent installation path:''')
        #o chuja chodzi
        print(site.getsitepackages()[0])
    else:
        print('''WARNING: You are in the global environment!
Every reagent you install here leaks into the whole system.

To seal the laboratory, run:
python3 -m venv lab_env
source lab_env/bin/activate # On Unix
lab_env\\Scripts\\activate # On Windows

Then run this program again.''')


if __name__ == "__main__":
    main()

# https://docs.python.org/3/library/venv.html
# When a Python interpreter is running from a virtual environment, sys.prefix and sys.exec_prefix point to the directories of the virtual environment, whereas sys.base_prefix and sys.base_exec_prefix point to those of the base Python used to create the environment.
#import lib i getattr