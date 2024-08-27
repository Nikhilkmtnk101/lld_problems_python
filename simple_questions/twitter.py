"""
Problem Statement:
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user,
and is able to see the 10 most recent tweets in the user's news feed.
"""


# Models
import datetime
import uuid
from threading import Lock, RLock


class User:
    def __init__(self, user_id, user_name, email, phone):
        self.user_id = user_id
        self.user_name = user_name
        self.email = email
        self.phone = phone

    def get_user_id(self):
        return self.user_id

    def set_user_id(self, user_id):
        self.user_id = user_id

    def get_user_name(self):
        return self.user_name

    def set_user_name(self, user_name):
        self.user_name = user_name

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.user_id = phone


class Tweet:
    def __init__(self, tweet_id, content, owner_id, created_at):
        self.tweet_id = tweet_id
        self.content = content
        self.owner_id = owner_id
        self.created_at = created_at

    def get_tweet_id(self):
        return self.tweet_id

    def set_tweet_id(self, tweet_id):
        self.tweet_id = tweet_id

    def get_content(self):
        return self.content

    def set_content(self, content):
        self.content = content

    def get_owner_id(self):
        return self.owner_id

    def set_owner_id(self, owner_id):
        self.owner_id = owner_id

    def get_created_at(self):
        return self.created_at

    def set_created_at(self, created_at):
        self.created_at = created_at


class Followers:
    def __init__(self, followers_id, follower_id, followee_id):
        self.followers_id = followers_id
        self.follower_id = follower_id
        self.followee_id = followee_id

    def get_followers_id(self):
        return self.followers_id

    def set_followers_id(self, followers_id):
        self.followers_id = followers_id

    def get_follower_id(self):
        return self.follower_id

    def set_follower_id(self, follower_id):
        self.follower_id = follower_id

    def get_followee_id(self):
        return self.followee_id

    def set_followee_id(self, followee_id):
        self.followee_id = followee_id


class UserRepository:
    def __init__(self):
        self.lock = Lock()
        self.user_id_vs_user = {}

    def create_user(self, user_name, email, phone):
        user_id = uuid.uuid4()
        user = User(user_id, user_name, email, phone)
        self.lock.acquire()
        self.user_id_vs_user[user_id] = user
        self.lock.release()
        return user_id

    def get_user_by_user_id(self, user_id):
        self.lock.acquire()
        user = self.user_id_vs_user.get(user_id, None)
        self.lock.release()
        return user


class TweetRepository:
    def __init__(self):
        self.lock = Lock()
        self.owner_id_vs_tweets = {}
        self.tweet_id_vs_tweets = {}

    def create_tweet(self, content, owner_id):
        tweet_id = uuid.uuid4()
        created_at = datetime.datetime.now()
        tweet = Tweet(tweet_id, content, owner_id, created_at)
        self.lock.acquire()
        self.tweet_id_vs_tweets[tweet_id] = tweet
        if not self.owner_id_vs_tweets.get(owner_id, None):
            self.owner_id_vs_tweets[owner_id] = []
        self.owner_id_vs_tweets[owner_id].append(tweet)
        self.lock.release()
        return tweet_id

    def get_tweets_by_owner_id(self, owner_id):
        self.lock.acquire()
        tweets = self.owner_id_vs_tweets.get(owner_id, None)
        self.lock.release()
        return tweets


