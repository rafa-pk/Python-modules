def check_temperature(temp_str: str) -> int | None:
    """tries to convert str to nb and checks for errors"""
    try:
        temp = int(temp_str)
    except Exception:
        print(f"Error: '{temp_str}' is not a valid number\n")
    else:
        if temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)\n")
        elif temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)\n")
        else:
            print(f"Temperature {temp}°C is perfect for plants!\n")


def test_temperature_input() -> None:
    """testing function which shows good and bad input"""
    temps_to_test = ["25", "abc", "100", "-50"]

    print("=== Garden Temperature Checker ===\n")
    for temp in temps_to_test:
        print(f"Testing temperature: {temp}")
        check_temperature(temp)
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    """programs entry point, calls tester function"""
    test_temperature_input()
