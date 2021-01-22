#!/usr/bin/env python
# coding: utf-8

# In[1]:


# In[3]:


import streamlit as st


# In[4]:


import pandas_datareader as pdr
from cryptocmd import CmcScraper
import plotly.express as px

# In[6]:

st.write('# 비트코인 BTC 데이터')

st.write('''
# 삼성전자 주식 데이터
마감 가격과 거래량을 차트로 보여줍니다~~~
''')


scraper = CmcScraper('BTC', '01-01-2021', '07-01-2021')

df = scraper.get_dataframe()

fig_close = px.line(df, x='Date', y=['Open','High','Low','Close'],title='가격')
fig_volume = px.line(df, x='Date', y=['Volume'], title='거래량')

st.plotly_chart(fig_close)
st.plotly_chart(fig_volume)


# In[ ]:




