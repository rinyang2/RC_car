from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
from Raspi_PWM_Servo_Driver import PWM
from time import sleep

mh = Raspi_MotorHAT(addr=0x6f) 
myMotor = mh.getMotor(2) #핀번호

myMotor.setSpeed(100) #속도

servo = PWM(0x6F)
servo.setPWMFreq(60)
speed = 100
default_direction = 300

def move(speed, time, foward):
    myMotor.setSpeed(speed)
    try:
        if foward:
            myMotor.run(Raspi_MotorHAT.BACKWARD)
        else:
            myMotor.run(Raspi_MotorHAT.FORWARD)
        sleep(time)
        myMotor.run(Raspi_MotorHAT.RELEASE)
    finally:
        myMotor.run(Raspi_MotorHAT.RELEASE)

def turn(direction):
    global default_direction
    if direction==1:
        default_direction += 30
    elif direction ==2:
        default_direction -= 30
    else:
        default_direction = 300
    servo.setPWM(0,0,default_direction)
def teabag():
    for _ in range(5):
        servo.setPWM(0,0,250)
        sleep(0.1)
        servo.setPWM(0,0,350)
        sleep(0.1)
    servo.setPWM(0,0,300)

while True:
    s = list(input('Input Order >> ').split())
    if len(s)==0:
        continue
    if s[0] == 'move':
        move(int(s[2]),int(s[3]), s[1]=='f')
    elif s[0] == 'turn':
        if s[1] == 'r':
            turn(1)
        elif s[1] == 'l':
            turn(2)
        else:
            turn(0)
    elif s[0] == 'set':
        speed = int(s[1])
    elif s[0] =='zz':
        teabag()
    else:
        if s[0]=='w':
            move(speed,1,True)
        elif s[0]=='a':
            turn(2)
        elif s[0]=='s':
            move(speed, 1, False)
        elif s[0] == 'd':
            turn (1)
        else:
            turn(0)
