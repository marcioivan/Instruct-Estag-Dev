import urllib.request, json

def getWebsites(data):
    print("-> Users's websites:")
    for item in data:
        print("{}".format(item["website"]))
    print("")

def getEmail(data):
    for item in data:
        if(item["username"] == "Samantha") :
            print("-> Samantha's email:\n{}\n".format(item["email"]))
            return

def getUsersSouthHem(data):
    users = 0
    for item in data:
        if(float(item["address"]["geo"]["lat"]) < 0) :
            users += 1
    print("-> Number of users in the south hemisphere:\n{}".format(users))

with urllib.request.urlopen("http://jsonplaceholder.typicode.com/users") as url:
    data = json.loads(url.read().decode())
    getWebsites(data)
    getEmail(data)
    getUsersSouthHem(data)
