#!/usr/bin/env python
# coding: utf-8

# ### Home assignment 01.
# 
# Your goal is to follow this notebook and complete all the steps.
# 
# Please, solve all these excersises (both on python and bash) _using the remote machine_: either in jupyter notebook or using bash.
# 
# We ask you to start with signing this notebook in the following cell and printing some tech information. Please, just run the second cell without any changes.
# 
# Good luck!

# In[9]:


first_name = 'Victor'
last_name = 'Reeves'


# In[10]:


import sys
print(sys.path)
print(sys.version)


# #### Excersise 0
# Import `this` and read the zen of Python.

# In[11]:


import this


# In[12]:


student_has_read_zen_of_python = True
assert student_has_read_zen_of_python


# #### Excersise 1
# 
# Read the docs on `isinstance` method and check whether the following objects belong to the proposed types (hint: `isinstance`).
# 
# Additional excersise: visualize this correspondance matrix (object – type), e.g. using numpy and [pcolormesh](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pcolormesh.html) for visualization.

# In[24]:


list_of_objects = [
    int,
    2,
    2.,
    None,
    object,
    str,
    str(2.),
    float('2.0'),
    'hello',
    this,
    dict,
    list,
    [dict],
    {1: []}
]

list_of_types = [
    int,
    float,
    object,
    str,
    #module,
    dict,
    list
]


# In[23]:


y = tuple(list_of_types)
for i in list_of_objects:
    x = isinstance(i, y)
    print(x)


# #### Excersise 2
# 
# Set quotient and remainder of 89 divided by 11 to "a" and "b" variables *

# In[29]:


a, b = divmod(89, 11)
print(a, b)


# #### Excersise 3
# 
# Calculate the next cells:
# ```
# 0) 10 ** 1000
# 1) 1.0 / 10 ** 1000
# 2) 1 / 10 ** 1000
# 3) 10 ** 1000 / 1
# 4) 1 / (1 / 10 ** 1000)
# ```

# In[79]:


from __future__ import division
from decimal import Decimal


a0 = 10 ** 1000
a1 = Decimal(1) / 10 ** 1000
a2 = Decimal(1) / 10 ** 1000
a3 = Decimal(10) ** 1000 / 1
a4 = 1 / (Decimal(1) / 10 ** 1000)



# How to avoid these behaviours to receive correct results in steps 1-4?
# 
# It is enough to provide your thoughts / seach the web for decisions and share the links / point to specific constructions in Python which were constructed to solve this problem.

# these errors are causwd by not handling the types properly using decimal will solve all of these issues although there are many other fixes

# #### Excersise 4.1
# 
# Check if string is a correct integer
# 

# In[ ]:


a = "5"
a.isnumeric()


# #### Excersise 4.2
# 
# Create a palindrom from given string. For example, "abc" -> "abcba"

# In[101]:


s = input()
x = list(s)
a = x[::-1]
b = x[0:-1]

print(b + a)


# #### Excersise 4.3
# 
# User inputs one's name into "name" variable. One can use `lowercase`, `UPPERCASE`, or `sOmeTHingLikeThatCaSE`. You need to turn this string into regular case used with names: `Firstletterisbigothersaresmall`.

# In[100]:


name1 = 'HellOIamUsER'
name2 = 'johndeere'
name3 = 'FIRSTNAMELASTNAME'

lst1 = [name1, name2, name3]

for i in lst1:
    i = i[0].upper() + i[1:].lower()
    print(i)
    
# YOUR CODE HERE


# #### Excersise 4.4
# 
# You have a string that consists of English letters and ".", ",", "-", "!", "?", ":", ";" symbols. Extract all words without punctuation from this string.

# In[97]:


s = input()
print(''.join((c if c.isalnum() else ' ') for c in s).split())


# #### Excersise 4.5
# 
# Assign string `"""'''\/'''"""` to Python variable (all 14 symbols)
# 

# In[96]:


a = ''' \"\"\"\'\'\'\\/\'\'\'\"\"\" '''
print(a)


# #### Excersise 4.6
# 
# Print pi number in a string  "pi is approximately equal to ALMOSTPI", where instead of ALMOSTPI you insert 22/7 with 3 digits after comma.

# In[95]:


x = 22/7
a = "pi is approximately equal to ALMOSTPI"
print(format(x,".3f"))


# #### Excersise 5
# 
# You have multiline text inside string variable named `text`. Create list of lines from that text.

# In[92]:


x = text.splitlines()
print(x)


# #### Excersise 5
# Answer with your own words to one of the following questions. Your variant is based on your name and computed automatically in the next cell.
# 
# Variant 1:
# Imagine, you are developing a vending machine. You need to keep your vending machine state: which items are presented on which shelves, how much money inside machine to give change, how much money user inserted in current time, which purchases users made etc. You need to create a data structure for that using known data types.
# 
# Variant 2:
# Imagine, you are developing a messenger with direct messages, groups, different media types of messages, etc. You need to keep your messenger state in memory: all users with their data, which chats they have, etc. You need to create a data structure for that using known data types.
# 
# Variant 3:
# Imagine, you are developing a staff management system for a mid-size corporation. You need to keep all organizational structure in memory: departments, employees, their personal data, positions, salaries, history of growth, who is whose boss, etc. You need to create a data structure for that using known data types.

# In[103]:


variant = hash(' '.join(["Victor", "Reeves"])) % 3 + 1
print(f'Your variant is {variant}')


# _Your answer here_

# I would use Dictionaries and lists  to keep and use the relevant information

# #### Excersise 6
# 
# Clear your current repository (remove all useless files).
# Then create a package named `assignment01`.
# 
# In the `assignment01` package you should have two `.py` files:
# 
# ```
# get_date.py
# get_time.py
# ```
# File `get_date.py` contains only function `ding()` which returns the current date in format `yyyy-mm-dd`
# 
# File `get_date.py` contains only function `dong()` which  returns the current time in 24h format `hh:mm:ss`
# 
# Import these files and call the functions in the next cell.

# In[109]:


from get_date.py import *

ding()


# #### Excersise 7
# 
# Create the `.gitignore` file in the current repository and enshure git will ignore jupyter notebook checkpoints (hint: check the hidden directories) and python cache.

# _Here you should interact with the command prompt_

# #### Excersise 8
# Create folder `shell_tools` in your repository.
# 
# Solve the excersises from [this lesson](https://missing.csail.mit.edu/2020/shell-tools/) from the brilliant course by MIT: https://missing.csail.mit.edu
# 
# Place your solutions in the `shell_tools` directory. It should contain one file for each step except step 2 (named `step0*`) with bash commands. Step 2 already requires you to write `marco` and `polo` scripts).

# _Here you should interact with the command prompt_

# #### Excersise 9
# 
# Move this notebook to the repository directory (unless it is already there), commit and push all updates to the remote. Thes sync it to the local machine and check that this exact notebook runs (Kernel –> Restart and run all) without any changes.

# In[ ]:


notebook_runs_on_local_machine_without_any_changes = # True or False
assert notebook_runs_on_local_machine_without_any_changes


# ### Sumbitting your home assignment
# Push your results to the remote repository and share the link to it in the Google Classroom.
# 
# Congratulations!
