def recursive(current_day: int, harvest_days: int) -> None:
    if current_day > harvest_days:
        print("Harvest time!")
        return
    print(f"Day {current_day}")
    recursive(current_day + 1, harvest_days)


def ft_count_harvest_recursive() -> None:
    harvest_days = int(input("Days until harvest: "))
    recursive(1, harvest_days)
