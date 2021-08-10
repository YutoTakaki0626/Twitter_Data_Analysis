import re

def improve_new_line(strings):
    '''
    \nを除去する処理
    '''
    new_list = []

    for st in strings:
        while re.search(r'\n', st):
            an = re.search(r'\n', st)
            start = an.span()[0]
            end = an.span()[1]
            st = str(st[:start]) + str(st[end:])
        new_list.append(st)
        
    # return new_list

def count_the_number_of_user_mention(tweets_list):
    '''
    ユーザーメンションの個数を数える
    '''
    
    user_mention_cnt = 0
    user_mention_list = []

    for tweet in tweets_list:
        if tweet[0] == '@':
            user_mention_cnt += 1
            user_mention_list.append(tweet)
            
    return user_mention_cnt

def count_the_number_of_url(tweets_list):
    '''
    URlの数を数える
    '''

    url_cnt = 0
    url_list = []

    for tweet in tweets_list:
        if re.search(r'http', tweet) is not None:
            url_cnt += 1
            url_list.append(tweet)
            
    return url_cnt

def count_the_number_of_hashtag(tweets_list):
    '''
    ハッシュタグの数を数える
    '''

    hashtag_cnt = 0
    hashtag_list = []

    for tweet in tweets_list:
        if re.search(r'#', tweet) is not None:
            hashtag_cnt += 1
            hashtag_list.append(tweet)
            
    return hashtag_cnt

