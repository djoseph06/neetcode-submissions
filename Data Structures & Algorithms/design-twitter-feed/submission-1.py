class Twitter:

    def __init__(self):
        self.following = {}
        self.tweets = {}
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:

        if userId not in self.tweets:
            self.tweets[userId] = []

        self.tweets[userId].append((self.time, tweetId))
        self.time += 1


        

    def getNewsFeed(self, userId: int) -> List[int]:
        all_tweets = []

        users = {userId}

        if userId in self.following:
            users.update(self.following[userId])

        for user in users:
            if user in self.tweets:
                all_tweets.extend(self.tweets[user])

        all_tweets.sort(reverse = True)

        result = []

        for time, tweetId in all_tweets[:10]:
            result.append(tweetId)
            
        return result




        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()

        self.following[followerId].add(followeeId)
        
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)
        