import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st


st.title("olympics Data Analysis")
st.markdown("### Athletes Analysis :")

olympics = pd.read_csv('sources/olympics_1.csv')

st.info('#### Can you find Top 10 of  athletes with the __highest__ medals of all time in olympics(winter & summer)?')
con1 = st.container()
col1, col2 = con1.columns(2)

the_highset_olympics = olympics.groupby('Athlete')[['Medal']].count().sort_values(by='Medal', ascending=False).head(10)

col1.markdown('#### Top 10 of athletes')
col1.write(the_highset_olympics)
col2.plotly_chart(px.bar(the_highset_olympics, x=the_highset_olympics.index, y='Medal', title='The highest medalists'))

############################################################################################################


st.warning('###  Top __10__ __male__ athlete of olympics(winter & summer) ?')
con2 = st.container()
col1, col2 = con2.columns(2)

the_highest_male_olympics =olympics[olympics['Gender'] == 'Men']['Athlete'].value_counts().head(10)

col1.markdown('#### Top 10 male athlete')
col1.write(the_highest_male_olympics)
col2.plotly_chart(px.bar(the_highest_male_olympics, x=the_highest_male_olympics.index, y='Athlete', title='The highest medalists'))

############################################################################################################


st.error('###  TOP 10  female athlete of all olympics(winter & summer)?')
con3 = st.container()
col1, col2 = con3.columns(2)

the_highest_Female_olympics =olympics[olympics['Gender'] == 'Women']['Athlete'].value_counts().head(10)

col1.markdown('#### TOP 10  female athlete')
col1.write(the_highest_Female_olympics)
col2.plotly_chart(px.bar(the_highest_Female_olympics, x=the_highest_Female_olympics.index, y='Athlete', title='The highest medalists'))


