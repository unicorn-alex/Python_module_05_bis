import sys

def main() -> None:
    print("LABORATORY STATUS: ", end="")
    #o co tu chodzi
    print(sys.path)
    if sys.prefix != sys.base_prefix:
        print("The laboratory is sealed")
    else:
        print("You are working in the open")
    print("Current Python: ")

    print()


if __name__ == "__main__":
    main()

# https://docs.python.org/3/library/venv.html
# When a Python interpreter is running from a virtual environment, sys.prefix and sys.exec_prefix point to the directories of the virtual environment, whereas sys.base_prefix and sys.base_exec_prefix point to those of the base Python used to create the environment.