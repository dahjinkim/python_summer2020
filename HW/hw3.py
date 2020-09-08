# import necessary packages
import importlib
import sys
import tweepy

# set directory and get API key
sys.path.insert(0, '/Users/jinki/Documents/API keys')
twitter = importlib.import_module('start_twitter')
api = twitter.client

# get wustl user and follower info
wustl = api.get_user('WUSTLPoliSci')
wustl_followers = wustl.followers_ids()
len(wustl_followers) # 469 followers


##### One degree of separation #####
# 1) Among the followers of @WUSTLPoliSci who is the most active?
# most active follower loop
activity = []
for ids in wustl_followers: # iterate over follower ids
    user = api.get_user(ids) # get each user
    activity.append(user.statuses_count) # collect their number of tweets
most_active_id = wustl_followers[activity.index(max(activity))] # index by the maximum number of tweets
most_active_follower = api.get_user(most_active_id) # get user info

# most active follower info
print(most_active_follower.id) # 810933338
print(most_active_follower.name) # 十勝餡粒々@アメリカPh.D.リベンジ
print(most_active_follower.screen_name) # @ tubuann_only
print(most_active_follower.statuses_count) # 109681 tweets


# 2) Among the followers of @WUSTLPoliSci who is the most popular,
# i.e. has the greatest number of followers?
# most popular follower loop
followers = []
for ids in wustl_followers: # iterate over follower ids
    user = api.get_user(ids) # get each user
    followers.append(user.followers_count) # collect number of followers
most_popular_id = wustl_followers[followers.index(max(followers))] # index by the maximum number of followers
most_popular_follower = api.get_user(most_popular_id) # get user info

# most popular follower info
print(most_popular_follower.id) # 84653850
print(most_popular_follower.name) # Brendan Nyhan
print(most_popular_follower.screen_name) # @ BrendanNyhan
print(most_popular_follower.followers_count) # 81127 followers


# 3) Among the friends of @WUSTLPoliSci, i.e. the users she is following,
# who are the most active layman, expert, and celebrity?
# get friends of WUSTLPoliSci
wustl_friends = []
for friend in tweepy.Cursor(api.friends, id = 'WUSTLPoliSci').items(1000): # get upto 1000 friends
    wustl_friends.append(friend)
len(wustl_friends) # 158 friends

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

# function for finding the most active friend in each type
def most_active(types):
    activity = []
    if types == "layman":
        for user in layman: # iterate over layman users
            activity.append(user.statuses_count) # collect number of tweets
            active_user = layman[activity.index(max(activity))] # find the most active user
    elif types == "expert":
        for user in expert: # iterate over expert users
            activity.append(user.statuses_count)
            active_user = expert[activity.index(max(activity))]
    elif types == "celebrity":
        for user in expert: # iterate over celebrity users
            activity.append(user.statuses_count)
            active_user = celebrity[activity.index(max(activity))]
    else:
        print("Enter a valid type: layman, expert, celebrity")
    return print(types + "\nid: {}\nname: {}\nscreen_name: {}\ntweets: {}\nfollowers: {}".format(active_user.id, active_user.name, active_user.screen_name, active_user.statuses_count, active_user.followers_count))

# find most active layman, expert, and celebrity
most_active("layman")
# id: 764260766
# name: usman falalu
# screen_name: usmanfalalu1
# tweets: 1445
# followers: 30
most_active("expert")
# id: 1064533471
# name: Tim... we're doomed
# screen_name: prof_nokken
# tweets: 12577
# followers: 719
most_active("celebrity")
# id: 48028479
# name: WashU Residential Life
# screen_name: washureslife
# tweets: 519
# followers: 1033


# 4) Among the friends of @WUSTLPoliSci, who is the most popular?
followers = []
for friend in wustl_friends:
    followers.append(friend.followers_count)
most_popular_friend = wustl_friends[followers.index(max(followers))]

# most popular friend info
print(most_popular_friend.id) # 813286
print(most_popular_friend.name) # Barack Obama
print(most_popular_friend.screen_name) # @ BarackObama
print(most_popular_friend.followers_count) # 122336786 followers


##### Two degrees of Separation #####
##### Limit searches to layman and expert #####
# 1) Among the followers of @WUSTLPoliSci and their followers, who is the most active?

# limit wustl followers to layman and expert
limited_followers = []
# for loop
for follower in wustl_followers:
    user = api.get_user(follower)
    if user.followers_count <= 1000: # if up to 1000 followers
        limited_followers.append(follower) # assign layman
    else:
        continue
len(limited_follower) # 366 layman and expert followers

# get followers of limited followers
follower_follower = []
for follower in limited_follower:
    user = api.get_user(follower)
    follower_follower.append(user.followers_ids())

# limit follower_follower to layman and expert
limited_fofollower = []
for follower in follower_follower:
    user = api.get_user(follower)
    if user.followers_count <= 1000: # if up to 1000 followers
        limited_fofollower.append(follower) # assign layman
    else:
        continue

# combine followers of WUSTLPoliSci and followers of followers
# and check for duplicates
full_followers = limited_follower + limited_fofollower
set_full_followers = set(full_followers)
unique_full_followers = list(set_full_followers)

# get most active user
activity = []
for ids in unique_full_followers: # iterate over follower ids
    user = api.get_user(ids) # get each user
    activity.append(user.statuses_count) # collect their number of tweets
most_active_id = unique_full_followers[activity.index(max(activity))] # index by the maximum number of tweets
most_active_follower = api.get_user(most_active_id) # get user info

# most active follower info
print(most_active_follower.id) # 810933338
print(most_active_follower.name) # 十勝餡粒々@アメリカPh.D.リベンジ
print(most_active_follower.screen_name) # @ tubuann_only
print(most_active_follower.statuses_count) # 109681 tweets


# 2) Among the friends of @WUSTLPoliSci and their friends, who is the most active?
