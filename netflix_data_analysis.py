import numpy as np 
import pandas as pd 
import plotly.express as px 
from textblob import TextBlob 

df = pd.read_csv(r"C:\Users\ASHWANI\Desktop\Divyanshu.py\project 10\netflix_titles.csv")

print(df.columns)
x = df.groupby(['rating']).size().reset_index(name='counts')
print(x)

pieChart = px.pie(x, values='counts', names='rating', title='Distribution of content ratings on Netflix')
pieChart.show()

df['director']=df['director'].fillna('Director not specified')
df.head()

directors_list = pd.DataFrame()
print(directors_list)

directors_list = directors_list.to_frame()
print(directors_list)

directors_list = directors_list.to_frame()
print(directors_list)

directors = directors_list.groupby(['Director']).size().reset_index(name='Total Count')
print(directors)

directors = directors[directors.Director != 'Director not specified']

print(directors)

directors = directors.sort_values(by=['Total Count'], ascending = False)
print(directors)


top5Directors = directors.head()
print(top5Directors)
     
top5Directors = top5Directors.sort_values(by=['Total Count'])
barChart = px.bar(top5Directors, x='Total Count', y = 'Director', title = 'Top 5 Directors on Netflix')
barChart.show()

df1 = df[['type', 'release_year']]
df1 = df1.rename(columns = {"release_year":"Release Year", "type": "Type"})
df2 = df1.groupby(['Release Year', 'Type']).size().reset_index(name='Total Count')
     
print(df2)

df2 = df2[df2['Release Year']>=2000]
graph = px.line(df2, x = "Release Year", y="Total Count", color = "Type", title = "Trend of Content Produced on Netfilx Every Year")
graph.show()


df3 = df[['release_year', 'description']]
df3 = df3.rename(columns = {'release_year':'Release Year', 'description':'Description'})
for index, row in df3.iterrows():
  d=row['Description']
  testimonial = TextBlob(d)
  p = testimonial.sentiment.polarity
  if p==0:
    sent = 'Neutral'
  elif p>0:
    sent = 'Positive'
  else:
    sent = 'Negative'
  df3.loc[[index, 2], 'Sentiment']=sent

df3 = df3.groupby(['Release Year', 'Sentiment']).size().reset_index(name = 'Total Count')

df3 = df3[df3['Release Year']>2005]
barGraph = px.bar(df3, x="Release Year", y="Total Count", color = "Sentiment", title = "Sentiment Analysis of Content on Netflix")
barGraph.show()
     





