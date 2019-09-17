#!/usr/bin/env python
# coding: utf-8

# In[1]:


import datetime
date = input()
k = 0
for i in date:
  if i =='/':
    k+=1
if k>0:
  date = date.split('/')
else:
  date = date.split('.')
for i in range(len(date)):
  date[i]=int(date[i])
if date[2] < 100:
  if date[2] > 18:
    date[2] +=1900
  else:
    date[2] += 2000
if date[2] <1000:
  if date[2]> 100:
    date[2]+=1000
year = date[2]
month = date[1]
day = date[0]
d = datetime.date(year,month,day)
a = d.weekday()
if a == 0:
  print('Понедельник')
if a == 1:
  print('Вторник')
if a == 2:
  print('Среда')
if a == 3:
  print('Четверг')
if a == 4:
  print('Пятница')
if a == 5:
  print('Суббота')
if a == 6:
  print('Воскресенье')


# In[ ]:




