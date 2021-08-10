import string
import re

def count_the_number_of_mixed_tweet(tweets_list):

    lower_list = list(string.ascii_lowercase)
    upper_list = list(string.ascii_uppercase)
    alphabet_list = lower_list + upper_list

    contained_cnt = 0
    contained_list = []

    for tweet in tweets_list:
        splited_list = tweet.split(None)
        for split in splited_list:
            if split[0] == '@':
                continue
            if re.search(r'http', split) is not None:
                continue
            if re.search(r'#', split) is not None:
                continue
            for alphabet in alphabet_list:
                if re.search(r'{}'.format(alphabet), split) is not None:
                    contained_cnt += 1
                    contained_list.append(tweet)
                    break
            break
            
    return contained_cnt

def tweets_the_number_of_mixed_tweet(tweets_list):

    lower_list = list(string.ascii_lowercase)
    upper_list = list(string.ascii_uppercase)
    alphabet_list = lower_list + upper_list

    contained_cnt = 0
    contained_list = []

    for tweet in tweets_list:
        splited_list = tweet.split(None)
        for split in splited_list:
            if split[0] == '@':
                continue
            if re.search(r'http', split) is not None:
                continue
            if re.search(r'#', split) is not None:
                continue
            for alphabet in alphabet_list:
                if re.search(r'{}'.format(alphabet), split) is not None:
                    contained_cnt += 1
                    contained_list.append(tweet)
                    break
            break
            
    return contained_list