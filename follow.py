# program to follow account you enter based on @name

import tweepy


def followAccount(api, userAccount):

    accountToFollow = input("Enter the twitter @ of the account you wish to follow: ")
    
    status = api.show_friendship(source_screen_name=userAccount,
                                     target_screen_name=accountToFollow)

    if status[0].following:
        print("You already follow @" + accountToFollow)
    else:
        name = api.create_friendship(screen_name = accountToFollow)
        print("Successfully followed @" + name.screen_name)  

def yesOrNo(api, userAccount):
    yn = input("Would you like to follow someone else? y/n: ")
    if yn == 'y'.lower():
        main()
    elif yn == 'n'.lower():
        print("You're done!")
    else:
        print("Invalid input")
        main()
        

def main():
    # Credentials go here (generate at: https://apps.twitter.com)
    auth = tweepy.OAuthHandler('4jg8N5linHnCn2yh7TfRvg8tE', 'coVxVnFXOlz3EY0FyKyMPNxmNEdRjA2Ewp545YnqvtrSPyd6qk')
    auth.set_access_token('635128344-KhtiQylAT8brKzlkQPDns5Z2dpbhw4wZCH9bvSE8', 'ZhJNMn3vDAOy4sWQB64OvmQ3WxIDkgWBLbDEhKqMoXHsu')

    # Connect to Twitter
    api = tweepy.API(auth)
    
    userAccount = input("Enter your twitter @: ")

    followAccount(api, userAccount)
    yesOrNo(api, userAccount)
main()
