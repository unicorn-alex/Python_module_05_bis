import importlib

#dodac install message dla Poetry

def error_message(module) -> str:
    return (f"[KO] {module} - the module is missing\n" +
            f"     To install {module} in pip, type in command line:\n" +
            f"         pip install {module}")


def main() -> None:
    print("REAGENT STATUS: Loading reagents...\n")
    print("Checking dependencies:")
    pandas_present = False
    numpy_present = False
    try:
        pandas_mod = importlib.import_module("pandas")
    except ImportError:
        print(error_message("pandas"))
    else:
        pandas_present = True
        print(f"[OK] pandas {pandas_mod.__version__}",
              "- Data manipulation ready")
    try:
        numpy_mod = importlib.import_module("numpy")
    except ImportError:
        print(error_message("numpy"))
    else:
        numpy_present = True
        print(f"[OK] numpy {numpy_mod.__version__}",
              "- Numerical computation ready")

    print('''\npip vs Poetry:
  requirements.txt declares what to install; pip resolves it at install time.
  pyproject.toml declares the same constraints, and Poetry pins the resolved
  versions in poetry.lock so every install is identical.''')

    if pandas_present is False or numpy_present is False:
        print("\nSome reagents are missing.")
    else:
        print("\nAll reagents present and accounted for.")


if __name__ == "__main__":
    main()
