# MicroPython-Encoder-motor
Closed loop(PID) speed and position control library for N20 motors with encoders.
## Wiring example
![Schematic][wire]
## Usage
### Open loop speed control
```
from encoder_N20_esp import Motor
# Create a motor object
m = Motor(21, 22, 23, 16, 4)  # Motor(M1, M2, EN, C1, C2, frequency) Default frequency is set at 50Hz
# Call the speed method using the  Motor object(m)
# Speed range from -1000 to 1000(10 bit resolution). 
m.speed(100)  
# "-" symbol before the value suggests reverse direction of the rotation 
# m.speed(-100)               # For reverse direction
```
### Closed loop speed control
```
from encoder_N20_esp import Motor, PID
m = Motor(21, 22, 23, 16, 4)  # Motor object
# Create a PID object  with desired PID values(tested PID values for 12v 500rpm N20 motor)
p = PID(m, 3, 0, 10, 800)  # PID(Motor object, Propotional, Derivative, Integral, Max correction speed)
# Create a loop
# Call setSpeed method in a loop
while(1):
  p.setSpeed(100)             # setSpeed(Speed in RPM, Motor object)
  #p.setSpeed(-100)           # For reverse direction
```

### Closed loop position control
```
from encoder_N20_esp import Motor, PID
m = Motor(21, 22, 23, 16, 4)
p = PID(m, 5, 0.1, .001, 800)      # Tested Pid values for 12v 500rpm N20 motor
while(1):
  p.setTarget(1000)          # setTarget(Number of encoder ticks)
```
Check the multi_motor.py for multiple motor contorl.
#### Note1: Swap the C1 and C2 pins if encoder counts in only one direction
#### Note2: To stop the motor set the motor speed to 0 by using "m.speed(0)" line.
#### Note3: When you exit the loop, remember to set the motor speed to 0 just after the exit.
#### Note4: Time delta is pre defined in the setTarget and setSpeed methods due to a bug in MicroPython. You can see the source code on how to overide it. (Do at you own will, results may vary)

[wire]: media/wire.png
