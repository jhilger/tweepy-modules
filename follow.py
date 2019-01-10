# simple program to follow whatever account you enter based on @name

import tweepy

# Credentials go here (generate at: https://apps.twitter.com)
auth = tweepy.OAuthHandler('4jg8N5linHnCn2yh7TfRvg8tE', 'coVxVnFXOlz3EY0FyKyMPNxmNEdRjA2Ewp545YnqvtrSPyd6qk')
auth.set_access_token('635128344-KhtiQylAT8brKzlkQPDns5Z2dpbhw4wZCH9bvSE8', 'ZhJNMn3vDAOy4sWQB64OvmQ3WxIDkgWBLbDEhKqMoXHsu')

# Connect to Twitter
api = tweepy.API(auth)

accountToFollow = "jack"

# follow account
name = api.create_friendship(screen_name = accountToFollow)
print("Successfully followed @", name.screen_name)
