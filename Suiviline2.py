# Librairie   : https://github.com/kholm777/maqueen/tree/main
from maqueen import Maqueen
from microbit import * 
import utime

# Constantes
WHITE = 1
BLACK = 0

robot = Maqueen()
display.show(Image.HAPPY)

while True:
    if robot.line_left()==BLACK and robot.line_right()==BLACK:
        robot.motor_left(100)
        robot.motor_right(100)
    elif robot.line_left()==WHITE and robot.line_right()==BLACK:
        robot.motor_left(125)
        robot.motor_right(25)
    elif robot.line_left()==BLACK and robot.line_right()==WHITE:
        robot.motor_left(25)
        robot.motor_right(125)
