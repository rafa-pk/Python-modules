def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> str | None:
    """function which makes necessary checks and raises errors"""
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")
    elif water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    elif water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    elif sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    elif sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too high "
                         f"(max 12)")
    else:
        return f"Plant '{plant_name}' is healthy!\n"


def test_plant_checks() -> None:
    """tester function for error handling"""
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    try:
        print(check_plant_health("Tomato", 5, 6))
    except ValueError as message:
        print(f"Error: {message}\n")
    print("Testing empty plant name...")
    try:
        print(check_plant_health("", 5, 6))
    except ValueError as message:
        print(f"Error: {message}\n")
    print("Testing bad water level...")
    try:
        print(check_plant_health("Tomato", 15, 6))
    except ValueError as message:
        print(f"Error: {message}\n")
    print("Testing bad sunlight hours...")
    try:
        print(check_plant_health("Tomato", 5, 0))
    except ValueError as message:
        print(f"Error: {message}\n")
    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
