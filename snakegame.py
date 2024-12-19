import turtle
import time
import random


print("Welcome to Tariq's Snake game")
x = input("Enter 'yes' if you want play in classic mode or 'no' if not")
def go_up():
    """sig: none -> none
    moves snake in response to up arrow"""
    if head.direction != 'down':
        head.direction = 'up'
def go_down():
    """sig: none -> none
    moves snake in response to down arrow"""
    if head.direction != 'up':
        head.direction = 'down'
def go_left():
    """sig: none -> none
    moves snake in response to left arrow"""
    if head.direction != 'right':
        head.direction = 'left'
def go_right():
    """sig: none -> none
    moves snake in response to right arrow"""
    if head.direction != 'left':
        head.direction = 'right'

def move():
    """sig: none -> none
    helps snake move"""
    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    # Move segment 0 to the head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    # Keep the snake moving in the same direction
    if head.direction == 'up':
        head.sety(head.ycor() + 10)
    if head.direction == 'down':
        head.sety(head.ycor() - 10)
    if head.direction == 'left':
        head.setx(head.xcor() - 10)
    if head.direction == 'right':
        head.setx(head.xcor() + 10)


if x == 'yes':
    print("Instructions\nUsing the snake try to collect as much food as possible without colliding into the walls or the body of the snake")
    time.sleep(5)

    # Score and delay
    score = 0
    high_score = 0
    delay = 0.1

    # Set up the screen
    wn = turtle.Screen()
    wn.title('Snake Game - Classic Mode')
    wn.bgcolor("green")
    wn.setup(width=700, height=700)
    wn.tracer(0)  # Turns off screen updates

    # Outline of the playing field
    pencil = turtle.Turtle()
    pencil.speed(0)
    pencil.color('black')
    pencil.penup()
    pencil.hideturtle()
    pencil.goto(310,310)
    pencil.pendown()
    pencil.goto(-310,310)
    pencil.goto(-310,-310)
    pencil.goto(310,-310)
    pencil.goto(310,310)
    pencil.penup()

    # Snake head
    
    head = turtle.Turtle()
    head.speed(0) 
    head.shape("square")
    head.color('orange')
    head.penup()
    head.goto(0,0)
    head.direction = 'stop'
    
    # Snake Food
    
    food = turtle.Turtle()
    food.speed(0) 
    food.shape("circle")
    food.color('red')
    food.penup()
    food.goto(0,100)
    
    # Contains information about snake body
    segments = []

    go_up()
    go_down()
    go_left()
    go_right()

    move()
     
    def collision():
        """sig: none -> none
        tells game if collision occurs and prints out score and highscore"""
        head.speed(0)
        head.goto(0,0)
        head.direction = 'stop'
        
        # Hide the segments
        for segment in segments:
            segment.hideturtle()
        # Clear the segments list
        segments.clear()

        global score
        global high_score
        if score > high_score:
                high_score = score
        print("GAME OVER\nYour score is:", score,"\nYour high score is:", high_score)
        score=0
        # Reset the delay
        global delay
        delay = 0.1

    #Keyboard bindings 
    wn.listen()
    wn.onkeypress(go_up, 'Up')
    wn.onkeypress(go_down, 'Down')
    wn.onkeypress(go_left, 'Left')
    wn.onkeypress(go_right, 'Right')
    x=[0,0]

    while True:
        # Updates the window repeatedly
        wn.update()

        # Check for collision with border
        if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
            collision()

        # Check if the snake eats the food
        if head.distance(food) < 20:
            # Move the food to a random spot
            food.goto(random.randint(-290,290),random.randint(-290,290))
            # Add a segment
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape('square')
            new_segment.color("orange")
            new_segment.penup()
            segments.append(new_segment)
            # Shorten the delay - this increases speed of snake as it gets longer
            delay -= 0.003
            
            def score1():
                """sig: none -> none
                updates score and high score as the game progresses"""
                global score
                global high_score
                score += 1
                if score > high_score:
                    high_score = score
            score1()
        move()
     
        # Check for head collision with the body segments
        for segment in segments:
            if segment.distance(head) < 10:
                collision()
        # Delay so that we can see things move
        time.sleep(delay)

    # Makes the window visible and runs everythings
    wn.mainloop()
