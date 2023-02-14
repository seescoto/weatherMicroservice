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

After that, run weatherServer.py in a terminal. In a different terminal, run your client script and a text file with the response will be created in the directory.