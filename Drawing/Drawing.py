from tkinter import *
import math
from turtle import color, window_height, window_width
import random

root = Tk(className="scr_functions")

window_height = 600
window_width = 800

canvas = Canvas(root, width=window_width, height=window_height)
canvas.pack()


def get_color_from_rgb(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)


def draw_triangle(size, color):
    size_difference = size / 50
    for i in range(50):
        size -= size_difference

        red = random.randint(0, 256) if (color == "r" or color == "rgb") else 0
        green = random.randint(0, 256) if (
            color == "g" or color == "rgb") else 0
        blue = random.randint(0, 256) if (
            color == "b" or color == "rgb") else 0

        if color != "r" and color != "g" and color != "b" and color != "rgb":
            print("Invalid command")
            root.destroy()
            return

        random_color = get_color_from_rgb(red, green, blue)
        height = (math.sqrt(3)/2) * size

        canvas.create_polygon(window_width/2, window_height - height, window_width /
                              2 + size/2, window_height, window_width/2 - size/2, window_height, fill=random_color)


print("Please difine the size of the triangle")
#size = int(input())
print("Please difine the the colour you'd like to randomize (r, g, b, or rgb)")
#color = input()
draw_triangle(600, "rgb")

root.mainloop()
