import turtle

turtle.speed(10) 

#ruleInput = ['F']
#ruleOutput = ["F-F++F-F"]      #F
#start = "F++F++F"      #S

#ruleInput = ['F']
#ruleOutput = ["-F[-F+F-F]+[+F-F-F]"]
#start = "F"

#ruleInput = ['X', 'F']
#ruleOutput = ["--FXF++FXF++FXF--", 'FF']       #X #F
#start = "FXF--FF--FF"   #S


ruleInput = ['X', 'F']
ruleOutput = ["F[+X][-X]FX", "FF"]
start = "X"

#ruleOutput = ["F[+F]F[-F]F"]
#ruleOutput = ["F[+X][-X]FX"]
#ruleOutput = ["FF", "F+F[+FX]-X"]
#start = "F"


front = 5
#front = 20
#front = 20
#turn = 26
turn = 60
turn = 26
#turn = 26
stack = []
dirstack = []

turtle.left(90)
turtle.penup()          #перо поднять
turtle.setpos(0, -100)  #поставить позицию?
turtle.pendown()        #перо опустить
#turtle.shape("turtle")

def generate(iteration):
	result = start
	temp = ""
	for i in range(iteration):
		for j in range(len(result)):
			for k in range(len(ruleInput)):
				if (result[j] == ruleInput[k]):
					temp += ruleOutput[k]
					break
				if (k == len(ruleInput)-1):
					temp += result[j]
		result = temp
		temp = ""
	return result

def draw(input):
	for x in input:
		if (x == 'F'):
			turtle.forward(front)
		elif (x == '-'):
			turtle.left(turn)
		elif (x == '+'):
			turtle.right(turn)
		elif (x == '['):
			stack.append(turtle.pos())      #запомнить позицию и вставить в стек
			dirstack.append(turtle.heading())       #запомнить направление и вставить в стек
		elif (x == ']'):
			turtle.penup()
			post = stack.pop()
			direc = dirstack.pop()
			turtle.setpos(post)    #вытащить позицию из стека 
			turtle.setheading(direc)         #вытащить направление из стека
			turtle.pendown()
	turtle.hideturtle()
	turtle.done()

#draw(generate(5))


print('1 Снежинка Коха')
print('2 дерево 1')
print('3 дерево 2')
print('4 треугольник Серпинского')
print('5 дракон Хартера-Хатвея')
print('6 Кривая Гильберта')
Choose = int(input("Input number: "))

#Снежинка Коха
if Choose == 1:
        front = 5
        turn = 60
        ruleInput = ['F']
        ruleOutput = ["F-F++F-F"]      #F
        start = "F++F++F"      #S
        gen = int(input("Input iter generate: "))
        draw(generate(gen))
#дерево 1
elif Choose == 2:
        front = 20
        turn = 26
        ruleInput = ['F']
        ruleOutput = ["-F[-F+F-F]+[+F-F-F]"]
        start = "F"
        gen = int(input("Input iter generate: "))
        draw(generate(gen))
#дерево 2
elif Choose == 3:
        front = 5
        turn = 60
        ruleInput = ['X', 'F']
        ruleOutput = ["F[+X][-X]FX", "FF"]
        start = "X"
        gen = int(input("Input iter generate: "))
        draw(generate(gen))
#треугольник Серпинского
elif Choose == 4:
        front = 5
        turn = 60
        ruleInput = ['X', 'F']
        ruleOutput = ["--FXF++FXF++FXF--", 'FF']       #X #F
        start = "FXF--FF--FF"   #S
        gen = int(input("Input iter generate: "))
        draw(generate(gen))
#дракон Хартера-Хатвея
elif Choose == 5:
        front = 5
        turn = 90
        ruleInput = ['X', 'F', 'Y']
        ruleOutput = ["X+YF+", 'F', '-FX-Y']       #X #F
        start = "FX"   #S
        gen = int(input("Input iter generate: "))
        draw(generate(gen))
#Кривая Гильберта
elif Choose == 6:
        front = 5
        turn = 90
        ruleInput = ['X', 'F', 'Y']
        ruleOutput = ["-YF+XFX+FY-", 'F', '+XF-YFY-FX+']       #X #F
        start = "X"   #S
        gen = int(input("Input iter generate: "))
        draw(generate(gen))
else:
    print('err')
