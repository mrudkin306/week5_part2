#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[18]:


table = pd.read_excel("C:/Users/mcrud/Documents/GIS 6345/Week 5/daycare_dogs.xlsx", "Sheet1")


# In[19]:


table.head(5)


# In[21]:


table.plot.bar(x = 'Name', y = "Age")


# In[ ]:




