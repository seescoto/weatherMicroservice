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

def toWeatherDict(response):
   #response is of class swagger_client.models
   #goes through relevant properties and creates a nested dictionary 
   weatherDict = {'location': toDict(response.location), 
                  'current': toDict(response.current),
                  'forecast': toDict(response.forecast)} 
   
   
   
   #weatherDict['location'] = toDict(response.location)
   #weatherDict['current'] = toDict(response.current)
   #weatherDict['forecast'] = toDict(response.forecast)

   return weatherDict


def toDict(response):
   #generic making of dictionary from a property of swagger_client.models
   #recursive, allows for double, triple, etc. nested dicts

   toPop = []

   if isStatic(response):
      newDict = response
   
   #test if it's a list, then the keys will be 0, 1, etc. 
   elif type(response) == list:
      newDict = {}
      for i in range(len(response)):
         newDict[i] = toDict(response[i])
         if newDict[i] == None:
            toPop.append(i)

      #delete all in toPop
      for key in toPop:
         newDict.pop(i)

   else:
      try:
         newDict = vars(response)
         for key in newDict:
            newDict[key] = toDict(newDict[key])
            #if the value is none add it to a list to delete
            if newDict[key] == None:
               toPop.append(key)

         #delete all in toPop 
         for key in toPop:
            newDict.pop(key)

      except TypeError:
         newDict = None #if type error, return none so key/val pair will be deleted later
      
   return newDict

def printKeys(dictionary):
   keyPrintHelper(dictionary,0)

def keyPrintHelper(dictionary, sublevel):
   #prints keys of a dictionary, even if it's nested
   #(recursive)
   #sublevel > 0 means there will be sublevel tabs before the printed values
   tabs = "\t" * sublevel

   for key in dictionary:
      if type(dictionary[key]) == dict:
         print()
         print(f"{tabs} subdictionary {key}:")
         keyPrintHelper(dictionary[key], sublevel + 1)
      else:
         print(tabs, key)


