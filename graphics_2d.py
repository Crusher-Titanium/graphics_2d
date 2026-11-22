from turtle import goto, setup, penup, dot, done, tracer, update, hideturtle

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