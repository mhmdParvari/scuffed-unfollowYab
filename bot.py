import time
import os
import glob
import database
from instabot import Bot
cookie_del = glob.glob("config/*cookie.json")
if cookie_del : os.remove(cookie_del[0])
mybot= Bot()
def login(_username, _password):
    mybot.login(username= _username, password = _password)
    time.sleep(3)


# print('\nPeople who unfollowed you since the last session:')
def get_unfollowers(username):
    new_followers = mybot.get_user_followers(username)
    old_followers = database.read_all()
    result=[]
    for follower in old_followers:
        if new_followers.count(follower[0]) == 0:
            time.sleep(5)
            result.append(mybot.get_username_from_user_id(follower[0]))

    database.fill_with_list(new_followers)
    return result
print('')

# for following in following_list:
#     if follower_list.count(following) == 0:
#         time.sleep(5)
#         print(mybot.get_username_from_user_id(following))
