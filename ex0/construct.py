import sys
import os
import site

#dlaczego mypy tutaj nie gra

def main() -> None:
    print("LABORATORY STATUS: ", end="")
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
