#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install requests


# In[2]:


pip install html5lib


# In[3]:


pip install bs4


# In[4]:


import csv
from csv import writer
import requests
from bs4 import BeautifulSoup
url = "https://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=78&Tx_State=MH&Tx_District=14&Tx_Market=2495&DateFrom=20-Oct-2021&DateTo=21-Oct-2021&Fr_Date=20-Oct-2021&To_Date=21-Oct-2021&Tx_Trend=0&Tx_CommodityHead=Tomato&Tx_StateHead=Maharashtra&Tx_DistrictHead=Pune&Tx_MarketHead=Pune(Khadiki)"


# In[5]:


#Step 1 : Get the Html
r = requests.get(url)
htmlcontent = r.content
print(htmlcontent)


# In[6]:


htmlText = r.text
print(htmlText)


# In[7]:


# Step 2 : Parse the html
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())


# In[8]:


#find the title
title = soup.title
print(title)
# print(type(soup))
# print(type(title))
# print(type(title.string))


# In[9]:


#find the table
print(soup.find_all('table'))


# In[10]:


#find the class  Name

print(soup.find('table')['class'])


# In[11]:


#find the element using class
table = soup.find('table', attrs={"class": "tableagmark_new"})
header = []
rows = []
for i, row in enumerate(table.find_all('tr')):
    if i == 0:
        header = [el.text.strip() for el in row.find_all('th')]
    else:
        rows.append([el.text.strip() for el in row.find_all('td')])

print(header)


# In[12]:


for row in rows:
    print(row)


# In[13]:


#write in csv file

# with open(r'E:\Power-BI-Tutorial-Files\scarping3.csv', 'w', encoding='UTF8') as f:
#     writer = csv.writer(f)

#     # write the header
#     writer.writerow(header)

#     # write the data
#     writer.writerow(rows)


# In[14]:


#find the anchor tags

anchors = soup.find_all('a')
all_links = set()
# Get all the links on the page:
for link in anchors:
    if(link.get('href') != '#'): 
        linkText = "https://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=78&Tx_State=MH&Tx_District=14&Tx_Market=2495&DateFrom=20-Oct-2021&DateTo=21-Oct-2021&Fr_Date=20-Oct-2021&To_Date=21-Oct-2021&Tx_Trend=0&Tx_CommodityHead=Tomato&Tx_StateHead=Maharashtra&Tx_DistrictHead=Pune&Tx_MarketHead=Pune(Khadiki)" +link.get('href')
        all_links.add(link)
        print(linkText)


# In[ ]:




