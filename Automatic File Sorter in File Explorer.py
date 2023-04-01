#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os, shutil


# In[22]:


path = r"/Users/trucb/Documents/DataAnalytist/Python/PythonProjects/FileSorter/"


# In[23]:


file_names = os.listdir(path)
print(file_names)


# In[15]:


folder_names = ["csv_files", "images_files", "text_files"]
folder_length = len(folder_names)


# In[24]:


folder_names = ["csv_files", "images_files", "text_files"]
for i in range(0, folder_length):
    if not os.path.exists(path + folder_names[i]):
        os.makedirs(path + folder_names[i])


# In[26]:


for file in file_names:
    if ".csv" in file and not os.path.exists(path + "csv_files/" + file):
        shutil.move(path + file, path + "csv_files/" + file)
    elif ".jpg" in file and not os.path.exists(path + "images_files/" + file):
        shutil.move(path + file, path + "images_files/" + file)
    elif ".txt" in file and not os.path.exists(path + "text_files/" + file):
        shutil.move(path + file, path + "text_files/" + file)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




