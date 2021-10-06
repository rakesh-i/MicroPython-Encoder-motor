from machine import Pin
import time
import motor

p1 = Pin(27, Pin.IN)
p2 = Pin(26, Pin.IN)

target = 10000          #Target position of encoder
speed = 500         
last_pos = 0
w = 0
KP = .12
KD = .1
KI = .00005
max_correction = 500    #Maximum speed of the motor 

pos = 0

def convert(x, i_m, i_M, o_m, o_M):
    return max(min(o_M, (x - i_m) * (o_M - o_m) // (i_M - i_m) + o_m), o_m)

#
def correction(revolutions):
    if revolutions > 0:
        if revolutions > max_correction:
            revolutions = max_correction
        else:
            revolutions = revolutions
    else:
        if revolutions < -max_correction:
            revolutions = -max_correction
        else:
            revolutions = revolutions 
    return revolutions

#Swap encoder pins if pos(position counter) value doesn't reduce when we reverse the direction of motor.
def handle_interrupt(pin):
    global pos
    a = p2.value()
    if a > 0:
        pos = pos+1
    else:
        pos = pos-1

#interrpt handler(triggers interrupt when encoder 1 on Pin 27 goes high)
p1.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt) 

while(1):
    propotional = target- pos
    derivative = target - last_pos
    integral = target +last_pos
    rotate = (propotional*KP + derivative*KD + integral*KI)
    r = int(correction(rotate))
    motor.motorSpeed(r)
    last_pos = pos
    print(pos, r)
    
    time.sleep(.1) #Add atleast .01sec delay for stable terminal

