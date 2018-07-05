'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!
polarity_list = []
subjectivity_list = []


for tweet in tweetData:
    tb = TextBlob(tweet['text'])
    polarity_list.append(tb.polarity)

for tweet in tweetData:
    tb = TextBlob(tweet['text'])
    subjectivity_list.append(tb.subjectivity)

polarityAvg = float(sum(polarity_list)/len(polarity_list))
subjectivityAvg= float(sum(subjectivity_list)/len(subjectivity_list))

plt.hist(polarity_list, bins=[-0.60,-0.45,-0.30,-0.15 ,0.0, 0.15, 0.30, 0.45,0.60, 1])
plt.xlabel('Polarity')
plt.ylabel('Number of Tweets')
plt.title('Histogram of Tweet Polarity')
plt.axis([-1.1, 1.1, 0, len(polarity_list)])
plt.grid(True)
plt.show()

plt.hist(subjectivity_list, bins=[0.0, 0.15, 0.30, 0.45,0.60, 1])
plt.xlabel('Subjectivity')
plt.ylabel('Number of Tweets')
plt.title('Histogram of Tweet Subjectivity')
plt.axis([-1.1, 1.1, 0, len(subjectivity_list)])
plt.grid(True)
plt.show()


largeTweetString = ''
filtered_words = {}
for tweet in tweetData:
    largeTweetString += (" " + tweet['text'])

tb2 = TextBlob(largeTweetString)

tweetSearch = "automation"
wordsToFilter = ["your","about", "https", "in", "the", "thing", "will", "could", tweetSearch]
for word in tb2.words:
    count = 0
    currentWord = word.lower()
    if currentWord.isalpha() == True:
        if len(currentWord) > 3 and currentWord not in wordsToFilter:
            for word2 in tb2.words:
                if currentWord == word2.lower():
                    count += 1
            filtered_words[currentWord] = int(count)

filtered_words_list = []
for key in filtered_words:
    temp = (key,filtered_words[key])
    filtered_words_list.append(temp)

wordcloud = WordCloud(background_color = 'white',max_font_size = 50).generate_from_frequencies(filtered_words_list)
wordcloud.recolor(True)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
