import random
import time

acttime = time.time() 
while True:
    temp = random.uniform(15,25)
    time.sleep(4)
    if(temp > 21):
        print("Alarm goes on")
        
    else:
        print("Alarm goes off")
    if acttime + 30 < time.time() :
        print("Entire system goes down")
        break
