import turtle
import math
from turtle import Turtle


def draw_branch(t: Turtle, branch_length: float, angle: float, level: int) -> None:
    """Draw one branch of the tree recursively.

    :param t: Turtle used for drawing.
    :param branch_length: Length of the current branch.
    :param angle: Angle used for left and right turns.
    :param level: Current level of recursion.
    """
    # Stop recursion when level reaches zero
    if level == 0:
        return

    # Draw the main branch
    t.forward(branch_length)

    # Draw the left branch
    t.left(angle)  # Turn left by the given angle
    # Recursively draw the left branch with a smaller length
    draw_branch(t, branch_length * math.cos(math.radians(angle)), angle, level - 1)
    t.right(angle)  # Turn right to go back to the main branch

    # Draw the right branch
    t.right(angle)  # Turn right by the given angle
    # Recursively draw the right branch with a smaller length
    draw_branch(t, branch_length * math.cos(math.radians(angle)), angle, level - 1)
    t.left(angle)  # Turn left to return to the original direction

    # Move back to the previous branch position
    t.backward(branch_length)


def draw_tree(level: int) -> None:
    """Initialize the turtle and draw the tree.

    :param level: The depth of recursion for drawing the tree.
    """
    t = turtle.Turtle()
    t.speed("fastest")  # Set the fastest drawing speed

    # Set the initial position of the turtle
    t.penup()
    t.goto(0, -250)
    t.pendown()
    t.left(90)  # Point the turtle upwards

    # Start drawing the tree with a branch length of 100 and an angle of 45 degrees
    draw_branch(t, 100, 45, level)

    turtle.done()  # Finish turtle graphics


if __name__ == "__main__":
    try:
        level_input = input("Enter the recursion level: ")
        level: int = int(level_input)
        draw_tree(level)
    except ValueError:
        print("Please enter a valid integer for the recursion level.")
