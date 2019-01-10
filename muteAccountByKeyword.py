# Mute accounts based on keyword search results
import tweepy

# Mute accounts based on if sign appears more than 5 times in a tweet
def muteAccounts(api):

    searchQuery = input('Enter the search keyword: ')
    
    search = api.search(q=searchQuery, count=100)

    muteString = input("Enter the character or string you want to mute accounts based on: ")
    
    # Traverses search tweet by tweet and mutes accounts where sign appears
    for tweet in search:    
        if (tweet.text.count(muteString.lower()) > 0):                
            name = api.create_mute(tweet.user.id)
            print(name.screen_name, "is now muted")

    yn = input("Would you like to search again? y/n: ")
    if yn == 'y':
        muteAccounts(api)
    else:
        print("You're done!")
       
def main():
    # Credentials go here (generate at: https://apps.twitter.com)
    auth = tweepy.OAuthHandler('4jg8N5linHnCn2yh7TfRvg8tE', 'coVxVnFXOlz3EY0FyKyMPNxmNEdRjA2Ewp545YnqvtrSPyd6qk')
    auth.set_access_token('635128344-KhtiQylAT8brKzlkQPDns5Z2dpbhw4wZCH9bvSE8', 'ZhJNMn3vDAOy4sWQB64OvmQ3WxIDkgWBLbDEhKqMoXHsu')

    # Connect to Twitter
    api = tweepy.API(auth)

    muteAccounts(api)
main()