class FollowersRepository:
    def __init__(self):
        self.lock = RLock()
        self.follower_id_vs_followers = {}
        self.followee_id_vs_followers = {}
        self.followers_id_vs_followers = {}

    def __remove_from_followers_list(self, followers_list, followers_id):
        self.lock.acquire()
        idx = -1
        for i in range(0, len(followers_list)):
            if followers_list[i].get_followers_id() == followers_id:
                idx = i
        if idx >= 0:
            followers_list.pop(idx)
        self.lock.release()

    def create_follower(self, follower_id, followee_id):
        followers_id = uuid.uuid4()
        followers = Followers(followers_id, follower_id, followee_id)
        self.lock.acquire()

        self.followers_id_vs_followers[followers_id] = followers

        if not self.follower_id_vs_followers.get(follower_id, None):
            self.follower_id_vs_followers[follower_id] = []
        self.follower_id_vs_followers[follower_id].append(followers)

        if not self.followee_id_vs_followers.get(followee_id, None):
            self.followee_id_vs_followers[followee_id] = []
        self.followee_id_vs_followers[followee_id].append(followers)

        self.lock.release()

        return followers_id

    def remove_follower(self, follower_id, followee_id):
        self.lock.acquire()

        followers_id = None
        followers = self.follower_id_vs_followers.get(follower_id, [])
        for follower in followers:
            if followee_id==follower.get_followee_id():
                followers_id = follower.get_followers_id()
                break

        if followers_id:
            self.__remove_from_followers_list(self.follower_id_vs_followers.get(follower_id, []), followers_id)
            self.__remove_from_followers_list(self.followee_id_vs_followers.get(followee_id, []), followers_id)
            self.followers_id_vs_followers.pop(followers_id, None)

        self.lock.release()

    def get_followers_by_follower_id(self, follower_id):
        return self.follower_id_vs_followers.get(follower_id, [])


class TwitterService:
    def __init__(self):
        self.user_repository = UserRepository()
        self.tweet_repository = TweetRepository()
        self.followers_repository = FollowersRepository()

    def create_user(self, user_name, email, phone):
        return self.user_repository.create_user(user_name, email, phone)

    def create_tweet(self, owner_id, content):
        return self.tweet_repository.create_tweet(content, owner_id)

    def follow_user(self, follower_id, followee_id):
        return self.followers_repository.create_follower(follower_id, followee_id)

    def unfollow_user(self, follower_id, followee_id):
        self.followers_repository.remove_follower(follower_id, followee_id)

    def get_feed(self, user_id):
        followers_list = self.followers_repository.get_followers_by_follower_id(follower_id=user_id)
        tweets = []
        for followers in followers_list:
            followee_id = followers.get_followee_id()
            followee_tweets = self.tweet_repository.get_tweets_by_owner_id(owner_id=followee_id)
            tweets += followee_tweets

        tweets.sort(key=lambda x: x.created_at, reverse=True)
        return tweets


if __name__ == '__main__':
    # Create an instance of TwitterService
    twitter_service = TwitterService()

    # Create a new user
    user_id_1 = twitter_service.create_user("JohnDoe", "johndoe@example.com", "1234567890")
    print(f"User Created: {user_id_1}")

    # Assuming the user_id returned from creating a user is 1
    tweet = twitter_service.create_tweet(owner_id=user_id_1, content="Hello, this is my first tweet!")
    print(f"Tweet Created: {tweet}")

    # Assuming the user_id returned from creating a user is 1
    tweet1 = twitter_service.create_tweet(owner_id=user_id_1, content="Hello, this is my second tweet!")
    print(f"Tweet Created: {tweet}")

    # Create another user to follow
    user_id_2 = twitter_service.create_user("JaneDoe", "janedoe@example.com", "0987654321")

    # Follow the user
    follow = twitter_service.follow_user(follower_id=user_id_2, followee_id=user_id_1)
    print(f"Follow Status: {follow}")

    # Unfollow the user
    twitter_service.unfollow_user(follower_id=user_id_2, followee_id=user_id_1)
    print("Unfollowed the user")

    # Fetch the feed for the user
    tweets = twitter_service.get_feed(user_id=user_id_2)
    for tweet in tweets:
        print(f"Tweet Id: {str(tweet.get_tweet_id())}, User Id: {str(tweet.get_owner_id())}, Content: {str(tweet.get_content())}, "
              f"created_at: {str(tweet.get_created_at())}")

