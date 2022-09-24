import random
import time

actual_time = time.time() 
while True:
    #random function to generate room temperature
    curr_temp = random.uniform(15,25)
    time.sleep(3)
    if curr_temp > 21:
        print("Alarm sets on")
        
    else:
        print("Alarm sets off")
    #To break the loop explicitly
    if actual_time + 40 < time.time() :
        print("Supervising time out of range")
        break
