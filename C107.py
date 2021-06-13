import pandas as pd
import csv
import plotly.graph_objects as go

df=pd.read_csv('data12345.csv')
print(df.groupby('level')['attempt'].mean())
studentDf=df.loc[df['student_id']=='TRL_xyz']

fig2=go.Figure(
go.Bar(
x=studentDf.groupby('level')['attempt'].mean(),y=['Level 1','Level 2','Level 3','Level 4'],orientation='h'
    )
    )
fig2.show()
