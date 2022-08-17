from time import sleep, ticks_ms, sleep_ms, ticks_us, ticks_diff
from machine import Pin
import motor

prevT = 0
px = Pin(14, Pin.IN)  #encoder pin1 (C1)
py = Pin(27, Pin.IN)  #encoder pin2 (C2)
pos = 0

def convert(x, i_m, i_M, o_m, o_M):
    return max(min(o_M, (x - i_m) * (o_M - o_m) // (i_M - i_m) + o_m), o_m)

class PID:
    def __init__(self, kpIn, kdIn, kiIn, umaxIn, eprev=0, eintegral=0):
        self.kpIn = kpIn
        self.kdIN = kdIn
        self.kiIn = kiIn
        self.umaxIn  =umaxIn
        self.eprev = eprev
        self.eintegral = eintegral

    def evalu(self,value, target, deltaT):
        e = target-value
        dedt = (e-self.eprev)/(deltaT)
        self.eintegral = self.eintegral + e*deltaT
        u = self.kpIn*e + self.kdIN*dedt + self.kiIn*self.eintegral
        if u > 0:
            if u > self.umaxIn:
                u = self.umaxIn
            else:
                u = u
        else:
            if u < -self.umaxIn:
                u = -self.umaxIn
            else:
                u = u 
        return u
    
#Swap encoder pins if pos(position counter) value doesn't reduce when we reverse the direction of motor.
def handle_interrupt(pin):
    global pos
    a = px.value()
    if a > 0:
        pos = pos+1
    else:
        pos = pos-1

#interrpt handler(triggers interrupt when encoder 1 on Pin 27 goes high)
py.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt) 

p1 = PID(3,.1,0.001,1000) # set pid values PID(Propotional, derivative, integral, max correction speed)

def set(t):
    global prevT
    global py
    currT = ticks_us()
    deltaT = (currT - prevT)/(1000000)
    prevT = currT
    while(1):
        x = int(p1.evalu(pos, t, deltaT))
        motor.motorSpeed(x)
        print(pos, t)  # print curr positon and target point
        sleep_ms(10)


    

