# weatherMicroservice
A microservice for cs361 connecting to weatherapi.com and getting weather data from anywhere in the world for today and up to 10 days in the future.


## Getting started
After cloning the repository to your machine, you need to sign up for a free [weatherapi.com](https://www.weatherapi.com/signup.aspx) account to get an API key. With that key, add a python file to the directory called 'config.py' where the only line is this:

```python
apiKey = 'YOUR_API_KEY'
```

Once this is done, download swagger_client to access the API by running this in the terminal:

```sh
pip install git+https://github.com/weatherapicom/python.git
```

Install remaining requirements:
```sh
pip install -r requirements.txt
```

## Requesting data

To get weather in a location for the next x days, you want to request "place, x".Data sent through ZMQ has to be sent in bytes, so be sure to encode it in one of two ways:

>socket.send(b'place,  x')       #converts to binary
>socket.send('place, x'.encode('ASCII'))     #also converts to binary

You can request a place by naming a city, 
>socket.send(b'London, 7')    #weather in London for this week
or by using a zipcode/postalcode.
>socket.send(b'20500, 7')     #weather in Washington, DC for this week
>socket.send(b'EC3M, 7')      #weather in a subset of London for this week

## Receiving data

Once you've requested data, the server will return a pickle file in 'weather.pickle' that contains a nested dictionary with information on the location, the current weather, and the forecasted weather. Load the dictionary into your script like this:

```python
with open('weather.pickle', 'rb') as infile:
   weather = pickle.load(infile)
```
To print out all the keys so you can get an idea of what information you have access to, run this:

```python
serverFuncs.printKeys(weather)
```

Be warned, thuogh, since the forecasted weather gives updates by the day and hour, the output will be very long with many subdictionaries. If you only want to print the the location information and current weather, run this:

```python
serverFuncs.printKeys(weather['location'])
serverFuncs.printKeys(weather['current'])
```

After that, run weatherServer.py in a terminal. In a different terminal, run your client script and a text file with the response will be created in the directory.

Terminal 1:
```sh
python3 weatherService.py
```

Terminal 2:
```sh
python3 YOUR_CLIENT_SCRIPT.py
```