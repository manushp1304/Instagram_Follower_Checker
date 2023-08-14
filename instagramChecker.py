import json

followers = open("NameOfDownloadedFolder/followers_and_following/followers_1.json")
followersData = json.load(followers)


following = open("NameOfDownloadedFolder/followers_and_following/following.json")
followingData = json.load(following)

followerList = []

for x in followersData:
    user = x['string_list_data']
    userDict = user[0]
    followerList.append(userDict['value'])

DataDict = followingData['relationships_following']
for user in DataDict:
    if user['string_list_data'][0]['value'] not in followerList:
        print(user['string_list_data'][0]['value'])
    
followers.close()
following.close()
