import time
import sys
import ibmiotf.application
import ibmiotf.device
import random
import requests
import json

#Provide your IBM Watson Device Credentials
organization = "fdd82r"
deviceType = "Pi"        #Credentials of Watson IoT sensor simulator
deviceId = "123"
authMethod = "token"
authToken = "12345678"


# Initialize the device client.
try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()
while True:
    i = random.uniform(11.632299,13.130195)
    i=round(i,6)
    m=random.uniform(77.560710,80.255989)
    m=round(m,6)
    j=random.randint(60,90)
    k=random.randint(60,100)
    l=random.randint(100,140)
    #Send random data to node-red to IBM Watson
    data = { 'Latitude' : i, 'Longitude' : m, 'Heart Rate':k, 'Systole':l,"Diastole":j}
    print(data)
    def myOnPublishCallback():
        print("\nPublished gprs location = to IBM Watson\n")

    success = deviceCli.publishEvent("Data", "json", data, qos=0, on_publish=myOnPublishCallback)
    time.sleep(600)
    if not success:
        print("Not connected to IoTF")
    time.sleep(1)
    
deviceCli.disconnect()