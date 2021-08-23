import re

def count_the_number_of_user_mention(tweets_list):
    '''
    ユーザーメンションの個数を数える
    '''

    user_mention_list = []

    for tweet in tweets_list:
        if tweet[0] == '@':
            user_mention_list.append(tweet)

        if re.search(r'@[0-9a-zA-Z_]+\s', tweet) is not None:
            user_mention_list.append(tweet)

        if re.search(r'@[0-9a-zA-Z_]{4,}', tweet) is not None:
            user_mention_list.append(tweet)

    user_mention_list = list(set(user_mention_list))
    user_mention_cnt = len(user_mention_list)
            
    return user_mention_cnt, user_mention_list

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
            
    return url_cnt, url_list

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

def count_w(tweets_list):
    hashtag_cnt = 0
    hashtag_list = []

    for tweet in tweets_list:
        if re.search(r'ww+', tweet) is not None:
            hashtag_list.append(tweet)

    for tweet in tweets_list:
        if tweet[-1] == str:
            if tweet[-1] == 'w':
                hashtag_list.append(tweet)

    hashtag_list = list(set(hashtag_list))

    hashtag_cnt = len(hashtag_list)
            
    return hashtag_cnt, hashtag_list



def count_the_number_of_w(tweets_list):
    '''
    wの数を数える（末尾）
    if len(tweet) == 0:
            continue
    '''
    
    w_list = []
    
    for tweet in tweets_list:
        contexts = tweet.strip()
        for context in contexts:
            if context[-1]=='w':
                w_list.append(tweet)
                break
        
    for tweet in tweets_list:
        if re.search(r'ww+', tweet) is not None:
            if tweet[-1] != 'w':
                w_list.append(tweet)

    w_list = list(set(w_list))

    return w_list

def count_the_number_of_not_single(tweets_list):
    '''
    英単語２文字以上のものをかぞえる
    '''

    not_single_list = []

    for tweet in tweets_list:
        if re.search(r'[a-zA-Z][a-zA-Z]+', tweet) is not None:
            not_single_list.append(tweet)
            
    return not_single_list


