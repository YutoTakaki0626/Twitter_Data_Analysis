import re

def remove_hashtag(tweets_list):
    '''
    ハッシュタグを除去する処理
    '''
    removed_list = []

    for tweet in tweets_list:
        while re.search(r'#', st) is not None:
            an = re.search(r'\n', st)
            start = an.span()[0]
            end = an.span()[1]
            tweet = str(tweet[:start]) + str(tweet[end:])
        hashtag_list.append(tweet)
 return removed_list