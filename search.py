from IPython.display import display
import snscrape.modules.twitter as sntwitter
import pandas as pd

def searchKeyword(keyword):
    tweets_list = []

    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(keyword + ' since:2020-11-01 until:2021-01-01 ').get_items()):
        if i>20:
            tweets_df1.to_csv('ManchesterUnited.csv')
        tweets_list.append([tweet.id,tweet.inReplyToTweetId,tweet.conversationId,tweet.user.username, tweet.rawContent,tweet.lang,tweet.date,tweet.user.location,tweet.likeCount, tweet.replyCount,tweet.retweetCount,
tweet.user.followersCount,tweet.user.renderedDescription,tweet.user.friendsCount, tweet.user.statusesCount,tweet.user.favouritesCount,tweet.user.listedCount,
tweet.user.mediaCount, tweet.url, tweet.hashtags, tweet.source])
        tweets_df1 = pd.DataFrame(tweets_list, columns=['TweetId', 'Replyto', 'conversationId', 'username', 'rawContent', 'language','date', 'location', 'likeCount', 'replyCount', 'retweetCount', 'followersCount', 
                                                         'renderedDescription','friendsCount','statusesCount','favouritesCount','listedCount','mediaCount','url','hashtags','source'])
        
        


def searchKeywordWithTimeRange(keyword, since, until):
    tweets_list = []

    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(keyword + ' since:' + since + ' until:' + until).get_items()):
        if i>1000:
            tweets_df1.to_csv('ManchesterUnited.csv')
        tweets_list.append([tweet.id,tweet.inReplyToTweetId,tweet.conversationId,tweet.user.username, tweet.rawContent,tweet.lang,tweet.date,tweet.user.location,tweet.place,tweet.likeCount, tweet.replyCount,tweet.retweetCount,
tweet.user.followersCount,tweet.user.renderedDescription,tweet.user.friendsCount, tweet.user.statusesCount,tweet.user.favouritesCount,tweet.user.listedCount,
tweet.user.mediaCount, tweet.url, tweet.hashtags, tweet.source,  tweet.viewCount, tweet.mentionedUsers])
        tweets_df1 = pd.DataFrame(tweets_list, columns=['TweetId', 'Replyto', 'conversationId', 'username', 'rawContent', 'language','date', 'location','place' ,'likeCount', 'replyCount', 'retweetCount', 'followersCount', 
                                                         'renderedDescription','friendsCount','statusesCount','favouritesCount','listedCount','mediaCount','url','hashtags','source','viewCount','mentionedUsers'])
        
    