import json

filePath = 'C:\\Users\\Code\\Desktop\\'
fileName = 'FIX_FriendsDepth3.json'

dataUnsorted = []

with open(filePath + fileName,'r') as file:
    dataUnsorted = json.load(file)


print(type(dataUnsorted))

dataSorted = sorted(dataUnsorted)
print(type(dataSorted))

with open(filePath + 'SORTED_' + fileName, 'w') as file:
    json.dump(dataSorted, file)