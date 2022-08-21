from encoder_N20_esp.py import PID, Motor

# Creating objects of each motor
m1 = Motor(21, 22, 23, 16, 4)
m2 = Motor(19, 18, 5, 14, 27)

# Creating PID objects for each motor
p1 = PID(m1, 5, 0.1, 0.001, 800) 
p2 = PID(m2, 5, 0.1, 0.001, 800)

while(1):
  p1.setTarget(1000)
  p2.setTarget(-1000)
