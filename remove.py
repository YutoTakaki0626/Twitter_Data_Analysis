import re
import string

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
        
    return new_list


def remove_usermention(tweets_list):
    '''
    ユーザーメンションを除去する処理
    '''
    removed_list = []

    for tweet in tweets_list:
        while re.search(r'@[0-9a-zA-Z_]+\s', tweet) is not None:
            an = re.search(r'@[0-9a-zA-Z_]+\s', tweet)
            start = an.span()[0]
            end = an.span()[1]
            tweet = str(tweet[:start]) + str(tweet[end:])
        removed_list.append(tweet)

    return removed_list


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

def remove_hashtag_words(tweets_list):
    '''
    ハッシュタグのみを除去する処理
    '''
    removed_list = []

    for tweet in tweets_list:
        while re.search(r'#[0-9a-zA-Z_]+\s', tweet) is not None:
            an = re.search(r'#[0-9a-zA-Z_]+\s', tweet)
            start = an.span()[0]
            end = an.span()[1]
            tweet = str(tweet[:start]) + str(tweet[end:])
        removed_list.append(tweet)

    return removed_list



