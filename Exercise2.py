import turtle

def pifagor_tree(t, length, level):
    if level == 0:
        return
    t.forward(length)
    t.left(45)
    pifagor_tree(t, length * 0.7, level - 1)
    t.right(90)
    pifagor_tree(t, length * 0.7, level - 1)
    t.left(45)
    t.backward(length)

def main():
    level = int(input("Введіть рівень рекурсії: "))
    t = turtle.Turtle()
    screen = turtle.Screen()
    t.speed(0)
    t.left(90)
    t.penup()
    t.goto(0, -200)
    t.pendown()
    pifagor_tree(t, 100, level)
    screen.mainloop()

if __name__ == "__main__":
    main()
