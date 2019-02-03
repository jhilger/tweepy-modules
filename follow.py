# program to follow account you enter based on @name

import tweepy


def followAccount(api, userAccount):

    accountToFollow = input("Enter the twitter @ of the account you wish to follow: ")
    
    status = api.show_friendship(source_screen_name=userAccount,
                                     target_screen_name=accountToFollow)


