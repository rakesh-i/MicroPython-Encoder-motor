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
p = PID(3, 0, 10, 800)  # PID(Propotional, Derivative, Integral, Max correction speed)
# Create a loop
# Call setSpeed method in a loop
while(1):
  p.setSpeed(100,m)             # setSpeed(Speed in RPM, Motor object)
  #p.setSpeed(-100,m)           # For reverse direction
```
#### Note: Swap the C1 and C2 pins if encoder counts in only one direction
### Closed loop position control
```
from encoder_N20_esp import Motor, PID
m = Motor(21, 22, 23, 16, 4)
p = PID(5, 0.1, .001, 800)      # Tested Pid values for 12v 500rpm N20 motor
while(1):
  p.setTarget(1000, m)          # setTarget(Number of encoder ticks, Motor object)
```
Check the multi_motor.py for multiple motor contorl.

[wire]: media/wire.png
