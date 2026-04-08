def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """uses sorted() with a lambda to sort by power level"""
    return sorted(artifacts, key=lambda field: field["power"],
                  reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """use filter() with a lambda to find mages with power >= min_power"""
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """use map() with a lambda to add '*' prefix and suffix"""
    return list(map(lambda x: '*' + x + '*', spells))


def mage_stats(mages: list[dict]) -> dict:
    """use lambdas with max(), min() to find stuff"""
    return {
        'max_power': max(mages, key=lambda mage: mage["power"])["power"],
        'min_power': min(mages, key=lambda mage: mage["power"])["power"],
        'avg_power': round(sum(mage["power"] for mage in mages)
                           / len(mages), 2),
    }


def main() -> None:
    """main function, testing script"""
    print("\nTesting artifact sorter...")

    artifacts = [{'name': 'Storm Crown', 'power': 90, 'type': 'focus'},
                 {'name': 'Lightning Rod', 'power': 107, 'type': 'focus'},
                 {'name': 'Water Chalice', 'power': 83, 'type': 'focus'},
                 {'name': 'Crystal Orb', 'power': 74, 'type': 'weapon'}]
    mages = [{'name': 'River', 'power': 89, 'element': 'fire'},
             {'name': 'Phoenix', 'power': 81, 'element': 'light'},
             {'name': 'Sage', 'power': 75, 'element': 'shadow'},
             {'name': 'Sage', 'power': 69, 'element': 'lightning'},
             {'name': 'Nova', 'power': 98, 'element': 'wind'}]
    spells = ['blizzard', 'flash', 'heal', 'tornado']

    sorted_artifacts = artifact_sorter(artifacts)
    print(f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']} "
          f"power) comes before {sorted_artifacts[1]['name']} "
          f"({sorted_artifacts[1]['power']} power)")

    filtered_mages = power_filter(mages, 80)
    print("\nTesting power filter...")
    print(filtered_mages)

    print("\nTesting spell transformer...")
    print(spell_transformer(spells))

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(stats)


if __name__ == "__main__":
    main()
