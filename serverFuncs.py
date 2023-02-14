###
#helper functions for weather microservice
#cleans up the server code for easier understanding

def isStatic(variable):
   #returns if the variable is a non static variable (anything thats not int, float, str, etc.)
   #so we dont have a list as a dictionary key
   ret = False
   t = type(variable) 

   if t == str or t == int or t == float:
      ret = True
   
   return ret

def convertToDict(response):
   #response is of class swagger_client.models
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

def printKeys(dictionary):
   #prints keys of a dictionary, even if it's nested
   # #(recursive)
   for key in dictionary:
      if type(dictionary[key]) == dict:
         print(f"subdictionary {key}:")
         printKeys(dictionary[key])
         print()
      else:
         print(key)


