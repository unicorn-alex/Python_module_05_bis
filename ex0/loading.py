import importlib

# def install_message() -> None:
#     To install {module} in pip, type in command line:
#         pip install {module}
        

def main() -> None:
    print("REAGENT STATUS: Loading reagents...\n")
    print("Checking dependencies:")

    try:
        pandas_mod = importlib.import_module("pandas")
    except ImportError:
        pass
    try:
        numpy_mod = importlib.import_module("numpy")
    except ImportError:
        pass


    
if __name__ == "__main__":
    main()