
# coding: utf-8

# In[ ]:


#Loading a txt converted file of original dataset
dataSet = open("originalDataset.txt", "r")

#Used All the dirty words from Google's "what do you love" project - https://gist.github.com/jamiew/1112488
with open('badWords.txt') as f:
    word_list = f.read().splitlines() 
words = set(word_list)
for line in dataSet:
    if words & set(line.split()):
        #printing all the sentences that contains the swear words.
        print line,

