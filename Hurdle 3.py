def turnRight():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turnRight()
    move()
    turnRight()
    move()
    turn_left()
   
    
while not at_goal():
    if wall_in_front():
        jump()
    elif front_is_clear():
        move()
    else: 
        pass;
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
def turnRight():
    turn_left()
    turn_left()
    turn_left()