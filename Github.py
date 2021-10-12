import requests
import json
# username = input("Enter the github username:")
# request = requests.get('https://api.github.com/users/' +
#                        username)

username = "szeichner"
url = 'https://api.github.com/users/{}'.format(username)
response = requests.get(url)
# json = request.json()

output = json.loads(response.text)

print(output)

# for i in range(len(output)):
#     print(output[i]["login"])

# fp = open("Json.json", "w")
# fp.write(str(json))
# fp.close()

# print("Hello")
# print(len(json))

# for i in range(len(json)):
#     print("Hello", json[i], "\n")

#     print("Project Number:", i+1)
#     print("Project Name:", json[i]['name'])
#     print("Project URL:", json[i]['svn_url'], "\n")
