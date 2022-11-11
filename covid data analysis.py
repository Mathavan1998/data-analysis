#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seabornas as sns
import plotly.express as px
from plotly.subplots import make_subplots
from detetime import datetime


# In[3]:


import pandas as pd
covid_df=pd.read_csv("D:/New folder/archive/covid india/covid_19_india.csv")


# In[4]:


covid_df.head(10)


# In[5]:


covid_df.info()


# In[6]:


covid_df.describe()


# In[7]:


vaccine_df=pd.read_csv("D:/New folder/archive/covid india/covid_vaccine_statewise.csv")


# In[9]:


vaccine_df.head(7)


# In[29]:


covid_df.drop(["Sno", "Time", "ConfirmedIndianNational", "ConfirmedForeignNational"],inplace=True,axis=1)


# In[28]:


covid_df.head


# In[15]:


covid_df['Date']=pd.to_datetime(covid_df['Date'],format='%Y-%m-%d')


# In[16]:


covid_df.head()


# In[17]:


#active cases
covid_df['Active_Cases']=covid_df['Confirmed']-(covid_df['Cured']+covid_df['Deaths'])
covid_df.tail()


# In[19]:


statewise=pd.pivot_table(covid_df,values=['Confirmed','Deaths','Cured'],index="State/UnionTerritory",aggfunc=max)


# In[20]:


statewise["Recovery Rate"]=statewise["Cured"]*100/statewise["Confirmed"]


# In[21]:


statewise["Mortality Rate"]=statewise["Deaths"]*100/statewise["Confirmed"]


# In[22]:


stateeise= statewise.sort_values(by = "Confirmed",ascending=False)


# In[24]:


statewise.style.background_gradient(cmap = "cubehelix")


# In[26]:


top_10_active_cases=covid_df.groupby(by='State/UnionTerritory').max()[['Active_Cases','Date']].sort_values(by=['Active_Cases'],ascending=False).reset_index()


# In[31]:


import matplotlib.pyplot as plt
fig=plt.figure(figsize=(16,9))


# In[32]:


plt.title("Top 10 states with most active cases in india",size=25)


# In[37]:


import seaborn as sns
ax=sns.barplot(data=top_10_active_cases.iloc[:10],y='Active_Cases',x="State/UnionTerritory",linewidth=2,edgecolor='red')


# In[39]:


top_10_active_cases=covid_df.groupby(by='State/UnionTerritory').max()[['Active_Cases','Date']].sort_values(by=['Active_Cases'],ascending=False).reset_index()
fig=plt.figure(figsize=(16,9))
plt.title("Top 10 states with most active cases in india",size=25)
ax=sns.barplot(data=top_10_active_cases.iloc[:10],y='Active_Cases',x="State/UnionTerritory",linewidth=2,edgecolor='red')
plt.xlabel('States')
plt.ylabel('Total Active Cases')
plt.show()


# In[5]:


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px
covid_df=pd.read_csv("D:/New folder/archive/covid india/covid_19_india.csv")
top_10_deaths=covid_df.groupby(by='State/UnionTerritory').max()[['Deaths','Date']].sort_values(by=['Deaths'],ascending=False).reset_index()
fig=plt.figure(figsize=(18,5))
plt.title('Top 10 states with most Deaths',size=25)
ax=sns.barplot(data=top_10_deaths.iloc[:12],y='Deaths',x='State/UnionTerritory',linewidth=2,edgecolor='black')
plt.xlabel('States')
plt.ylabel('Total Deaths Cases')
plt.show()


# In[ ]:





# In[ ]:




