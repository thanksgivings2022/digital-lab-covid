from dash import Input, Output, callback, dcc

import plotly.express as px

from plots import *



import preprocess.load_data1 as data
import preprocess.load_data2 as data2
import preprocess.transform_datas as data_joined




df = data.raw_df.copy()
df2 = data2.raw_df2.copy()
df_joined = data_joined.df1_df2_joined.copy()



@callback(
    Output('page-1-display-value', 'children'),
    Input('page-1-dropdown', 'value'),
    Input('page-1-date-picker-single','date'))
def display_value(value,date_value):
    print('Filters set :',value,date_value)
    fig = plot_per_country(df,value)
    return dcc.Graph(figure=fig)

@callback(
    Output('page-1-display-map', 'children'),
    Input('page-1-date-picker-single','date'),
    Input('strig-death-switch', 'on'))
def display_value(date_value,on):
    fig = plot_total_deaths_per_date(df,date_value,display=on)
    return dcc.Graph(figure=fig)

@callback(
    Output('page-1-display-death-stringency', 'children'),
    Input('page-1-dropdown', 'value'))
def display_value(value):
    if value :
        fig = plot_deaths_cases_stringency(df,value[-1])
    else :
        fig = plot_deaths_cases_stringency(df,"")
    return dcc.Graph(figure=fig)


@callback(
    Output('page-2-display-value', 'children'),
    Input('page-2-dropdown', 'value'))
def display_value(value):
    return f'You have selected {value}'
