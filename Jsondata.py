
#Importing jason file the class library.
import json

# Creation of a python object named data.

data= {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York, NY',
    'intrest':['Traveling','football','Golf','Running','Videogames','History'],
    'is_student': False
}

#creating a json and writing the phyton object content to the json.
with open('data.json','w') as json_file:

    json.dump(data,json_file, indent=4)

print ("Data has been written to data.jason")

#Reading the Json object.
with open('data.json','r') as json_file:

    #created an object called loaded data. Load the jason file into the argument parameter.
    loaded_data= json.load(json_file)

print("successfully able to read data.json")
print(loaded_data)

#Altering the JSON object.
loaded_data['age'] = 34 #<-ints
loaded_data['intrest'].append('secret Hobby')

#Rewrite the changes to the json file
with open('data.json','w') as json_file:

    json.dump(loaded_data,json_file, indent=4)

print ("Data has been written to data.jason")
