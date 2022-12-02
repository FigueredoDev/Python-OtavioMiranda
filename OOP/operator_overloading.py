class Rectangle:
    def __init__(self, x, y) -> None:
        self.value_x = x
        self.value_y = y

    def get_area(self):
        return self.value_x * self.value_y

    def __repr__(self) -> str:
        return f"<class 'Rectangle({self.value_x}, {self.value_y})'>"

    def __add__(self, other):
        new_x = self.value_x + other.value_x
        new_y = self.value_y + other.value_y
        return Rectangle(new_x, new_y)

    def __lt__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 < a2:
            return True
        else:
            return False

    def __gt__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 > a2:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.value_x == other.value_x and self.value_y == other.value_y:
            return True
        else:
            return False


r1 = Rectangle(10, 20)
r2 = Rectangle(10, 20)
r3 = r1 + r2
print(r3)
