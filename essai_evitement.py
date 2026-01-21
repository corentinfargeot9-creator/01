# Librairie   : https://github.com/kholm777/maqueen/tree/main
from maqueen import Maqueen
from microbit import * 
import utime

# Constantes
WHITE = 1
BLACK = 0

sb=0
robot = Maqueen()
display.show(Image.HAPPY)

while True:
    sleep(10)
    if robot.line_left()==BLACK and robot.line_right()==BLACK:
        robot.motor_left(150)
        robot.motor_right(150)
    elif robot.line_left()==WHITE and robot.line_right()==BLACK:
        robot.motor_left(150)
        robot.motor_right(20)
    elif robot.line_left()==BLACK and robot.line_right()==WHITE:
        robot.motor_left(20)
        robot.motor_right(150)
    distance = robot.ultrasound_measure()
    
    if distance <10:
        robot.motor_left(150)
        robot.motor_right(20)
        sleep(1000)
        

            
    if robot.line_left()==WHITE and robot.line_right()==WHITE:
        robot.motor_left(50)
        robot.motor_right(50)
        
    
        