else:
    x = input("Enter 'yes' if you want play in poison food mode or 'no' if not")
    if x == 'yes':
        print("Instructions\nUsing the snake try to collect as much food as possible without colliding into the walls or the body of the snake. Be sure not to eat the blue triangles as these are poison and it will take a point off your score.")
        time.sleep(5)

        # Score and delay
        score = 0
        high_score = 0
        delay = 0.1


        # Set up the screen
        wn = turtle.Screen()
        wn.title('Snake Game - Poison Mode')
        wn.bgcolor("green")
        wn.setup(width=700, height=700)
        wn.tracer(0)  # Turns off screen updates
        
        # Outline of the playing field
        pencil = turtle.Turtle()
        pencil.speed(0)
        pencil.color('black')
        pencil.penup()
        pencil.hideturtle()
        pencil.goto(310,310)
        pencil.pendown()
        pencil.goto(-310,310)
        pencil.goto(-310,-310)
        pencil.goto(310,-310)
        pencil.goto(310,310)
        pencil.penup()

        # Snake head
        head = turtle.Turtle()
        head.speed(0) 
        head.shape("square")
        head.color('orange')
        head.penup()
        head.goto(0,0)
        head.direction = 'stop'

        # Snake Food
        food = turtle.Turtle()
        food.speed(0) 
        food.shape("circle")
        food.color('red')
        food.penup()
        food.goto(0,100)

        # Snake poison
        poison = turtle.Turtle()
        poison.speed(0) 
        poison.shape("triangle")
        poison.color('blue')
        poison.penup()
        poison.goto(100,100)
        
        # Contains information about snake body
        segments = []

        go_up()
        go_down()
        go_left()
        go_right()
        
        move()
        
        def collision():
            """sig: none -> none
            tells game if collision occurs and prints out score and highscore"""
            head.speed(0)
            head.goto(0,0)
            head.direction = 'stop'
            
            # Hide the segments
            for segment in segments:
                segment.hideturtle()
                
            # Clear the segments list
            segments.clear()

            global score
            global high_score
            if score > high_score:
                    high_score = score
            print("GAME OVER\nYour score is:", score,"\nYour high score is:", high_score)
            score=0
            # Reset the delay
            global delay
            delay = 0.1    
        
        wn.listen()
        wn.onkeypress(go_up, 'Up')
        wn.onkeypress(go_down, 'Down')
        wn.onkeypress(go_left, 'Left')
        wn.onkeypress(go_right, 'Right')
        x=[0,0]

        
        ### Loop that runs the game code
        while True:
            # Updates the window repeatedly
            wn.update()

            # Check for collision with border
            if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
                collision()

            # Check if the snake eats the food
            if head.distance(food) < 20:
                # Move the food to a random spot
                food.goto(random.randint(-290,290),random.randint(-290,290))

                # Add a segment
                new_segment = turtle.Turtle()
                new_segment.speed(0)
                new_segment.shape('square')
                new_segment.color("orange")
                new_segment.penup()
                
                segments.append(new_segment)
                
                # Shorten the delay - this increases speed of snake as it gets longer
                delay -= 0.003
               
                score += 1

            if head.distance(poison) < 20:
                # Move the poison to a random spot
                poison.goto(random.randint(-290,290),random.randint(-290,290))

                
                # remove a segment
                segments[-1].hideturtle()
                segments.remove(segments[-1])
    
                # Derease the score
                score = score - 1
                if segments == []:
                    collision()
        
            move()
         
            # Check for head collision with the body segments
            for segment in segments:
                if segment.distance(head) < 10:
                    collision()
            # Delay so that we can see things move
            time.sleep(delay)

        # Makes the window visible and runs everythings
        wn.mainloop()
    else:
        print("You are now playing timed mode")
        print("Instructions\nCollect as much food as possible in a minute.")
        time.sleep(5)

        # Score and delay
        score = 0
        high_score = 0
        delay = 0.1


        # Set up the screen
        wn = turtle.Screen()
        wn.title('Snake game - Timed Mode')
        wn.bgcolor("green")
        wn.setup(width=700, height=700)
        wn.tracer(0)  # Turns off screen updates

        # Outline of the playing field
        pencil = turtle.Turtle()
        pencil.speed(0)
        pencil.color('black')
        pencil.penup()
        pencil.hideturtle()
        pencil.goto(310,310)
        pencil.pendown()
        pencil.goto(-310,310)
        pencil.goto(-310,-310)
        pencil.goto(310,-310)
        pencil.goto(310,310)
        pencil.penup()
        
        # Snake head
        head = turtle.Turtle()
        head.speed(0) 
        head.shape("square")
        head.color('orange')
        head.penup()
        head.goto(0,0)
        head.direction = 'stop'

        # Snake Food
        food = turtle.Turtle()
        food.speed(0) 
        food.shape("circle")
        food.color('red')
        food.penup()
        food.goto(0,100)

        # Contains information about snake body
        segments = []

        go_up()
        go_down()
        go_left()
        go_right()
        move()
        
        def collision():
            """sig: none -> none
            tells game if collision occurs"""
            head.speed(0)
            head.goto(0,0)
            head.direction = 'stop'

            global score
            global high_score
            if score > high_score:
                    high_score = score
            
            # Reset the delay
            global delay
            delay = 0.1
            

        ### Keyboard bindings
        wn.listen()
        wn.onkeypress(go_up, 'Up')
        wn.onkeypress(go_down, 'Down')
        wn.onkeypress(go_left, 'Left')
        wn.onkeypress(go_right, 'Right')
        x=[0,0]
        #assigning game start time
        start_time = time.time()
        while True:
            # Updates the window repeatedly
            wn.update()
            #Calculate time spent playing game
            playtime = time.time() - start_time
            if playtime > 60:
                print("GAME OVER\nYour score is:", score,"\nYour high score is:", high_score)
                exit()

            # Check for collision with border
            if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
                collision()

            # Check if the snake eats the food
            if head.distance(food) < 20:
                # Move the food to a random spot
                food.goto(random.randint(-290,290),random.randint(-290,290))
                # Add a segment
                new_segment = turtle.Turtle()
                new_segment.speed(0)
                new_segment.shape('square')
                new_segment.color("orange")
                new_segment.penup()
                segments.append(new_segment)
                # Shorten the delay - this increases speed of snake as it gets longer
                delay -= 0.003
                
                def score1():
                    """sig: none -> none
                    updates score and high score as the game progresses"""
                    global score
                    global high_score
                    score += 1
                    if score > high_score:
                        high_score = score
                score1()

            move()
         
            # Check for head collision with the body segments
            for segment in segments:
                if segment.distance(head) < 10:
                    collision()
            # Delay so that we can see things move
            time.sleep(delay)

        # Makes the window visible and runs everythings
        wn.mainloop()
