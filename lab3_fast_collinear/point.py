from __future__ import annotations
from functools import total_ordering

import turtle


@total_ordering
class Point:
    def __init__(self, x: float, y: float):
        # DO NOT MODIFY
        self.x = x
        self.y = y

    def draw(self) -> None:
        # DO NOT MODIFY
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.dot(8, "black")

    def draw_to(self, that: Point) -> None:
        # DO NOT MODIFY
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.pensize(2)
        turtle.pencolor("black")
        turtle.goto(that.x, that.y)

    def __str__(self) -> str:
        # DO NOT MODIFY
        return f"({self.x}, {self.y})"
    
    def _is_valid_operand(self, that: object) -> bool:
        # DO NOT MODIFY
        return isinstance(that, Point)

    def __lt__(self, that: Point) -> bool:
        # use _is_valid_operand above to check if `that` is a Point and raise an error if it isn't a Point object
        if not self._is_valid_operand(that):
            raise TypeError("Operand must be a Point")
        if self.y == that.y:
            return self.x < that.x
        return self.y < that.y

    def __eq__(self, that: Point) -> bool:
        # use _is_valid_operand above to check if `that` is a Point and raise an error if it isn't a Point object
        if not self._is_valid_operand(that):
            raise TypeError("Operand must be a Point")
        return self.x == that.x and self.y == that.y
    
    def __hash__(self):
        return hash((self.x, self.y))  # Hash based on x and y coordinates

    def slope_to(self, that: Point) -> float:
        # calculate the slope from this to that Point
        if self == that:
            return float('-inf')  # Fail line segment
        if self.x == that.x:
            return float('inf')  # Vertical line
        if self.y == that.y:
            return 0.0  # Horizontal line
        return (that.y - self.y) / (that.x - self.x)
    
    @staticmethod
    def main():
        LENGTH = 800
        WIDTH = 600
        MARGIN = 50

        # Initialize turtle screen
        screen = turtle.Screen()
        screen.setup(LENGTH, WIDTH)

        # Transfer the point of origin to the bottom left
        screen.setworldcoordinates(-MARGIN, -MARGIN, LENGTH - MARGIN, WIDTH - MARGIN)
        turtle.hideturtle()

        # Create points
        p1 = Point(0, 0)
        p2 = Point(150, 200)
        # p3 = Point(200, 300)
        # p4 = Point(300, 350)


        # Draw points
        p1.draw()
        p2.draw()
        # p3.draw()
        # p4.draw()

        # Draw line between points
        p1.draw_to(p2)
        # p2.draw_to(p3)
        # p3.draw_to(p4)


        # Calculate slope (uncomment this if you have implemented slope_to)
        print("Slope between p1 and p2:", p1.slope_to(p2))
        # print("Slope between p1 and p3:", p1.slope_to(p3))
        # print("Slope between p1 and p4 :", p2.slope_to(p4))


        # Keep the window open
        turtle.done()


# Example usage
if __name__ == "__main__":
    Point.main()
