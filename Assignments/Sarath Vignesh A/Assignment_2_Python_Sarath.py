import random
import time
temp_limit=int(input("Enter the threshold value of temperature from 1C to 100C:"))
humidity_limit=int(input("Enter the humidity threshold value from 1% to 50%:")) 
humidity_alarm=0 
temp_alarm=0     
#Alarm beeps  when temperature is greater than the threshold or humidity lesser than the threshold 
# or both happens at the same time
#In While loop Continously the values of temperature and Humidity values are checked
while(True):     #Continously generate temp and humidity value and set the value of alarms accordingly and display the information 
    temp=random.uniform(1,100)
    humidity=random.uniform(1,50)     
    print("Current temperature value is {0:.2f}".format(temp)) 
    print("Current humidity value is {0:.2f} %".format(humidity))
    time.sleep(1)
    if temp>=temp_limit and humidity<=humidity_limit:
        temp_alarm=1  
        humidity_alarm=1 
        print("Both the alarms are ON\n")
        time.sleep(2) 
    elif humidity<=humidity_limit :
        temp_alarm=0 
        humidity_alarm=1 
        print("Humidity alarm is ON and Temperature alarm is OFF \n")
        time.sleep(2)
    elif temp>=temp_limit:
        temp_alarm=1  
        humidity_alarm=0
        print("Humidity alarm is OFF and Temperature alarm is ON \n")
        time.sleep(2)
    else:
        temp_alarm=0
        humidity_alarm=0
        print("Both alarms are OFF \n")
        time.sleep(2)
 
