def garden_operations(error: str) -> None:
    """function which triggers errors based on given argument"""
    if error == "value":
        int("abc")
    elif error == "zerodiv":
        42 / 0
    elif error == "file":
        file = open("missing.txt")
        file.close()
    elif error == "key":
        dic = {"key1": "val1", "key2": "val2"}
        dic["missing_plant"]


def test_error_types() -> None:
    """function which tests error handling for all
    error types triggered in garden_operations"""
    errors = {
            "value": ValueError,
            "zerodiv": ZeroDivisionError,
            "file": FileNotFoundError,
            "key": KeyError
            }

    print("=== Garden Error Types Demo ===\n")
    for flag, error in errors.items():
        print(f"Testing {error.__name__}...")
        try:
            garden_operations(flag)
        except (error) as ret:
            print(f"Caught {error.__name__}: {ret}\n")
    print("Testing multiple errors together...")
    try:
        garden_operations("value")
        garden_operations("zerodiv")
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!\n")
    print("All error types tested successfuly!")


if __name__ == "__main__":
    """program's entry point"""
    test_error_types()
