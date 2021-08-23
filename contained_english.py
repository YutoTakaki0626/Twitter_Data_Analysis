import string
import re

def count_the_number_of_mixed_tweet(tweets_list):

    lower_list = list(string.ascii_lowercase)
    upper_list = list(string.ascii_uppercase)
    alphabet_list = lower_list + upper_list

    contained_cnt = 0
    contained_list = []

    for tweet in tweets_list:
        for alphabet in alphabet_list:
            if re.search(r'{}'.format(alphabet), tweet) is not None:
                    contained_cnt += 1
                    contained_list.append(tweet)
                    break

    return contained_cnt, contained_list
