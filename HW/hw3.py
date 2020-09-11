"""
Class: Python 2020
Homework Assignment 3
Author: Jin Kim
"""

# import necessary packages
import importlib
import sys
import tweepy

# set directory and get API key
sys.path.insert(0, '/Users/jinki/Documents/API keys')
twitter = importlib.import_module('start_twitter')
api = twitter.client

# get wustl user info
wustl = api.get_user('WUSTLPoliSci')

# get wustl followers info
wustl_followers = []
for follower in tweepy.Cursor(api.followers, id = 'WUSTLPoliSci').items(1000): # get upto 1000 followers
    wustl_followers.append(follower) # should I fix this to followers()?
len(wustl_followers) # 469 followers

# get wustl friend info
wustl_friends = []
for friend in tweepy.Cursor(api.friends, id = 'WUSTLPoliSci').items(1000): # get upto 1000 friends
    wustl_friends.append(friend)
len(wustl_friends) # 158 friends

# function for most active user
def most_active_user(userlist):
    activity = []
    for user in userlist:
        activity.append(user.statuses_count)
    most_active_user = userlist[activity.index(max(activity))]
    return "user id: {}, user name: {}, twitter handle: {}, tweets: {}, followers: {}".format(most_active_user.id, most_active_user.name, most_active_user.screen_name, most_active_user.statuses_count, most_active_user.followers_count)

# function for most popular user:
def most_popular_user(userlist):
    followers = []
    for user in userlist:
        followers.append(user.followers_count)
    most_popular_user = userlist[followers.index(max(followers))]
    return "user id: {}, user name: {}, twitter handle: {}, tweets: {}, followers: {}".format(most_popular_user.id, most_popular_user.name, most_popular_user.screen_name, most_popular_user.statuses_count, most_popular_user.followers_count)

##### One degree of separation #####
# 1) Among the followers of @WUSTLPoliSci who is the most active?
most_active_user(wustl_followers)
# 'user id: 810933338, user name: 十勝餡粒々@アメリカPh.D.リベンジ,
# twitter handle: tubuann_only, tweets: 109698, followers: 1439'

# 2) Among the followers of @WUSTLPoliSci who is the most popular,
# i.e. has the greatest number of followers?
most_popular_user(wustl_followers)
# 'user id: 84653850, user name: Brendan Nyhan,
# twitter handle: BrendanNyhan, tweets: 90590, followers: 81126'

# 3) Among the friends of @WUSTLPoliSci, i.e. the users she is following,
# who are the most active layman, expert, and celebrity?
# separate friends into 3 types (Layman, Expert, Celebrity)
layman = []
expert = []
celebrity = []
for friend in wustl_friends:
    if friend.followers_count < 100: # if less than 100 followers
        layman.append(friend) # assign layman
    elif friend.followers_count <= 1000: # between 100 - 1000 followers
        expert.append(friend) # assign expert
    else: # more than 1000 followers
        celebrity.append(friend) # assign celebrity


# find most active layman, expert, and celebrity
most_active_user(layman)
# 'user id: 764260766, user name: usman falalu,
# twitter handle: usmanfalalu1, tweets: 1445, followers: 30'
most_active_user(expert)
# user id: 1064533471, user name: Tim... we're doomed,
# twitter handle: prof_nokken, tweets: 12577, followers: 719
most_active_user(celebrity)
# 'user id: 807095, user name: The New York Times,
# twitter handle: nytimes, tweets: 406707, followers: 47255333'


# 4) Among the friends of @WUSTLPoliSci, who is the most popular?
most_popular_user(wustl_friends)
# 'user id: 813286, user name: Barack Obama,
# twitter handle: BarackObama, tweets: 15919, followers: 122336786'


##### Two degrees of Separation #####
##### Limit searches to layman and expert #####
# 1) Among the followers of @WUSTLPoliSci and their followers, who is the most active?

# limit wustl followers to layman and expert
limited_followers = []
# for loop
for user in wustl_followers:
    if user.followers_count <= 1000: # if up to 1000 followers
        limited_followers.append(user) # assign layman
    else:
        continue
len(limited_followers) # 366 layman and expert followers

# get layman and expert followers of limited followers
ffollowers = []
for user in limited_followers:
    try:
        for follower in tweepy.Cursor(api.followers, id = user.id).items(5000): # get upto 5000 friends
            if follower.followers_count <= 1000:
                ffollowers.append(follower)
    except tweepy.TweepError:
        continue

# combine followers of WUSTLPoliSci and followers of followers
full_followers = limited_followers + ffollowers

# get most active user
most_active_user(full_followers)
# 'user id: 871399252815204354, user name: Terry Egan,
# twitter handle: Terryg1979, tweets: 256668, followers: 115'


# 2) Among the friends of @WUSTLPoliSci and their friends, who is the most active?
# limit wustl friends to layman and expert
limited_friends = []
# for loop
for user in wustl_friends:
    if user.followers_count <= 1000: # if up to 1000 followers
        limited_friends.append(user) # assign layman
    else:
        continue
len(limited_friends) # 75 layman and expert friends

# get layman and expert friends of friends
ffriends = []
for user in limited_friends:
    try:
        for friend in tweepy.Cursor(api.friends, id = user.id).items(5000): # get upto 5000 friends
            if friend.followers_count <= 1000:
                ffriends.append(friend)
    except tweepy.TweepError:
        continue
len(ffriends) # 9174 layman and expert friends of friends

# add limited_friends and ffriends
full_friends = limited_friends + ffriends
len(full_friends) # 9249 friends and friends of friends

# find the most active user
most_active_user(full_friends)
# 'user id: 18701550, user name: El Yunke Obeezy,
# twitter handle: MissAir, tweets: 148141, followers: 671'
