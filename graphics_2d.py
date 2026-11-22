from turtle import goto, setup, penup, pendown, dot, done, tracer, update, hideturtle

class Window:
    def __init__(self):
        self.width = 700
        self.height = 500
        setup(self.width, self.height)
        tracer(0)
        penup()
        hideturtle()

    def show(self):
        update()
        done()

    def draw_dot(self, x, y):
        goto(x, y)
        dot()

    def draw_line(self, x1, y1, x2, y2):
        self.draw_dot(x1, y1)
        pendown()
        self.draw_dot(x2, y2)
        penup()
    def draw_triangle(self, x1, y1, x2, y2, x3, y3):
        self.draw_line(x1, y1, x2, y2)
        self.draw_line(x2, y2, x3, y3)
        self.draw_line(x3, y3, x1, y1)
