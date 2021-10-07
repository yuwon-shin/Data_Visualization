import plotly.graph_objs as go
import pandas as pd
import os

courseDf = pd.read_csv(os.path.join(os.path.dirname(__file__), os.pardir, 'data', 'courses.csv'))
df = courseDf[courseDf['Year']==2021]

grouped_Df = df.groupby(['Semester','Department']).count()
grouped_Df = grouped_Df.reset_index()
semesters = ['Spring', 'Fall']


bar1 = go.Bar(name='School of Computing', x=semesters, y=grouped_Df.loc[grouped_Df['Department']=='School of Computing']['Course'])
bar2 = go.Bar(name='General Required', x=semesters, y=grouped_Df.loc[grouped_Df['Department']=='General Required']['Course'])
bar3 = go.Bar(name='Electrical Engineering', x=semesters, y=grouped_Df.loc[grouped_Df['Department']=='Electrical Engineering']['Course'])
bar4 = go.Bar(name='Cyber Security', x=semesters, y=grouped_Df.loc[grouped_Df['Department']=='Cyber Security']['Course'])
bar5 = go.Bar(name='Computer Engineering', x=semesters, y=grouped_Df.loc[grouped_Df['Department']=='Computer Engineering']['Course'])
bar6 = go.Bar(name='Mech/BioMed Engineering', x=semesters, y=grouped_Df.loc[grouped_Df['Department']=='Mech/BioMed Engineering']['Course'])
fig=go.Figure(data=[bar1,bar2,bar3,bar4,bar5,bar6 ])
fig.update_layout(barmode='stack')
fig.show()