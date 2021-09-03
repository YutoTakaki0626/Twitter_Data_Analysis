import emoji

def get_all_emoji():
	'''
	すべての絵文字のリストを得る
	'''
	all_emojis = []
	emojis = emoji.UNICODE_EMOJI.values()
	emojis = list(emojis)
	for num in range(len(emojis)):
	    element_emojis=list(emojis[num].keys())
	    all_emojis += element_emojis

	return all_emojis

def detect_contained_emojis(tweets_list, all_emojis):
	'''
	絵文字を含んでいるリストを得る
	'''
	emojis_list = []
	for tweet in tweets_list:
		for string in tweet:
			if string in all_emojis:
				emojis_list.append(tweet)
				break

	return emojis_list

def removed_emojis(tweets_list, all_emojis):
	'''
	絵文字を除去する
	'''
	removed_list = []

	for tweet in tweets_list:
		tmp = []
		for idx, string in enumerate(tweet):
			if string in all_emojis:
				tmp.append(idx)
		new_tweet = ''
		tmp_in = 0
		for i in tmp:
			new_tweet = str(new_tweet) + str(tweet[tmp_in:i])
			tmp_in = i+1
		new_tweet = str(new_tweet) + str(tweet[tmp_in:])
		removed_list.append(new_tweet)

	return removed_list


