#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
from wordcloud import WordCloud
from PIL import Image
import matplotlib.pyplot as plt
import re


# In[ ]:


f = open('genres_improved.txt', 'r')


# In[ ]:


artists = f.read()


# In[ ]:


artists


# In[ ]:


artists = artists.split('\n')


# In[ ]:


artists


# In[ ]:


genres = []
for artist in artists:
    genre = artist[artist.find("[")+1:artist.find("]")]
    genres.append(genre)
genres


# I like the result of the first for loop more.
# second_list =[]
# for artist in artists:
#     genre = re.findall(r'\[.*?\]', artist)
#     second_list.append(genre)
# second_list


# In[ ]:


len(genres)


# In[ ]:


i = 0

for genre in enumerate(genres):
    if genres[i] == '':
        genres[i] = 'hip hop'
        i += 1
    else:
        i += 1


# In[ ]:


genres


# In[ ]:


len(genres)


# In[ ]:


def remove_punct(text):
    text = re.sub('[\W_]+', ' ', text)
    return text


# In[ ]:


type(genres)


# In[ ]:


genre_1 = genres[0]


# In[ ]:


genre_1


# In[ ]:


g1_np = remove_punct(genre_1)


# In[ ]:


g1_np


# ^^^that's exactly what I want for each line. Now how to interate over each line and do that.

# In[ ]:


genres_np = []

for genre in genres:
    if 'r&b' in genre:
        genre = genre.replace('r&b', 'rb')
    if 'lo-fi' in genre:    
        genre = genre.replace('lo-fi', 'lofi')
    g_np = remove_punct(genre)
    g_np = g_np.strip()
    genres_np.append(g_np)
    
genres_np


# In[ ]:


big_genres = []

for genre in genres_np:
    genres_list = genre.split(' ')
    big_genres.append(genres_list)
    
big_genres


# In[ ]:


genres_set = []

for genres in big_genres:
    genres_list = set(genres)
    genres_set.append(genres_list)
    
genres_set


# In[ ]:


type(genres_set)


# In[ ]:


type(genres_set[0])


# In[ ]:


type(list(genres_set[0]))


# In[ ]:


all_genres = []

for genre in genres_set:
    all_genres.append(list(genre))

all_genres


# In[ ]:


type(all_genres[0])


# In[ ]:


genres_onemore = [' '.join(genre) for genre in all_genres]

genres_onemore


# In[ ]:


genres_final = ' '.join(genres_onemore)


# In[ ]:


genres_final


# In[ ]:


genres_final = genres_final.replace('rb', 'r&b')


# In[ ]:


genre_dict = {}
for word in genres_final.split(' '):
    if word not in genre_dict:
        genre_dict[word] = 1
    else:
        genre_dict[word] += 1
        
genre_dict


# In[ ]:


dict_keys = []

for key in genre_dict:
    if key not in dict_keys:
        dict_keys.append(key)
    
dict_keys


# In[ ]:


len(dict_keys) == len(set(dict_keys))


# Now we can start with the wordcloud.

# In[ ]:


mask = np.array(Image.open('logo.jpeg'))


# In[ ]:


wordcloud = WordCloud(width = 1600, height = 1600, 
                      background_color = 'black', 
  min_font_size = 1, colormap="turbo").generate_from_frequencies(genre_dict)


# In[ ]:


plt.figure(figsize = (200, 100), facecolor = 'k')
plt.imshow(wordcloud)
plt.axis('off')
plt.tight_layout(pad = 0)

plt.show()


# In[ ]:




