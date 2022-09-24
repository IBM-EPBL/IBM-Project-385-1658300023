import random
import time
thresh1=int(input("Enter the threshold value for temperature:"))
thresh2=int(input("Enter the threshold value for humidity:")) 
hu=0
tp=0     

while(True):     
    temp=random.uniform(1,100)
    humidity=random.uniform(1,50)     
    print("temperature is : {0:.2f}".format(temp)) 
    print("humidity is : {0:.2f} %".format(humidity))
    time.sleep(1)
    if temp>=thresh1 and humidity<=thresh2:
        tp=1  
        hu=1 
        print("\nHIGH ALERT\nHumidity alarm and Temperature alarm are ON \n")
        time.sleep(2) 
    elif humidity<=thresh2:
        tp=0
        hu=1 
        print("\nHumidity alarm is ON and Temperature alarm is OFF \n")
        time.sleep(2)
    elif temp>=thresh1:
        tp=1  
        hu=0
        print("\nHumidity alarm is OFF and Temperature alarm is ON \n")
        time.sleep(2)
    else:
        tp=0
        hu=0
        print("\nBoth alarms are OFF \n")
        time.sleep(2)