from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
from sshkeyboard import listen_keyboard
from Raspi_PWM_Servo_Driver import PWM
from gpiozero import DistanceSensor
from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from sense_hat import SenseHat
from threading import Thread
from time import sleep
import asyncio
import cv2
BUZZERPORT=18

b=TonalBuzzer(BUZZERPORT)
sense = SenseHat()
sense.clear(255, 255, 255)



mh = Raspi_MotorHAT(addr=0x6f)
myMotor = mh.getMotor(2) #핀번호

myMotor.setSpeed(100) #속도

servo = PWM(0x6F)
servo.setPWMFreq(60)
speed = 20
direction = 300

# 제어 #
def home():
    t = 1.5
    for _ in range(6):
        servo.setPWM(0,0,180)
        move(100, True)
        sleep(t)
        servo.setPWM(0,0,395)
        move(100, False)
        sleep(t)
    servo.setPWM(0,0,300)
    myMotor.run(Raspi_MotorHAT.RELEASE)
def slow_home():
    t = 0.8
    for _ in range(16):
        servo.setPWM(0,0,350)
        move(80, True)
        sleep(t)
        servo.setPWM(0,0,250)
        move(80, False)
        sleep(t)
    servo.setPWM(0,0,300)
    myMotor.run(Raspi_MotorHAT.RELEASE)
def move(speed, foward):
    myMotor.setSpeed(speed)
    if foward:
        myMotor.run(Raspi_MotorHAT.BACKWARD)
    else:
        myMotor.run(Raspi_MotorHAT.FORWARD)
def turn(b):
    global direction
    if b==1:
        direction += 35
    elif b ==2:
        direction -= 35
    else:
        direction = 300
    if direction > 400:
        direction = 395
    elif direction < 200:
        direction = 180
    servo.setPWM(0,0,direction)

# 노래 #
def pororo():
        dic = {'x':0, 'c0': 261.6256, 'c1': 523.2511, 'c#0': 277.1826, 'c#1': 554.3653, 'd0': 293.6648, 'd1': 587.3295, 'd#0': 311.127, 'd#1': 622.254, 'e0': 329.6276, 'e1': 659.2551, 'f0': 349.2282, 'f1': 698.4565, 'f#0': 369.9944, 'f#1': 739.9888, 'g0': 391.9954, 'g1': 783.9909, 'g#0': 415.3047, 'g#1': 830.6094, 'a0': 440.0, 'a1': 880.0, 'a#0': 466.1638, 'a#1': 0, 'b0': 493.8833, 'b1': 0}
        pororo = ['x', 'e1', 'c#1', 'a0',
                'b0', 'b0', 'e0', 'e0',
                'x', 'e1', 'c#1', 'a0',
                'b0', 'f#1', 'e1',
                'f#1', 'f#1', 'g#1',
                'e1', 'e1', 'f#1',
                'c#1', 'f#1', 'c#1', 'a0',
                'c#1', 'b0', 'b0']
        beat = [1,1,1,1,
                0.5, 0.5, 1, 2,
                1, 1, 1, 1,
                1, 1, 2,
                1, 1, 2,
                1, 1, 2,
                1, 1, 1, 1,
                1, 1, 2]
        b = TonalBuzzer(BUZZERPORT)
        speed = 0.3
        for i in range(len(pororo)):
            now = dic[pororo[i]]
            if now==0:
                sleep(beat[i]*speed)
                continue
            b.play(now)
            sleep(beat[i]*speed)
            b.stop()
            sleep(speed/2)
def baby_shark():
        dic = {'x':0, 'c0': 261.6256, 'c1': 523.2511, 'c#0': 277.1826, 'c#1': 554.3653, 'd0': 293.6648, 'd1': 587.3295, 'd#0': 311.127, 'd#1': 622.254, 'e0': 329.6276, 'e1': 659.2551, 'f0': 349.2282, 'f1': 698.4565, 'f#0': 369.9944, 'f#1': 739.9888, 'g0': 391.9954, 'g1': 783.9909, 'g#0': 415.3047, 'g#1': 830.6094, 'a0': 440.0, 'a1': 880.0, 'a#0': 466.1638, 'a#1': 0, 'b0': 493.8833, 'b1': 0}
        pororo = ['d0', 'e0', 'g0','g0','g0','g0','g0',
                'g0','g0','g0','d0', 'e0', 'g0','x','g0','g0',
                'g0','g0','g0','d0', 'e0', 'g0','x','g0','g0',
                'g0','g0','g0','g0','g0','f#0','f#0']
        beat = [4, 4, 2, 2, 2, 1, 1,
                1, 2, 2, 2, 2, 2, 2, 1, 2,
                1, 2, 2, 2, 2, 2, 2, 1, 2,
                1, 1, 2, 2, 2, 2, 2 ]
        b = TonalBuzzer(BUZZERPORT)
        speed = 0.1
        for i in range(len(pororo)):
            now = dic[pororo[i]]
            if now==0:
                sleep(beat[i]*speed)
                continue
            b.play(now)
            sleep(beat[i]*speed)
            b.stop()
            sleep(speed/2)
