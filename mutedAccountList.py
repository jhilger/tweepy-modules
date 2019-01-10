# Prints list and number of muted accounts

import tweepy

# Prints muted accounts
def getMutedAccounts(api):    
    mutes = api.mutes_ids()
    mutedAccountIds = mutes['ids']

    mutedAccountNames = []
    for muteId in mutedAccountIds:
        username = api.get_user(muteId)
        mutedAccountNames.append(username.screen_name)
    for name in mutedAccountNames:
        print(name)
    print("The total number of muted accounts is ", len(mutedAccountNames))

def main():
    # Credentials go here (generate at: https://apps.twitter.com)
    auth = tweepy.OAuthHandler('4jg8N5linHnCn2yh7TfRvg8tE', 'coVxVnFXOlz3EY0FyKyMPNxmNEdRjA2Ewp545YnqvtrSPyd6qk')
    auth.set_access_token('635128344-KhtiQylAT8brKzlkQPDns5Z2dpbhw4wZCH9bvSE8', 'ZhJNMn3vDAOy4sWQB64OvmQ3WxIDkgWBLbDEhKqMoXHsu')

    # Connect to Twitter
    api = tweepy.API(auth)

    getMutedAccounts(api)
    
main()
