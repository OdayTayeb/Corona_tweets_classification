# Corona_tweets_classification

The project aims to classify arabic tweets (from Twitter) that are related to Corona Vaccine to: with vaccine - against vaccine - neutral.

# Project Files

Train - Test - Valid: The dataset.

preprocessing: where the text analysis, cleaning and normalization is done.

training model: where a machine learning model is trained and tuned.

# details

## preprocessing: 

in this phase we do some text analysis to the dataset like number of tweets per class, n-gram with highest and lowest frequency in dataset, trending hashtags in the dataset etc ...

then we implement some functions to clean the dataset like: Delete mentions URLs punctuation emojis and stopwords, delete not arabic words, delete repetitive words, stemming, Lemmatization etc...

## training model:

here we built a baseline model (Logistic Regression) and trained it on Bag of words features.

Then we tried to apply ONE preprocessing method only with the same model and with Bag of words features.

Then we build a final model (Logistic Regression) with all the preprocessing methods that improved the baseline performance and with tfidf features.

we tried to train a (SVM model) and a (deep learning model) with all the preprocessing methods that improved the baseline performance and with tfidf features.

## Results

![لقطة الشاشة 2022-09-17 220420](https://user-images.githubusercontent.com/92798033/190872644-31e85b66-f939-480f-b5a4-6c1ce4ceef60.png)

