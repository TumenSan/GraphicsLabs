
#import array as arr
import numpy as np
from PIL import Image, ImageDraw, ImageFilter  

try:  
    #image1 = Image.open("images/scr1.jpg")
    image1 = Image.open("images/round.jpg")
     
except FileNotFoundError:  
    print("Файл не найден")

print("Размер изображения:")  
print(image1.format, image1.size, image1.mode)

draw = ImageDraw.Draw(image1)
width = image1.size[0]
height = image1.size[1]
pix = image1.load()

#линейного растяжения гистограммы
for x in range(width):
    for y in range(height):
       #r = pix[x, y][0] #узнаём значение красного цвета пикселя
       #g = pix[x, y][1] #зелёного
       #b = pix[x, y][2] #синего
       r, g, b = pix[x, y]
       #sr = (r + g + b) // 3 #среднее значение
       sr = (r + g + b) // 3 #среднее значение
       #draw.point((x, y), (sr, sr, sr)) #рисуем пиксель монохром
       draw.point((x, y), (r + 30, g + 30, b + 30)) #рисуем пиксель яркость
       #draw.point((x, y), (r, g, b)) #рисуем пиксель обычная

image1.save("result1.jpg", "JPEG") #не забываем сохранить изображение




image2 = Image.open("images/round.jpg")
draw = ImageDraw.Draw(image2)
width = image2.size[0]
height = image2.size[1]
pix = image2.load()


Choose = int(input("Input number: "))
if Choose == 1:
    Core = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
elif Choose == 2:
    Core = [[0, 1, 0], [1, 4, 1], [0, 1, 0]]
elif Choose == 3:
    Core = [[0, 1, 0], [1, 0, -1], [0, -1, 0]]
elif Choose == 4:
    Core = [[0, 1, 0], [1, -4, 1], [0, 1, 0]]
elif Choose == 5:
    Core = [[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]
elif Choose == 6:
    Core = [[1, 2, 1], [2, 4, 2], [1, 2, 1]]
else:
    print('err')
    Core = [[1, 2, 1], [2, 4, 2], [1, 2, 1]]
SumCore = 0
#Core = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
#Core = [[0, 1, 0], [1, 0, -1], [0, -1, 0]]
#Core = [[0, 1, 0], [1, -4, 1], [0, 1, 0]]
#Core = [[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]
#Core = [[1, 2, 1], [2, 4, 2], [1, 2, 1]]
for x1 in range(0, 3):
            for y1 in range(0, 3):
                SumCore += Core[x1][y1]
                print(Core[x1][y1]) 
matrixR = [[0] * 3 for i in range(3)]
matrixG = [[0] * 3 for i in range(3)]
matrixB = [[0] * 3 for i in range(3)]
a = 3
r = [[0] * height for i in range(width)]
g = [[0] * height for i in range(width)]
b = [[0] * height for i in range(width)]
sr = 0

#линейного растяжения гистограммы

for x in range(1, width - 1):
    for y in range(1, height - 1):
        r[x][y], g[x][y], b[x][y] = pix[x, y]

for x in range(1, width - 1):
    for y in range(1, height - 1):
        sumPixR = 0
        sumPixG = 0
        sumPixB = 0
        srR = 0
        srG = 0
        srB = 0
        for x1 in range(0, 3):
            for y1 in range(0, 3):
                sumPixR += r[x - 1 + x1][y - 1 + y1] * Core[x1][y1]
                sumPixG += g[x - 1 + x1][y - 1 + y1] * Core[x1][y1]
                sumPixB += b[x - 1 + x1][y - 1 + y1] * Core[x1][y1]

        if SumCore != 0:
            srR = sumPixR // SumCore
            srG = sumPixG // SumCore
            srB = sumPixB // SumCore
        else:
            srR = sumPixR
            srG = sumPixG
            srB = sumPixB

        #sr = (r + g + b) // 3 #среднее значение
        
        #draw.point((x, y), (sr, sr, sr)) #рисуем пиксель монохром
        draw.point((x, y), (srR, srG, srB)) #рисуем пиксель яркость
        #draw.point((x, y), (r, g, b)) #рисуем пиксель обычная
               

image2.save("result.jpg", "JPEG") #не забываем сохранить изображение


"""

Point1 = [100, 215]
Point2 = [100, 110]
Point3 = [215, 100]
MatrixA = np.array([[Point1[0], Point1[1], Point2[0]],[Point2[1], Point3[0], Point3[1]],[0, 0, 1]])
MatrixPoint = np.linalg.inv(MatrixA)
for x1 in range(0, 3):
            for y1 in range(0, 3):
                #MatrixPoint[x1][y1] = round(MatrixPoint[x1][y1])
                #MatrixPoint[x1][y1] = int(MatrixPoint[x1][y1])
                MatrixPoint[x1][y1] = MatrixPoint[x1][y1]
print(MatrixPoint)
#MatrixA = [[Point1[0], Point1[1], Point2[0]], [Point2[1], Point3[0], Point3[1]], [0, 0, 1]]
image3 = Image.open("images/chill.jpg")
draw = ImageDraw.Draw(image3)
width = image3.size[0]
height = image3.size[1]
pix = image3.load()

print(Point1[0], ' ', Point2[0], ' ', Point3[0])

SumCore = 0
#Core = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
#Core = [[0, 1, 0], [1, 0, -1], [0, -1, 0]]
#Core = [[0, 1, 0], [1, -4, 1], [0, 1, 0]]
#Core = [[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]
#Core = [[1, 2, 1], [2, 4, 2], [1, 2, 1]]
Core = MatrixPoint
for x1 in range(0, 3):
            for y1 in range(0, 3):
                SumCore += Core[x1][y1]
                print(Core[x1][y1]) 
matrixR = [[0] * 3 for i in range(3)]
matrixG = [[0] * 3 for i in range(3)]
matrixB = [[0] * 3 for i in range(3)]
a = 3
r = [[0] * height for i in range(width)]
g = [[0] * height for i in range(width)]
b = [[0] * height for i in range(width)]
sr = 0

#линейного растяжения гистограммы

for x in range(1, width - 1):
    for y in range(1, height - 1):
        r[x][y], g[x][y], b[x][y] = pix[x, y]

for x in range(1, width - 1):
    for y in range(1, height - 1):
        sumPixR = 0
        sumPixG = 0
        sumPixB = 0
        srR = 0
        srG = 0
        srB = 0
        for x1 in range(0, 3):
            for y1 in range(0, 3):
                sumPixR += r[x - 1 + x1][y - 1 + y1] * Core[x1][y1]
                sumPixG += g[x - 1 + x1][y - 1 + y1] * Core[x1][y1]
                sumPixB += b[x - 1 + x1][y - 1 + y1] * Core[x1][y1]

        if SumCore != 0:
            srR = int(sumPixR // SumCore)
            srG = int(sumPixG // SumCore)
            srB = int(sumPixB // SumCore)
        else:
            srR = int(sumPixR)
            srG = int(sumPixG)
            srB = int(sumPixB)

        #sr = (r + g + b) // 3 #среднее значение
        
        #draw.point((x, y), (sr, sr, sr)) #рисуем пиксель монохром
        draw.point((x, y), (srR, srG, srB)) #рисуем пиксель яркость
        #draw.point((x, y), (r, g, b)) #рисуем пиксель обычная
               

image3.save("result6.jpg", "JPEG") #не забываем сохранить изображение
"""
