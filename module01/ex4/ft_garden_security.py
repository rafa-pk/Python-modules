class SecurePlant:
    """SecurePlant class, defines plan objects and methods with
    encapsulated information"""
    def __init__(self, name: str, height: int, age: int) -> None:
        """initalization method, assigns characteristics to new object"""
        self.name = name
        self.__height = height
        self.__age = age

    def get_height(self) -> None:
        """encapsulation method to access __height"""
        return self.__height

    def get_age(self) -> None:
        """encapsulating method to access __age"""
        return self.__age

    def creation(self) -> None:
        """method which prints newly created plant"""
        print(f"Plant created: {self.name}")

    def set_height(self, new_height: int) -> None:
        """method to set new height safely"""
        if new_height < 0:
            print(f"\nInvalid operation attempted: height {new_height}cm"
                  f" [REJECTED]")
            print("Security: Negative height rejected\n")
        else:
            self.__height = new_height
            print(f"Height updated: {self.get_height()}cm [OK]")

    def set_age(self, new_age: int) -> None:
        """method to set new age safely"""
        if new_age < 0:
            print(f"\nInvalid operation attempted: age {new_age} days"
                  " [REJECTED]")
            print("Security: Negative age rejected\n")
        else:
            self.__age = new_age
            print(f"Age updated: {self.get_age()} days [OK]")


def ft_garden_security(name: str, height: int, age: int) -> None:
    """function which creates new SecurePlant, sets new ages and heights
    and displays characteristics"""
    print("=== Garden Security System ===")
    plant = SecurePlant(name, height, age)
    plant.creation()

    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-5)
    print(f"Current plant: {plant.name} ({plant.get_height()}cm, "
          f"{plant.get_age()} days)")


def main() -> None:
    """main function, called in entry point"""
    ft_garden_security("Rose", 15, 25)


if __name__ == "__main__":
    main()
