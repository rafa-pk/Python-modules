import sys


def main() -> None:
    """main function, program orchestrator"""
    if len(sys.argv) == 1:
        print("No arguments provided.\nRun: python3 ft_inventory_system.py "
              "<key:value> ...")
        sys.exit()
    inventory = dict()
    total_items = 0
    most_abundant_key = None
    most_abundant_value = 0
    least_abundant_key = None
    least_abundant_value = 0

    for entry in sys.argv[1:]:
        key_and_value = entry.split(":")
        total_items += int(key_and_value[1])
        inventory[key_and_value[0]] = int(key_and_value[1])
    dict_pairs = inventory.items()
    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventory)}")
    print("\n=== Current Inventory ===")
    for pair in dict_pairs:
        print(f"{pair[0]}: {pair[1]} units ("
              f"{pair[1] / total_items * 100:.1f}%)")
    print("\n=== Inventory Statistics ===")
    for key, value in dict_pairs:
        if most_abundant_key is None or value > most_abundant_value:
            most_abundant_key = key
            most_abundant_value = value
        if least_abundant_key is None or value < least_abundant_value:
            least_abundant_key = key
            least_abundant_value = value
    print(f"Most abundant: {most_abundant_key} ({most_abundant_value} items)")
    print(f"Least abundant: {least_abundant_key} ("
          f"{least_abundant_value} items)")
    print("\n=== Item Categories ===")
    mod = dict()
    sca = dict()
    for key, value in dict_pairs:
        if value <= 3:
            sca.update({key: value})
        else:
            mod.update({key: value})
    print(f"Moderate: {mod}")
    print(f"Scarce: {sca}")
    print("\n=== Management Suggestions ===")
    restock = dict()
    for key, value in sca.items():
        if value == 1:
            restock.update({key: value})
    print(f"Restock needed: {list(restock.keys())}")
    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {list(inventory.keys())}")
    print(f"Dictionary values: {list(inventory.values())}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}!")


if __name__ == "__main__":
    main()
