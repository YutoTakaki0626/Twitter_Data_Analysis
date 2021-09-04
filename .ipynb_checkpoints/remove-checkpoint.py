import re
import string

def remove_new_line_marks(strings):
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
        
    return new_list

def remove_all_blanks(strings):
    '''
    全空白を除去する処理
    '''
    new_list = []

    for st in strings:
        while re.search(r'\u3000', st):
            an = re.search(r'\u3000', st)
            start = an.span()[0]
            end = an.span()[1]
            st = str(st[:start]) + str(st[end:])
        new_list.append(st)
        
    return new_list

def remove_usermention(tweets_list):
    '''
    ユーザーメンションを除去する処理
    '''

    lower_list = list(string.ascii_lowercase)
    upper_list = list(string.ascii_uppercase)
    alphabet_list = lower_list + upper_list
    alphabet_list.append('_')

    removed = []
    removed_list = []
    not_removed_list = []
    removed_list_complete = []

    for tweet in tweets_list:
        while re.search(r'@[0-9a-zA-Z_]+\s', tweet) is not None:
            an = re.search(r'@[0-9a-zA-Z_]+\s', tweet)
            start = an.span()[0]
            end = an.span()[1]
            tweet = str(tweet[:start]) + str(tweet[end:])
        removed.append(tweet)

    for tweet in removed:
        if tweet is not None:
            if tweet[0] == '@':
                for idx, st in enumerate(tweet[1:]):
                    if st not in alphabet_list:
                        removed_list.append(tweet[idx+1:])
                        break
            else:
                removed_list.append(tweet)
        else:
            removed_list.append(tweet)

    for tweet in removed_list:
        while re.search(r'@[0-9a-zA-Z_]{4,14}', tweet) is not None:
            an = re.search(r'@[0-9a-zA-Z_]{4,14}', tweet)
            start = an.span()[0]
            end = an.span()[1]
            tweet = str(tweet[:start]) + str(tweet[end:])
        removed_list_complete.append(tweet)

    return removed_list_complete


def remove_url(tweets_list):
    '''
    URLを除去する処理
    '''
    removed_list = []

    for tweet in tweets_list:
        while re.search(r'http', tweet) is not None:
            an = re.search(r'http', tweet)
            start = an.span()[0]
            tweet = str(tweet[:start])
        removed_list.append(tweet)

    return removed_list


def remove_hashtag(tweets_list):
    '''
    ハッシュタグのみを除去する処理
    '''
    removed_list = []
    removed_cnt = 0

    for tweet in tweets_list:
        if re.search(r'#', tweet) is not None:
            removed_cnt += 1
        while re.search(r'#', tweet) is not None:
            an = re.search(r'#', tweet)
            start = an.span()[0]
            end = an.span()[1]
            tweet = str(tweet[:start]) + str(tweet[end:])
        removed_list.append(tweet)
    return removed_list


def remove_hashtag_a_series_of_words(tweets_list):

    removed_list = []

    for tweet in tweets_list:
        while re.search(r'#[0-9a-zA-Z_]+\s', tweet) is not None:
            an = re.search(r'#[0-9a-zA-Z_]+\s', tweet)
            start = an.span()[0]
            end = an.span()[1]
            tweet = str(tweet[:start]) + str(tweet[end:])
        removed_list.append(tweet)

    return removed_list

def remove_w(tweets_list):
    
    '''
    wを除去する処理
    '''
    
    w_list = []
    
    for tweet in tweets_list:
        twee = []
        contexts = tweet.strip()
        for context in contexts:
            while context[-1] == 'w':
                    twee += context[:-1]
        w_list.append(twee)
        
    return w_list
        
        
#     for tweet in tweets_list:
#         if re.search(r'ww+', tweet) is not None:
#             if tweet[-1] != 'w':
#                 w_list.append(tweet)

#     w_list = list(set(w_list))

#     return w_list


