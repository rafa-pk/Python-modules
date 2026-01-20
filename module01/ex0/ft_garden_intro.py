def ft_garden_intro(name: str, height: int, age: int) -> None:
    '''This function takes a garden's plant name, height and age
    and displays its information'''
    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}\nHeight: {height}cm\nAge: {age} days\n")
    print("=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro("Rose", 178, 89)
