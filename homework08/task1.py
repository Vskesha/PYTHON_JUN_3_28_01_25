import turtle

# house settings
house_width = 500
house_height = 300
roof_height = 200
roof_width = 600
radius = 40

t = turtle.Turtle()
screen = t.getscreen()
screen.setup(width=roof_width + 100, height=max(house_height, roof_height) * 2 + 50)

def draw_rectangle(width: int, height: int):
    t.pendown()
    t.setheading(0)
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)

def draw_window(width: int, height: int):
    frame_width = width / 12
    win_width = (width - 3 * frame_width) / 2
    win_height = (height - 3 * frame_width) / 2

    draw_rectangle(width, height)
    
    t.penup()
    t.setheading(0)
    t.forward(frame_width)
    t.right(90)
    t.forward(frame_width)
    draw_rectangle(win_width, win_height)

    t.penup()
    t.setheading(0)
    t.forward(win_width + frame_width)
    draw_rectangle(win_width, win_height)

    t.penup()
    t.setheading(270)
    t.forward(win_height + frame_width)
    draw_rectangle(win_width, win_height)

    t.penup()
    t.setheading(180)
    t.forward(win_width + frame_width)
    draw_rectangle(win_width, win_height)


t.penup()
t.goto(-house_width // 2, 0)
t.pendown()

draw_rectangle(house_width, house_height)

t.penup()
t.goto(-roof_width // 2, 0)
t.pendown()

t.forward(roof_width)
t.goto(0, roof_height)
t.goto(-roof_width // 2, 0)

t.penup()
t.goto(0, roof_height // 2 - radius)
t.pendown()

t.circle(radius)

t.penup()
t.goto(house_width // 6, -house_height // 2)
t.pendown()
draw_rectangle(house_width // 6, house_height // 2)

t.penup()
t.goto(-house_width // 3, -house_height // 6)
draw_window(house_width // 4, house_height // 2)


turtle.done()
