import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st


st.title("olympics Data Analysis")
st.markdown("### Countries Analysis :")

olympics = pd.read_csv('sources/olympics_1.csv')

st.info('##### What are the __Top 10__ Countries by __total medals? (winter & summer)?')
con1 = st.container()
col1, col2 = con1.columns(2)

the_top_10_countries_olympics = olympics.groupby('Country')[['Medal']].count().sort_values(by='Medal', ascending=False).head(10)

col1.markdown('#### Top 10 of Countries')
col1.write(the_top_10_countries_olympics)
col2.plotly_chart(px.bar(the_top_10_countries_olympics, x=the_top_10_countries_olympics.index, y='Medal', title='the_top_10_countries_olympics'))

############################################################################################################


st.warning('#####  Calculate the Gold medals per each country and visualize the results ?')
con2 = st.container()
col1, col2 = con2.columns(2)

medlas_country_olympics_gold = pd.crosstab(olympics['Country'], olympics['Medal'])['Gold'].nlargest(10)

col1.markdown('#### The Gold medals')
col1.write(medlas_country_olympics_gold)
col2.plotly_chart(px.bar(medlas_country_olympics_gold, x=medlas_country_olympics_gold.index, y='Gold', title='medlas_country_olympics_gold'))

############################################################################################################


st.error('#####  Calculate the silver medals per each country and visualize the results ?')
con2 = st.container()
col1, col2 = con2.columns(2)

medlas_country_olympics_silver = pd.crosstab(olympics['Country'], olympics['Medal'])['Silver'].nlargest(10)

col1.markdown('#### The silver medals')
col1.write(medlas_country_olympics_silver)
col2.plotly_chart(px.bar(medlas_country_olympics_silver, x=medlas_country_olympics_silver.index, y='Silver', title='medlas_country_olympics_silver'))

############################################################################################################

st.info('#####  Calculate the Bronze medals per each country and visualize the results ?')
con1 = st.container()
col1, col2 = con1.columns(2)

medlas_country_olympics_Bronze	 = pd.crosstab(olympics['Country'], olympics['Medal'])['Bronze'].nlargest(10)

col1.markdown('#### The Bronze medals')
col1.write(medlas_country_olympics_Bronze)
col2.plotly_chart(px.bar(medlas_country_olympics_Bronze, x=medlas_country_olympics_Bronze.index, y='Bronze', title='medlas_country_olympics_Bronze'))

############################################################################################################


st.warning('#####  The most organized city for the Olympics with mentioning the number ?')
con2 = st.container()
col1, col2 = con2.columns(2)

the_number_of_organized_olympics = olympics[['City','Year']].drop_duplicates().groupby('City')[['Year']].count().sort_values(by='Year', ascending=False).head(10)

col1.markdown('#### The most organized city')
col1.write(the_number_of_organized_olympics)
col2.plotly_chart(px.bar(the_number_of_organized_olympics, x=the_number_of_organized_olympics.index, y='Year', title='the_number_of_organized_olympics'))



############################################################################################################


st.error('#####  The Top 10 organized countries in olympics ?')
con2 = st.container()
col1, col2 = con2.columns(2)

the_Top_10_organized_countries_olympics = olympics[['Country','Year']].drop_duplicates().groupby('Country')[['Year']].count().sort_values(by='Year', ascending=False).head(10)

col1.markdown('#### The Top 10 organized countries')
col1.write(the_Top_10_organized_countries_olympics)
col2.plotly_chart(px.bar(the_Top_10_organized_countries_olympics, x=the_Top_10_organized_countries_olympics.index, y='Year', title='the_Top_10_organized_countries_olympics'))

############################################################################################################


st.warning('#####  The sport that achieves the most medals in olympics ?')
con2 = st.container()
col1, col2 = con2.columns(2)

country_sport_olympics = olympics.groupby(['Sport'])[["Medal"]].count().sort_values(by='Medal', ascending=False).head(10)

col1.markdown('#### The sport that achieves')
col1.write(country_sport_olympics)
col2.plotly_chart(px.bar(country_sport_olympics, x=country_sport_olympics.index, y='Medal', title='country_sport_olympics'))






