####
#sending/receiving data to audrie's weather app using weatherapi.com and zmq 

#weather api
from __future__ import print_function
from pprint import pprint
import swagger_client 
from swagger_client.rest import ApiException 

#zmq 
import zmq
import time

#additional 
import config #has api key
import serverFuncs #additional functions for converting api response for the client
import pickle 

#set up communication between server/client 
context = zmq.Context()
socket = context.socket(zmq.REP) 
socket.bind("tcp://*:5555")

#configure api key authorization
configuration = swagger_client.Configuration() 
configuration.api_key['key'] = config.apiKey
#create instance of api class 
apiInstance = swagger_client.APIsApi(swagger_client.ApiClient(configuration))


#get request from client
while True:
   #receive message in format [place, days]
   message = socket.recv() 
   message = bytes.decode(message)
   place, days = message.split(',') 


   try:
      #get response, convert to dictionary
      response = apiInstance.forecast_weather(place, days)
      response = serverFuncs.convertToDict(response)
      #save dictionary in pickle file 
      with open('weatherDict.pickle', 'wb') as outfile:
         pickle.dump(response, outfile, protocol=pickle.HIGHEST_PROTOCOL)

   except ApiException as e:
      pprint("Exception calling APIsApi -> forecast_weather: %s \n" % e)

   time.sleep(1)  

   socket.send(b'Data in file \"weatherDict.pickle\".')
