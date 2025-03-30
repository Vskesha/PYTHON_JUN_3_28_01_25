import turtle

t = turtle.Turtle()
sides = 5

def draw_polygon():
    for _ in range(sides):
        t.forward(100)
        t.right(360 / sides)
    turtle.ontimer(draw_polygon, 500)

draw_polygon()

turtle.done()
