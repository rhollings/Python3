import json

#JSON ex: a dictionary
x = '{ "name":"John", "age":30, "city":"New York"}'

#parse thru x:
y = json.loads(x)

#the result is a Python dictionary:
print(y["age"])
