from nltk import wordpunct_tokenize
from nltk.corpus import stopwords

def language_detector(string):

	tokens = wordpunct_tokenize(string)
	words = [word.lower() for word in tokens]

	# compute language scores
	languages_ratios = {}
	for language in stopwords.fileids():
		stopwords_set = set(stopwords.words(language))
		words_set = set(words)
		common_elements = words_set.intersection(stopwords_set)
		languages_ratios[language] = len(common_elements) # language "score"

	languages_ratios
	most_rated_language = max(languages_ratios, key=languages_ratios.get)
	return most_rated_language