# from firebase import firebase
# firebase = firebase.FirebaseApplication('https://kamath-bill-create.firebaseio.com/', None)
# result = firebase.get('/users', "GOLDEN")
# print (result)
# # {'1': 'John Doe', '2': 'Jane Doe'}




# import json
# from pprint import pprint

# with open('BIllDetails.json') as f:
#     data = json.load(f)
#     value = json['key']

# pprint(data["GOLDEN"]["NUMBER"]["310"])
# pprint(value)



import json
f = open("BIllDetails.json")
data = json.load(f)
f.close()
type(data)
# print(data["GOLDEN"])
for data in data["GOLDEN"]:
    print(data[0])