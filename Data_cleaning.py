import json
def clean_data(data):
    #Remove data with missing names
    data["users"]=[user for user in data["users"]if user["name"].strip()]

    #Remove duplicate friends
    for user in data["users"]:
        user["friends"]=list(set(user["friends"]))

    #Remove Inactive users
    data["users"]= [user for user in data["users"]if user["friends"] or user["liked_pages"]]
    
    return data

#Load the data
data=json.load(open("Data_2.json"))
data=clean_data(data)
json.dump(data,open("cleaned_data2.json","w"),indent=4)
print("Data has been cleaned successfully")
