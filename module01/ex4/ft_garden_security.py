class SecurePlant:
    
    def __init__(self, name, height, age):
        
        self.name = name
        if height < 0:
            print("Security: Negative height rejected")
        else:
            self.height = height

        if age < 0:
            print("Security: Negative age rejected")
        else:
            self.age = age
        print(f"Plant created: {self.name}")


    def get_height(self):
        print(f"{self.name} height: {self.height}cm")


    def get_age(self):
        print(f"{self.name} age: {self.age} days")


    def set_height(self, new_height):
    
        if new_height < 0:
            print(f"\nInvalid operation attempted: height {new_height}cm"
                    " [REJECTED]")
            print("Security: Negative height rejected\n")
        else:
            self.height = new_height
            print(f"Height updated: {self.height}cm [OK]")


    def set_age(self, new_age):

        if new_age < 0:
            print(f"\nInvalid operation attempted: age {new_age} days" 
                  " [REJECTED]")
            print("Security: Negative age rejected\n")
        else:
            self.age = new_age
            print(f"Age updated: {self.age} days [OK]")


def ft_garden_security(name: str, height: int, age: int):

    print("=== Garden Security System ===")
    plant = SecurePlant(name, height, age)

    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-5)
    print(f"Current plant: {plant.name} ({plant.height}cm, {plant.age} days)")
    
def main():
    ft_garden_security("Rose", 15, 25)

if __name__ == "__main__":
    main()
