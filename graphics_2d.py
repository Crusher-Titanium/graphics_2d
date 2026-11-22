from turtle import goto, setup, penup, pendown, dot, done, tracer, update, hideturtle

class Window:
    def __init__(self):
        self.width = 700
        self.height = 500
        setup(self.width, self.height)
        tracer(0)
        penup()
        hideturtle()
        self.vertices = {}

    def show(self):
        update()
        done()

    def add_vertex(self, x, y):
        self.vertices["vertex"+str(len(self.vertices)+1)] = [x, y]

    def draw_dot(self, vertex):
        goto(self.vertices["vertex"+str(vertex)][0], self.vertices["vertex"+str(vertex)][1])
        dot()

    def draw_line(self, vertex1, vertex2):
        self.draw_dot(vertex1)
        pendown()
        self.draw_dot(vertex2)
        penup()

    def draw_triangle(self, vertex1, vertex2, vertex3):
        self.draw_line(vertex1, vertex2)
        self.draw_line(vertex2, vertex3)
        self.draw_line(vertex3, vertex1)

    def draw_quad(self, vertex1, vertex2, vertex3, vertex4):
        self.draw_triangle(vertex1, vertex2, vertex3)
        self.draw_triangle(vertex4, vertex3, vertex2)
