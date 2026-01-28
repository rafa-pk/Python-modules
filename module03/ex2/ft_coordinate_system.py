import sys
import math


def create_position(arg: str,
                    flag: bool) -> tuple[tuple[int, int, int], bool] | None:
    """function which takes command line arguments and returns a
    position tup"""
    points = arg.split(",")

    try:
        x = int(points[0])
        y = int(points[1])
        z = int(points[2])
        flag = True
        return (x, y, z), flag
    except ValueError as message:
        print(f"Error parsing coordinates: {message}")
        print(f"Error details - Type: {type(message).__name__}, Args: "
              f"{message}\n")
        return (0, 0, 0), flag


def calculate_distance(base: tuple[int, int, int],
                       point: tuple[int, int, int]) -> None:
    """function to calculate euclidean formula"""
    x1, y1, z1 = base
    x2, y2, z2 = point
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    print(f"Distance between point {base} and {point}: {distance:.2f}\n")


def unpacking_demo(pos: tuple[int, int, int]) -> None:
    x, y, z = (pos)
    print(f"Player at x={x}, y={y}, z={z}")
    X, Y, Z = (pos)
    print(f"Coordinates: X={X}, Y={Y}, Z={Z}")


def main() -> None:
    """main function, program orchestrator"""
    ac = len(sys.argv)
    base_coordinate = (0, 0, 0)
    invalid_coordinate = "abc, def, ghi"
    flag = False

    print("=== Game Coordinate System ===")
    if not ac == 3:
        print("Error: Wrong number of arguments (2 required)")
        return
    pos, flag = create_position(sys.argv[1], flag)
    print(f"\nPosition created: {pos}")
    calculate_distance(base_coordinate, pos)
    print(f'Parsing coordinates: "{sys.argv[2]}"')
    pos2, flag = create_position(sys.argv[2], flag)
    if flag:
        print(f"Parsed position: {pos2}")
    calculate_distance(base_coordinate, pos2)
    print(f'Parsing invalid coordinates: "{invalid_coordinate}"')
    pos3, flag = create_position(invalid_coordinate, flag)
    unpacking_demo(pos2)


if __name__ == "__main__":
    main()