def hype_boy():
    dic = {'x':0, 'c0': 261.6256, 'c1': 523.2511, 'c#0': 277.1826, 'c#1': 554.3653, 'd0': 293.6648, 'd1': 587.3295, 'd#0': 311.127, 'd#1': 622.254, 'e0': 329.6276, 'e1': 659.2551, 'f0': 349.2282, 'f1': 698.4565, 'f#0': 369.9944, 'f#1': 739.9888, 'g0': 391.9954, 'g1': 783.9909, 'g#0': 415.3047, 'g#1': 830.6094, 'a0': 440.0, 'a1': 880.0, 'a#0': 466.1638, 'a#1': 0, 'b0': 493.8833, 'b1': 0}
    pororo = ['g0', 'b0', 'b0', 'a0', 'g0', 'g0', 'f#0', 'g0',
              'a0', 'd0']
    beat = [1.5, 3, 3, 3, 9, 2, 2, 2, 3, 6]
    b = TonalBuzzer(BUZZERPORT)
    speed = 0.1
    for i in range(len(pororo)):
        now = dic[pororo[i]]
        if now==0:
            sleep(beat[i]*speed)
            continue
        b.play(now)
        sleep(beat[i]*speed)
        b.stop()
        sleep(speed/2)

# 센스햇 LED #
sense.show_letter('0')
# 충돌방지 #
off = False
def zeroday():
    sensor = DistanceSensor(echo=15, trigger=14)
    while True:
        if off:
            return
        dist = sensor.distance
        if dist<0.1:
            print("Safty Protocol Activated")
            myMotor.run(Raspi_MotorHAT.RELEASE)
            b.play(622)
            sleep(1)
            b.stop()
        if dist<0.6:
            myMotor.setSpeed(int(speed*dist*1.666))
        else:
            myMotor.setSpeed(speed)
        #sense.clear(255*int(1-sensor.distance),0,0)            
        sleep(0.1)
zday = Thread(target=zeroday)
zday.start()

# Camera #
def camera():
    camera = cv2.VideoCapture(-1) #카메라를 비디오 입력으로 사용. -1은 기본설정이라는 뜻
    camera.set(3,640)  #띄울 동영상의 가로사이즈 640픽셀
    camera.set(4,480)  #세로사이즈 480픽셀
    while( camera.isOpened() ):  #카메라가 Open되어 있다면,
        _, image = camera.read()  ##비디오의 한 프레임씩 읽습니다. _값이 True, 실패하면 False, image에 읽은 프레임이 나옴
        image = cv2.flip(image,-1)  #카메라 이미지를 flip, 뒤집습니다. -1은 180도 뒤집는다는 뜻입니다.
        cv2.imshow( 'Front' , image)  #카메라를 'camera test'라는 이름의 파일로 보여줍니다. 
        if cv2.waitKey(1) == ord('q'):  #만약 q라는 키보드값을 읽으면 종료합니다.
            break        
    cv2.destroyAllWindows() #이후 openCV창을 종료합니다.

flag = False
moving = False
async def press(key):
    global flag, speed, moving
    # CONTROL PART #
    if (key=='up'):
        flag = True
        moving = True
        move(speed, True)
    elif key == 'down':
        flag = True
        moving = False
        myMotor.run(Raspi_MotorHAT.RELEASE)
        move(speed, False)
    elif key == 'space':
        flag = False
        myMotor.run(Raspi_MotorHAT.RELEASE)
        sense.show_letter('0')
    elif key == 'left':
        turn(2)
    elif key=='right':
        turn(1)
    # SPEED PART #
    elif key in ['0','1', '2', '3']:
        speed = int(key)*100 + (50 if key == '0' else 0)
        sense.show_letter(key)
        if flag:
            move(speed, moving)
        print("Speed: "+str(speed))
    elif key == 'pageup' or key == 'pagedown':
        speed += 10 *((-1)*(1 if key=='pagedown' else -1)) * (speed>0)
        if flag:
            move(speed, moving)
        print("Speed: "+str(speed))
    # ADDITIONAL #
    elif key == 'home':
        slow_home()
    elif key == 'p':
        t1=Thread(target=pororo)
        t1.start()
    elif key == '+':
        t1=Thread(target=baby_shark)
        t1.start()
    elif key == '=':
        t1=Thread(target=hype_boy)
        t1.start()
    elif key=='c':
        cam = Thread(target=camera)
        cam.start()
    elif key=='x':
        
        global off
        if off:
            print('Safty Mode ON')
            off = False
            zday = Thread(target=zeroday)
            zday.start()
        else:
            print('Safty Mode OFF')
            off = True
    else:
        turn(0)
        print("Key: "+str(key))
async def release(key):
    pass
    

listen_keyboard(
    on_press=press,
    on_release=release,
)
