# # values of a quadrilateral

# a, b, c, d = input("Enter the values of four sides of a quadrilateral (space-separated for each value): ").split()

# a = float(a)
# b = float(b)
# c = float(c)
# d = float(d)

# print("Imported values: ", a, b, c, d)


## Classes and objects
# # Approach 1
'''
class Car:

    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def display_information(self):
        input("Press Enter to display car information...")
        print(f"Car Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")

if __name__ == "__main__":
    
    car1 = Car("Toyota Camry", 2020, "Black")
    car2 = Car("Ford Escape", 2014, "Red")

    car1.display_information()
    car2.display_information()
'''

# Approach 2
class Car:
    def __init__(self):
        self.model = ""
        self.year = ""
        self.color = ""

    def display_information(self):
        input("Press Enter to display car information...")
        print(f"Car Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")

if __name__ == "__main__":

    car1 = Car()
    car1.model = "Toyota Camry"
    car1.year = 2020
    car1.color = "Black"

    car2 = Car()
    car2.model = "Ford Escape"
    car2.year = 2014
    car2.color = "Red"

    print("Car 1 Information:")
    car1.display_information()
    print("\nCar 2 Information:")
    car2.display_information()