# https://leetcode.com/problems/design-twitter/

class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followingList = defaultdict(set)
        self.orderId = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.orderId, tweetId))
        self.orderId-=1

    def getNewsFeed(self, userId: int) -> list[int]:
        result = []
        heap = []
        self.followingList[userId].add(userId)
        for foloweeId in self.followingList[userId]:
            index = len(self.tweets[foloweeId])-1
            if index>=0:
                orderId, tweetId = self.tweets[foloweeId][index]
                heap.append((orderId, foloweeId, tweetId, index-1))
        
        heapify(heap)
        while heap and len(result)<10:
            orderId, foloweeId, tweetId, index = heappop(heap)
            result.append(tweetId)
            if index>=0:
                orderId, tweetId = self.tweets[foloweeId][index]
                heappush(heap, (orderId, foloweeId, tweetId, index-1))

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followingList[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followingList[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)