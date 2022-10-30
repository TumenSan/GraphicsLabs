import turtle

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
        turtle.right(120)
        koch_curve(size / 3, n - 1)
        turtle.left(60)
        koch_curve(size / 3, n - 1)
 
 
def draw_kox_snow(size, n):
    for i in range(3):
        koch_curve(size, n)
        turtle.right(120)
 
 
#draw_kox_snow(size, n)
#

print('123')

Choose = int(input("Input number: "))

if Choose == 1:
    draw_kox_snow(size, n)
elif Choose == 2:
    print('ok')
else:
    print('err')
