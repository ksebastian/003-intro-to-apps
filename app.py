######### import libraries 

import dash
from dash import html
from dash import dcc
import plotly.graph_objs as go

########### Define your variables
sports=['Soccer', 'Cricket', 'Basketball', 'Golf', 'Tennis', 'Volleyball', 'Baseball', 'Football']
total_fans=[3.5, 2.5, 2.4, 0.4, 1.0, 0.9, 0.5, 0.41]
highest_salary=[1.22, .34, 1.25, .7, .85, 1.25, .49, .73]
color2='green'
color1='midnightblue'
mytitle='Worldwide Sports Comparison'

label1='Fans Billion'
label2='Salary 100M'

########### Set up the chart

def make_that_cool_barchart(sports, total_fans, highest_salary, color1, color2, mytitle):
    fans_billions = go.Bar(
        x=sports,
        y=total_fans,
        name=label1,
        marker={'color':color1}
    )
    salary_millions = go.Bar(
        x=sports,
        y=highest_salary,
        name=label2,
        marker={'color':color2}
    )

    sports_data = [fans_billions, salary_millions]
    sports_layout = go.Layout(
        barmode='group',
        title = mytitle
    )

    sports_fig = go.Figure(data=sports_data, layout=sports_layout)
    return sports_fig


######### Run the function #######

if __name__ == '__main__':
    fig = make_that_cool_barchart(sports, total_fans, highest_salary, color1, color2, mytitle)
    fig.write_html('docs/barchart_mine.html')
    print('We successfully updated the barchart!')
