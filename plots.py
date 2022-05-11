import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd


def filter_country(df, pays):  # list de pays
    return df[df.location.isin(pays)]


def filter_date_range(df, start_date, end_date, label='date'):
    mask = (df[label] >= start_date) & (df[label] <= end_date)
    return df[mask]


def plot_total_deaths_per_date(df,date_value, display):  ## map https://plotly.com/python/reference/choropleth/
    if display:
        title = 'World Stringency during Covid pandemic'
        column = 'stringency_index'
        colors=["#4c6a9c", "#4c6a9c", "#e48573"]
    else:
        title = 'Total Death during Covid pandemic'
        column = 'death_per_hab'
        colors=["#4c6a9c", "#e48573", "#e48573"]
    death_per_hab = filter_date_range(df[['iso_code', 'location', 'total_deaths', 'population', 'date', 'stringency_index']],date_value,'2020-10-10')
    death_per_hab['death_per_hab'] = death_per_hab['total_deaths'] / death_per_hab['population']
    death_per_hab['total_deaths'] = death_per_hab['total_deaths'].fillna(0)

    fig = px.choropleth(
        death_per_hab[['iso_code', 'location', 'death_per_hab', 'total_deaths', 'date', 'stringency_index']],
        locations='iso_code',
        hover_name='location',
        hover_data=['total_deaths'],
        color=column,
        color_continuous_scale=colors,
        title=title)
    fig.update_layout(margin={"r":0,"l":0,"b":0})

    return fig




def plot_per_country(df, value):
    showlegend = bool(len(value) < 10)
    legend = dict(traceorder="reversed",bgcolor="rgba(0,0,0,0)")
    return px.scatter(filter_country(df, value), x='total_cases', y='total_deaths',hover_data=['date'],
            title='Deaths & Cases', color='location')\
        .update_traces(showlegend=showlegend)\
        .update_layout(legend=legend,margin={"r":0,"l":0})\
        .update_traces(marker=dict(size=3))##

def plot_deaths_cases_stringency(df,country):
  fig = make_subplots(specs=[[{"secondary_y": True}]])
  fig.add_trace(
      go.Scatter(x=filter_country(df,[country]).date, y=filter_country(df,[country]).total_cases.diff().fillna(0), mode='lines+markers', name='Positive case'),
      secondary_y=False)
  fig.add_trace(
      go.Scatter(x=filter_country(df,[country]).date, y=filter_country(df,[country]).total_deaths.diff().fillna(0), mode='lines+markers', name='Deaths'),
      secondary_y=False)
  fig.add_trace(
      go.Scatter(x=filter_country(df,[country]).date, y=filter_country(df,[country]).stringency_index.fillna(0), mode='lines+markers', name='Stringency Index'),
      secondary_y=True)
  fig.update_layout(
      legend=dict(traceorder="reversed", x=0, y=1,bgcolor="rgba(0,0,0,0)"),
      title_text="{} : daily values.".format(country),
      title_x=0.5)
  fig.update_xaxes(title_text="Date")
  fig.update_yaxes(title_text="Positive cases & Deaths", secondary_y=False, color='black')
  fig.update_yaxes(title_text="Stringency_index", secondary_y=True, color= 'limegreen')
  fig.update_traces(marker=dict(size=3))##
  return fig



def plot_USA_GDP_deaths_cases(df_joined):
  df_USA=df_joined
  country='United States'
  fig = make_subplots(specs=[[{"secondary_y": True}]])
  fig.add_trace(
    go.Scatter(x=df_USA['date'], y=df_USA['GDP'], mode='lines+markers', name='GDP'),
    secondary_y=True,
  )
  fig.add_trace(
      go.Scatter(x=pd.to_datetime(df_USA['date']), y=df_USA['total_cases'], mode='lines+markers', name='total cases'),
      secondary_y=False,
  )
  fig.add_trace(
      go.Scatter(x=pd.to_datetime(df_USA['date']), y=df_USA['total_deaths'], mode='lines+markers', name='total deaths'),
      secondary_y=False,
  )
  fig.update_layout(
      legend=dict(traceorder="reversed", x=0, y=1,bgcolor="rgba(0,0,0,0)"),
      title_text="{} (per day values)".format(country),
      title_x=0.5
  )
  # Set x-axis title
  fig.update_xaxes(title_text="Date")
  # Set y-axes titles
  fig.update_yaxes(title_text="Positive cases & Deaths", secondary_y=False, color='black')
  fig.update_yaxes(title_text="GDP", secondary_y=True, color= 'blue')
  fig.update_traces(marker=dict(size=3))##
  return fig


# Na: model output .csv
def plot_prediction(index, y_test, y_pred):   
    fig_model = go.Figure()
    fig_model.add_trace(go.Scatter(x=index, y=y_test, mode='markers+lines', name='Real')) # ? x-axis = date doesn't work?
    fig_model.add_trace(go.Scatter(x=index, y=y_pred, mode='markers+lines', name='Predicted'))
    fig_model.update_layout(
        title_text="Prediction of CAC40 daily high with a Random Forest Regressor",
        title_x=0.5
    )
    fig_model.update_xaxes(title_text="Number of days")
    fig_model.update_yaxes(title_text="CAC40 daily high")
    return fig_model

def case_cac40(case, cac40):
    
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=case, y=cac40, mode='markers+lines'))
    #fig.add_trace(go.Scatter(x=data0['total_cases'], y=data0['Daily_High'], mode='markers+lines'))
    fig.update_xaxes(title_text="Total Covid cases")
    fig.update_yaxes(title_text="CAC40 Daily high")

    fig.update_layout(
        title_text="Evolution of CAC40 daily high as a function of total Covid cases in France",
        title_x=0.5
    )
    return fig    
