ball_y = 100
y_speed = 4
ball_x = 100
x_speed = 4
brick = "nothit"
#brick = "hit"
brick2 = "nothit"
#brick2 = "hit"
brick3 = "nothit"
#brick3 = "hit"
brick4 = "nothit"
#brick4 = "hit"
brick5 = "nothit"


def setup():
    size(500, 500)
       
    
    
    
    
    
def draw():
    global ball_y
    global y_speed
    global ball_x
    global x_speed
    global brick
    global brick2
    global brick3
    global brick4
    global brick5
    background(255, 222, 249)
    fill(222, 245, 255)
    ellipse(ball_x, ball_y, 25, 25)
    rect(mouseX, 450, 70, 20) #controller rect
    

    if brick == "nothit":
        rect(0, 0, 100, 20)
    
    if brick2 == "nothit":
        rect(100, 0, 100, 20)
        
    if brick3 == "nothit":
        rect(200, 0, 100, 20)
        
    if brick4 == "nothit":
        rect(300, 0, 100, 20)
        
    if brick5 == "nothit":
        rect(400, 0, 100, 20)
    

    
     
    if ball_y < 475 and ball_y > 425 and ball_x < mouseX+125 and ball_x > mouseX-25:
        print("BOUNCE")
        y_speed = -y_speed
    
    if ball_y < 20:
        print("bounceback")
        y_speed = 4
    
    if ball_x < 20:
        x_speed = 4
    
    if ball_x > 450:
        x_speed = -x_speed
        
    if ball_y < 20 and ball_x < 100:
        print("bounceback")
        y_speed = 4
        
    
    if ball_y < 20 and ball_x < 100:
         brick = "hit"
         print("hit")
        
         if brick == "hit":
             fill(255, 222, 249)
             rect(0, 0, 100, 20)
             
    if ball_y < 20 and ball_x < 200 and ball_x > 100:
         brick2 = "hit"
         print("hit")
        
         if brick == "hit":
             fill(255, 222, 249)
             rect(100, 0, 100, 20)
            
    if ball_y < 20 and ball_x < 300 and ball_x > 200:
         brick3 = "hit"
         print("hit")
        
         if brick == "hit":
             fill(255, 222, 249)
             rect(300, 0, 100, 20)
             
    if ball_y < 20 and ball_x < 400 and ball_x >300:
        brick4 = "hit"
        print("hit")
        
        if brick == "hit":
            fill(255, 222, 249)
            rect(300, 0, 100, 20)
            
    if ball_y < 20 and ball_x < 500 and ball_x >400:
        brick5 = "hit"
        print("hit")
        
        if brick == "hit":
            fill(255, 222, 249)
            rect(400, 0, 100, 20)
    
        
           




    
    
    
    ball_x = ball_x + x_speed
    ball_y = ball_y + y_speed

    
        
    
