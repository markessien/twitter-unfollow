import twitter
import settings
import time

api = twitter.Api(consumer_key=settings.CONSUMER_KEY,
                  consumer_secret=settings.CONSUMER_SECRET,
                  access_token_key=settings.ACCESS_TOKEN_KEY,
                  access_token_secret=settings.ACCESS_TOKEN_SECRET)



def unfollow_users():
    users = api.GetFriends()
    for i, u in enumerate(users):
        print("Unfollowing " + u.screen_name)
        api.DestroyFriendship(screen_name=u.screen_name)
        time.sleep(1)
        if i == 600:
            break


if __name__ == '__main__':
    unfollow_users()