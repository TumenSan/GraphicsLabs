import turtle

turtle.speed(10) 

#ruleInput = ['F', 'X']
#ruleOutput = ["FF", "F-[[X]+X]+F[+FX]-X"]

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
			stack.append(turtle.pos())
			dirstack.append(turtle.heading())
		elif (x == ']'):
			turtle.penup()
			post = stack.pop()
			direc = dirstack.pop()
			turtle.setpos(post)
			turtle.setheading(direc)
			turtle.pendown()
	turtle.hideturtle()
	turtle.done()

draw(generate(5))
