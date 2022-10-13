import requests

endpoint= "https://httpbin.org/anything"
endpoint="http://127.0.0.1:8000/"

resp=requests.get(endpoint.da)  #HTTP requests
print(resp.text)
# print(resp.json())


#HTTP REQUESTS -> Raw HTML
#REST -> json i.e javascript object notation ~ python dictionary
# Json can be converted to python using loads()
# Python to json using dumps()


#we basically need to perform these steps
# Complex Data Type -> Python data type -> Json data