# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl 
import random

#-----game configuration----
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False
shape = "turtle"
color = "blue"
size = 2  
#beige
score = 0
#-----initialize turtle-----
counter =  trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(400,400)
counter.pendown()
ham = trtl.Turtle(shape = shape)
ham.color(color)
ham.shapesize(size)

sco = trtl.Turtle(shape = shape)
sco.shape("square")
sco.ht()
sco.penup()
sco.goto(-400,400)
font = ("Arial",30)
sco.write(score, font=font)




#-----game functions--------
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font)
    timer_up = True
    game_end()
  else:
    counter.write("Timer: " + str(timer), font=font)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)
     
def turtle_clicked(x,y):
    print("click")
    change_position()
    score_counter()
    ham.color(random_color())

def change_position():
    ham.penup()
    ham.ht()
    new_xpos = random.randint(-400,400)
    new_ypos = random.randint(-300,300)
    ham.goto(new_xpos, new_ypos)
    ham.st()

def score_counter():
    global score
    score += 1 
    print (score)
    sco.clear()
    sco.write(score, font=font)
    
def random_color():
    r = random.random()
    g = random.random()
    b = random.random()

    return (r,g,b)
def game_end():
    ham.ht()
    ham.goto(800,800)
    


#-----events----------------]
ham.onclick(turtle_clicked)

wn = trtl.Screen()
wn.ontimer(countdown, counter_interval) 
wn.mainloop()