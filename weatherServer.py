####
#sending/receiving data to audrie's weather app using weatherapi.com and zmq 

#weather api stuff
from __future__ import print_function
from pprint import pprint
import swagger_client 
from swagger_client.rest import ApiException 
import config #has api key
#import pandas as pd #converting json api response to a text file
import json

#zmq stuff
import zmq
import time

#set up communication between server/client 
context = zmq.Context()
socket = context.socket(zmq.REP) 
socket.bind("tcp://*:5555")

#configure api key authorization
configuration = swagger_client.Configuration() 
configuration.api_key['key'] = config.apiKey
#create instance of api class 
apiInstance = swagger_client.APIsApi(swagger_client.ApiClient(configuration))


def convertToDict(response):
   #class swagger_client.models
   #goes through relevant properties and creates a nested dictionary 
   weatherDict = {} 
   
   #location info
   #vars(x) returns all properties of x, use this to make dictionary
   #delete all with unusable data
   locationDict= vars(response.location)
   toPop =[]
   for key in locationDict:
      if not isStatic(locationDict[key]) or locationDict[key] == None:
         toPop.append(key)
   for k in toPop:
      locationDict.pop(k)

   #weather of today
   currDict = vars(response.current) 
   toPop =[]
   for key in currDict:
      if not isStatic(currDict[key] or currDict[key] == None):
         toPop.append(key)
   for k in toPop:
      currDict.pop(k)

   #weather for the next x days (specified in request)
   forecastDict = vars(response.forecast)
   toPop = []
   for key in forecastDict:
      if not isStatic(forecastDict[key] or forecastDict[key] == None):
         toPop.append(key)
   for k in toPop:
      forecastDict.pop(k)

   weatherDict['location'] = locationDict 
   weatherDict['current'] = currDict
   weatherDict['forecast'] = forecastDict

   return weatherDict

   

def isStatic(variable):
   #returns if the variable is a non static variable (anything thats not int, float, str, etc.)
   #so we dont have a list as a dictionary key
   ret = False
   t = type(variable) 

   if t == str or t == int or t == float:
      ret = True
   
   return ret
#get request from client
while True:
   #receive message in format place, days
   message = socket.recv() 
   message = bytes.decode(message)
   place, days = message.split(',') 

   #get response 
   try:
      response = apiInstance.forecast_weather(place, days)
      response = convertToDict(response)
      pprint(response.keys())
      pprint(response['location'].keys())
   except ApiException as e:
      pprint("Exception calling APIsApi -> forecast_weather: %s \n" % e)

   time.sleep(1)  

   socket.send(b'response')
