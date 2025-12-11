class SecurePlant:
    
    def __init__(self, name, height, age)
        
        self.name = name
        if height < 0:
            print("Security: Negative height rejected")
        else:
            self.height = height

        if age < 0:
            print("Security: Negative age rejected")
        else:
            self.age = age


    def get_height(self)
        print(f"{self.name} height: {self.height}cm")


    def get_age(self)
        print(f"{self.name} age: {self.age} days")


    def set_height(height)
    
        if height < 0:
            print(f"Invalid operation attempted: height {self.height}cm"
                    "[REJECTED]")
        else:
            self.height = height
            print(f"Height updated: {self.height}cm [OK]")


    def set_age(age):

        if age < 0:
            print(f"Invalid operation attempted: age {self.age} days" 
                  "[REJECTED]")
        else:
            self.age = age
            print(f"Age updated: {self.age} days [OK]")


def ft_garden_security():
