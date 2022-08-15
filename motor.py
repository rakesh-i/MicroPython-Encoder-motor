import machine
from machine import Pin, PWM
import time

#pin definition
p1 = machine.Pin(13, machine.Pin.OUT) // output 1
p2 = machine.Pin(12, machine.Pin.OUT) // output 2
p3 = machine.Pin(14) //PWM pin for speed control
pwm = machine.PWM(p3, freq=50)

#arduino "map" function implementation
def convert(x, i_m, i_M, o_m, o_M):
    return max(min(o_M, (x - i_m) * (o_M - o_m) // (i_M - i_m) + o_m), o_m)

#easy to use function for setting motor speed and direction
def motorSpeed(m1):
    pwm1 = convert(abs(m1),0, 1000, 0, 1000) 
    pwm.duty(pwm1)
    if m1>0:
        p1.on()
        p2.off()
    else:
        p1.off()
        p2.on()




