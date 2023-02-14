#   Connects REQ socket to tcp://localhost:5555
#   Sends something to the server and expects a return message back
#

import zmq
import pickle
import serverFuncs

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#example getting weather for next three days in zip code 22181
socket.send(b"22181, 1")
#get reply/confirmation
message = socket.recv()
print(f"Received reply \n [ {bytes.decode(message)} ]")
print("\n")


#open the dictionary with the data from your request 
with open('weather.pickle', 'rb') as infile:
   weather = pickle.load(infile)

#can now explore nested dictionary 
#subdictionaries in weather['location'], weather['current'], and weather['forecast']

#print(f"In {weather['location']['_name']} the temperature is {weather['current']['_temp_c']} degrees celcius" )

#prints all keys in dictionary, including nested ones, so you can see what's available
serverFuncs.printKeys(weather, 0)
