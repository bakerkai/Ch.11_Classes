'''
Open an arcade window that is 500 x 300 pixels and named 1000 Circles.
Create a class called Circle.
Initialize the x and y positions to be randomly placed somewhere in the window.
Initialize the radius to be 10 pixels.
Initialize the color to randomized 0-255 RGB color format.
Add a method to the Circle Class called draw_circle and draw the circle.
In the main program, use a for loop to call the Circle class and draw it 1000 times.
Feel free to see what happens if you draw it 10,000 times as well.
'''
import arcade
import random
SW = 500
SH = 300

class Circle():
    def __init__(self):
        self.radius = 10
        self.x = random.randint(self.radius, SW - self.radius)
        self.y = random.randint(self.radius, SH - self.radius)
        self.col = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    def draw_circle(self):
        arcade.draw_circle_outline(self.x,self.y, self.radius, self.col)



def myprogram():
    arcade.open_window(SW, SH, "1000 Circles")
    arcade.set_background_color(arcade.csscolor.BLUE)
    arcade.start_render()

    #draw stuff

    for i in range(1000):
        circle = Circle()
        circle.draw_circle()

    arcade.finish_render()
    arcade.run()


if __name__ == "__main__":
    myprogram()