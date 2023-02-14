####
#sending/receiving data to audrie's weather app using weatherapi.com and zmq 

#weather api stuff
from __future__ import print_function
from pprint import pprint
import swagger_client 
from swagger_client.rest import ApiException 
import config #has api key

#zmq stuff
import zmq
import time

#set up communication between server/client 
context = zmq.Context()
socket = context.socket(zmq.REP) 
socket.bind("tcp://*5555")

#configure api key authorization
configuration = swagger_client.Configuration() 
configuration['key'] = config.apiKey
#create instance of api class 
apiInstance = swagger_client.APIsApi(swagger_client.ApiClient(configuration))


#get request from client
while True:
   #receive message in format place, days
   message = socket.recv() 
   message = bytes.decode(message)
   place, days = message.split(',') 

   #get response 
   try:
      response = apiInstance.forecast(place, days) 
      print(response)
   except ApiException as e:
      pprint("Exception calling APIsApi -> forecast_weather: %s \n" % e)

   time.sleep(1)  

   socket.send(bytes(response, 'utf-8'))
