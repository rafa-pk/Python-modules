def recursive(current_day, harvest_days):

    if current_day > harvest_days:
        print("Harvest time!")
        return
    print(f"Day {current_day}")
    return recursive(current_day + 1, harvest_days)


def ft_count_harvest_recursive():

    harvest_days = int(input("Days until harvest: "))
    recursive(1, harvest_days)
