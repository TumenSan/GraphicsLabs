import turtle
import math

turtle.speed(100) 
size = 300
n = 3
 
#Koh snow 
def koch_curve(size, n):
    if n == 0:
        turtle.forward(size)
    else:
        koch_curve(size / 3, n - 1)
        turtle.left(60)
        koch_curve(size / 3, n - 1)
        turtle.right(60)
        turtle.right(60)
        koch_curve(size / 3, n - 1)
        turtle.left(60)
        koch_curve(size / 3, n - 1)
 
 
def draw_kox_snow(size, n):
    koch_curve(size, n)
    turtle.right(60)
    turtle.right(60)
    koch_curve(size, n)
    turtle.right(60)
    turtle.right(60)
    koch_curve(size, n)
 
 
#draw_kox_snow(size, n)
#


#draw_Tree
def draw_Tree(size, n):
    if n == 0:
        turtle.forward(size)
    else:
        koch_curve(size / 3, n - 1)
        turtle.left(60)
        koch_curve(size / 3, n - 1)
        turtle.right(60)
        turtle.right(60)
        koch_curve(size / 3, n - 1)
        turtle.left(60)
        koch_curve(size / 3, n - 1)
 
#draw_Tree(size, n)
#




def build_tree(branch_length, shorten_by, angle):
  if branch_length > 3:
    turtle.forward(branch_length)
    new_length = branch_length - shorten_by
    turtle.left(angle)
    build_tree(new_length, shorten_by, angle)
    turtle.right(angle)
    turtle.right(angle)
    build_tree(new_length, shorten_by, angle)
    turtle.left(angle)
    turtle.backward(branch_length)



print('123')

Choose = int(input("Input number: "))

if Choose == 1:
    draw_kox_snow(size, n)
elif Choose == 2:
    drawTriangleOutline(100, n)
elif Choose == 3:
    build_tree(50, 5, 30)
    turtle.hideturtle()
    turtle.setheading(90)
else:
    print('err')
