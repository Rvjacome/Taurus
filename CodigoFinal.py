from encoder_N20_esp import PID, Motor,Sensor
from time import sleep_ms, ticks_us
# Creating objects of each motor
m1 = Motor(9, 8, 7, 16, 17)
m2 = Motor(11, 12, 13, 18, 19)
pinSTBY = machine.Pin(10, machine.Pin.OUT)
pinSTBY.value(0)

# Creating PID objects for each motor
p1 = PID(m1, 5, 0.01, 0.0001, 800) 
p2 = PID(m2, 5, 0.01, 0.001, 800)

# Creating sensor objects 
S1 = Sensor(28,m1,m2,pinSTBY)

while(1):
  
  
  distancia_cm, _ = S1.leer_distancia()
  print("Distancia: {:.2f} cm".format(distancia_cm))

  if distancia_cm < 4:
      
      m1.forward()
      m2.forward()
      
  else:
 
      m1.reverse()
      m2.forward()
     
  sleep_ms(50)      
    
