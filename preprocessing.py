#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import nltk
import string
get_ipython().system('pip install emoji')
from emoji import UNICODE_EMOJI
nltk.download('stopwords')
from nltk.corpus import stopwords
import unicodedata as ud
import re
from nltk.stem.isri import ISRIStemmer
import csv

from nltk.tokenize import TweetTokenizer
def Tokenize_tweet(tweet):
    # Input : tweet as a string
    # output : List of Tokens
    tokenizer = TweetTokenizer()
    return tokenizer.tokenize(tweet)

def remove_urls(tweet):
    #Input: List of tweet tokens
    #Output: cleaned_tweet: tweet after removing urls
    result = []
    for i in range(len(tweet)):
        if (tweet[i].startswith('http') is False):
            result.append(tweet[i])
    return result

def remove_mentions(tweet):
    #Input: List of tweet tokens
    #Output: cleaned_tweet: tweet after removing mentions
    result = []
    for i in range(len(tweet)):
        if (tweet[i].startswith('@') is False):
            result.append(tweet[i])
    return result

def delete_rep(tweet):
    #Input: List of tweet tokens
    #Output: cleaned_tweet: tweet after removing repetitive letters
    result = []
    for i in range(len(tweet)):
        x = tweet[i][0];
        for j in range(1,len(tweet[i])):
            if (tweet[i][j]==tweet[i][j-1]):
                continue
            x += tweet[i][j]
        result.append(x)
    return result

def unified(tweet):
    # input : tweet as a string
    # output : modified tweet as a string
    res = tweet.replace('كرونا','كورونا')
    result = res.replace('فيروس','فايروس')
    return result

def delete_unneeded_numbers(tweet):
    # input: tokens of tweet
    # output : tokens after deleting unneeded numbers
    pattern = '([0-9])+(\\.([0-9])+)?'
    pattern2 = '([٠-٩])+(\\.([٠-٩])+)?'
    result = []
    for i in range(len(tweet)):
        if re.fullmatch(pattern,tweet[i]) or re.fullmatch(pattern2,tweet[i]):
            if i+1<len(tweet) and tweet[i+1] == '%':
                result.append(tweet[i])
        else :
            result.append(tweet[i])
    return result

def delete_punctuation(tweet):
    # input : tokens of tweet
    # output: tokens without punctuation
    result = []
    for i in range(len(tweet)):
        if not(ud.category(tweet[i][0]).startswith('P')):
            result.append(tweet[i])
        else :
            if tweet[i]=='%' or tweet[i].startswith('#'):
                result.append(tweet[i])
    return result

def delete_punctuation(tweet):
    # input : tokens of tweet
    # output: tokens without punctuation
    result = []
    for i in range(len(tweet)):
        if not(ud.category(tweet[i][0]).startswith('P')):
            result.append(tweet[i])
        else :
            if tweet[i]=='%' or tweet[i].startswith('#'):
                result.append(tweet[i])
    return result

def delete_emojis(tweet):
    # input : tokens of tweet
    # output: tokens without emojis
    result = []
    for i in range(len(tweet)):
        if tweet[i] not in UNICODE_EMOJI['en']:
            result.append(tweet[i])
    return result

def delete_stopwords(tweet):
    # input : tokens of tweet
    # output: tokens without stopwords
    result = []
    stop_words = set(stopwords.words('arabic'))
    for i in range(len(tweet)):
        if tweet[i] not in stop_words:
            result.append(tweet[i])
    return result

def delete_not_arabic(tweet):
    pattern = r'[ا-ي]*'
    pattern2 = '([0-9])+(\\.([0-9])+)?'
    pattern3 = '([٠-٩])+(\\.([٠-٩])+)?'
    pattern4 = r'[ا-ي_]*'
    # input : tokens of tweet
    # output: tokens without non-arabic words 
    result = []
    for i in range(len(tweet)):
        if re.fullmatch(pattern,tweet[i]) or re.fullmatch(pattern2,tweet[i]) or re.fullmatch(pattern3,tweet[i]) or tweet[i]=='%':
            result.append(tweet[i])
        else :
            if tweet[i].startswith('#') and re.fullmatch(pattern4,tweet[i][1:]):
                result.append(tweet[i])
    return result

def stemming(tweet):
    # input : tokens of tweet
    # output: stemmed tokens 
    pattern = r'[ا-ي]*'
    result = []
    stemmer = ISRIStemmer();
    for i in range(len(tweet)):
        if re.fullmatch(pattern,tweet[i]):
            st = stemmer.stem(tweet[i])
            result.append(st)
        else :
            result.append(tweet[i])
    return result

def replace_char(string,index,c):
    l = list(string)
    l[index] = c
    return ''.join(l)

def unified_charachters(tweet):
    # input : tokens of tweet
    # output: tokens unified
    for i in range(len(tweet)):
        for j in range(len(tweet[i])):
            if tweet[i][j] == 'ى':
                tweet[i]=replace_char(tweet[i],j,'ي')
            if tweet[i][j] == 'أ' or tweet[i][j] == 'إ' or tweet[i][j] == 'آ':
                tweet[i]=replace_char(tweet[i],j,'ا')
            if tweet[i][j] == 'ؤ' or tweet[i][j] == 'ئ':
                tweet[i]=replace_char(tweet[i],j,'ء')
            if tweet[i][j] == 'ة':
                tweet[i]=replace_char(tweet[i],j,'ه')
    return tweet

def preprocess(tweet, flags=[1,1,1,1,1,1,1,1,1,1,1]):
    """
    Process tweet function.
    Input:
        tweet: a string containing a tweet
        flags: list of "work" values for all functions will called here.
    Output:
        cleaned_tweet: tweet after apply all cleaning and normlizaing functions
    """
    if flags[0] == 1:
        tweet = unified(tweet)
    tweet = Tokenize_tweet(tweet)

    if flags[1] == 1:
        tweet = remove_urls(tweet)
    if flags[2] == 1:
        tweet = remove_mentions(tweet)
    if flags[3] == 1:
        tweet = delete_rep(tweet)
    if flags[4] == 1:
        tweet = delete_unneeded_numbers(tweet)
    if flags[5] == 1:
        tweet = delete_punctuation(tweet)
    if flags[6] == 1:
        tweet = delete_emojis(tweet)
    if flags[7] == 1:
        tweet = delete_stopwords(tweet)
    if flags[8] == 1:
        tweet = stemming(tweet)
    if flags[9] == 1:
        tweet =unified_charachters(tweet)
    if (flags[10] == 1):
        tweet = delete_not_arabic(tweet)
    return ' '.join(tweet)
  


# In[ ]:




