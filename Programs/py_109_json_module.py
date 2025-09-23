import json

# Json Module : json module provides helper functions to work with json
#               dumps(dictionary) = takes dictonary as an input, returns string  
#               loads(dictionary) = takes string as input return dictionary
#        
#               dump(dictionary, file) = directly dump json string to the given file
#               load(file) = directly load json data from file and convert it into dictionary object

dic = {'name' : 'shubham', 'age' : 23, 'gender': 'male'}

dicStr = json.dumps(dic)

dictObj = json.loads(dicStr)

print(dicStr)
print(type(dicStr))

print('----')

print(dictObj)
print(type(dictObj))

file = open('data.json', 'w')
json.dump(dic, file)
file.close()

file = open('data.json', 'r')
jsonObj = json.load(file)
print('----')
print(jsonObj)
print(type(jsonObj))
file.close()

