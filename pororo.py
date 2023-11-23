from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from time import sleep
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
    b = TonalBuzzer(21)
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



while True:
    pororo()
