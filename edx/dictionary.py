#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 17:58:57 2018

@author: praneeshkhanna
"""

''' 
Dictionary Lookup - Similar to indexing into a list
Looks up the key and returns the value of the key, if key isn't found returns an error.


Dictionary Operations 
New entry can be added in a dictionary
dict['New_key'] = value

'New_key' in dict would give true now.

delete an entry - del (dict['New_key'])

dict.keys() gives an iterable tuple with keys in the dictionary
dict.values() gives an iterable tuple with values in the dictionary

**** Important - Values and keys returned will not be ordered 


values
• any type (immutable and mutable)
• can be duplicates
• dictionary values can be lists, even other dictionaries!

keys
• must be unique
• immutabletype(int,float,string,tuple,bool)
• actually need an object that is hashable, but think of as immutable as all
immutable types are hashable
• careful with float type as a key

no order to keys or values!
'''


animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}
animals['d'] = 'donkey'
animals

# =============================================================================
# Creating and analyzing dictionaries
# =============================================================================

''' Three functions to analyze song lyrics 
    1) create a frequency dictionary mapping str:int
    2) find word that occurs the most and how many times
       use a list, in case there is more than one word
       return a tuple (list,int) for (words_list, highest_freq)
    3) find the words that occur at least X times
       let user choose “at least X times”, so allow as parameterS
       return a list of tuples, each tuple is a (list, int) containing 
       the list of words ordered by their frequency
       IDEA: From song dictionary, find most frequent word. Delete most 
       common word. Repeat. It works because you are mutating the song dictionary.
'''

def lyrics_to_frequencies(lyrics):
    my_dict = {}
    for word in lyrics :
        if word in my_dict:
            my_dict[word] = my_dict[word] + 1
        else:
            my_dict[word] = 1
    return my_dict   

   

def most_common_words(freqs):
    values = freqs.values()
    best = max(freqs.values())
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)

she_loves_you = ['she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',

'you', 'think', "you've", 'lost', 'your', 'love',
'well', 'i', 'saw', 'her', 'yesterday-yi-yay',
"it's", 'you', "she's", 'thinking', 'of',
'and', 'she', 'told', 'me', 'what', 'to', 'say-yi-yay',

'she', 'says', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'she', 'said', 'you', 'hurt', 'her', 'so',
'she', 'almost', 'lost', 'her', 'mind',
'and', 'now', 'she', 'says', 'she', 'knows',
"you're", 'not', 'the', 'hurting', 'kind',

'she', 'says', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',

'you', 'know', "it's", 'up', 'to', 'you',
'i', 'think', "it's", 'only', 'fair',
'pride', 'can', 'hurt', 'you', 'too',
'pologize', 'to', 'her',

'Because', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'Yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'yeah', 'yeah', 'yeah',
'yeah', 'yeah', 'yeah', 'yeah'
]


beatles = lyrics_to_frequencies(she_loves_you)
(w,b) = most_common_words(beatles)

# =============================================================================
# find the words that occur at least X times
# =============================================================================

 
def words_often(x, freqs):
   
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= x:
            result.append(temp)
            for w in temp[0]:
                del (freqs[w])
        else:
            done = True
    return result

words_often(beatles, 5)        
            































        
