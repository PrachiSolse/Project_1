import json

# Lets write a function to load data
def load_data(filename):
    with open(filename,"r") as f:
        data=json.load(f)
    return data

data=load_data("data.json")
print(type(data))


# Write a function to display users and their connections
def display_users(data):
    print("Users and their connections:\n")
    for user in data['users']:
        print(f" {user['id']}.{user['name']} is friends with {user['friends']} and liked pages are {user['liked_pages']}")
    print("\npages information:")

    for page in data['pages']:
        print(f"{page['id']}:{page['name']}")

display_users(data)