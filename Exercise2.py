import turtle
import math

def draw_pifagoras_tree(t, branch_length, level):
    if level == 0:
        return
    else:
        # Draw main branch
        t.forward(branch_length)

        # Save the current position and heading
        position = t.position()
        heading = t.heading()

        # Draw the left subtree
        t.left(45)
        draw_pifagoras_tree(t, branch_length * 0.6, level - 1)

        # Return to the saved position and heading
        t.penup()
        t.setposition(position)
        t.setheading(heading)
        t.pendown()

        # Draw the right subtree
        t.right(90)
        draw_pifagoras_tree(t, branch_length * 0.6, level - 1)

        # Return to the saved position and heading
        t.penup()
        t.setposition(position)
        t.setheading(heading)
        t.pendown()

        # Go back to the starting position
        t.right(45)
        t.backward(branch_length)

def main():
    # Setup turtle
    screen = turtle.Screen()
    screen.bgcolor("white")
    turtle.speed(0)  # Set the turtle speed to the maximum

    # Create turtle
    pifagoras_turtle = turtle.Turtle()
    pifagoras_turtle.color("green")
    pifagoras_turtle.width(2)

    # Move turtle to starting position
    pifagoras_turtle.left(90)
    pifagoras_turtle.up()
    pifagoras_turtle.backward(200)
    pifagoras_turtle.down()

    # Set recursion level
    recursion_level = int(turtle.numinput("Recursion Level", "Enter recursion level:", default=4))

    # Draw the Pifagoras tree
    draw_pifagoras_tree(pifagoras_turtle, 100, recursion_level)

    # Close the turtle graphics window when clicked
    turtle.exitonclick()

if __name__ == "__main__":
    main()
