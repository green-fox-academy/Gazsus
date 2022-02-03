from tkinter import *
import random
import math


def get_color_from_rgb(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)
# endregion


root = Tk(className="Lovely drawing")
window_height = 600
window_width = 800
canvas = Canvas(root, width=window_width, height=window_height)
canvas.pack()


def draw_triangle(size, color):
    size_difference = size / 50
    for i in range(50):
        size -= size_difference

        red = 0
        green = 0
        blue = 0
        if color == "r":
            red = random.randint(0, 256)
        elif color == "g":
            green = random.randint(0, 256)
        elif color == "b":
            blue = random.randint(0, 256)
        elif color == "rgb":
            red = random.randint(0, 256)
            green = random.randint(0, 256)
            blue = random.randint(0, 256)
        else:
            print("Invalid input")

        random_color = get_color_from_rgb(red, green, blue)

        height = (math.sqrt(3) / 2) * size
        canvas.create_polygon(window_width / 2, window_height - height, window_width / 2 + size / 2, window_height,
                              window_width / 2 - size / 2, window_height,
                              fill=random_color)


print("Please define the size of the triangle")
size = int(input())
print("Please define which color you want to randomize (r, g, b or rgb")
color = input()

draw_triangle(size, color)

# endregion
root.mainloop()
