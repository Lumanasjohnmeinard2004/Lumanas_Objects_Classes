class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        if self.radius < 0:
            print("Error: Radius cannot be negative")
        else:
            area = 3.14159 * self.radius ** 2
            print(f"The area of the circle is: {area:.2f}")

    def perimeter(self):
        if self.radius < 0:
            print("Error: Radius cannot be negative")
        else:
            perimeter = 2 * 3.14159 * self.radius
            print(f"The perimeter of the circle is: {perimeter:.2f}")


# Example if you input positive value
circle = Circle(5)

circle.area()
circle.perimeter()

# Example if you input negative value
circle = Circle(-2)

circle.area()
circle.perimeter()
