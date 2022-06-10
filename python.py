import json
dictionary =  {
"name" : "Meet",
"age"  : 23,
"salary" : 24000,
"role" : "B.tech",
"designation" : "Software Engineer"
} 
f = open("myfile.json","a")
y = json.dump(dictionary,f)
print(dict)



