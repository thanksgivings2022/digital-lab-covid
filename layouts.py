from dash import dcc,html 
from plots import * 

##Analyse des données##
import preprocess.load_data1 as data
import preprocess.transform_datas as data_joined
import preprocess.load_prediction as data_model
import preprocess.load_prediction2 as data_model2

df = data.raw_df.copy()
countries_list = df.location.unique()
df_pred = data_model.df_pred.copy() 
df_pred2 = data_model2.df_pred2.copy() 
df_joined = data_joined.df1_df2_joined.copy() 
##FINAnalyse des données##



from components.navbar import * 
from components.HomePage import HomePage

sidebar = html.Aside(html.Div([html.H3("Filters"),
            html.Span("Select a date 📅", className = "sidebar-subtitle"), 
            #https://dash.plotly.com/dash-core-components/datepickersingle
            dcc.DatePickerSingle(id = 'page-1-date-picker-single',
                min_date_allowed = '2019-12-31',
                max_date_allowed = '2020-10-19',
                date = '2020-10-10'
            ),
            html.Span("Select some countries 🌍", className = "sidebar-subtitle"),
            dcc.Dropdown(countries_list,
                ["France", "Spain", "Italy", "Belgium"],
                multi = True,
                id = 'page-1-dropdown'
            )
        ], className = "sidebar-content"),
        className = "sidebar"
    ) 

home = html.Div([navbar(),
        html.Div([HomePage().htmlContent, #html.H1("Welcome home."), #html.P("Please select a view to continue.")
                  ],className = "home-content")
    ]) 
                      
layout1 = html.Div([navbar(),
            html.Div([sidebar,
                    html.Div([#html.H3('Exploration View'),
                        html.Div([html.Div(id = 'page-1-display-value'),
                            html.Div(id = 'page-1-display-death-stringency'),
                            html.Div(dcc.Graph(figure = plot_USA_GDP_deaths_cases(df_joined))),
                            html.Div([html.Br(),
                                html.Br(),
                                html.H5("Explanation"),
                                html.Br(),
                                html.Div("""
                                    Firstly we present the geopolitical context in which the economic impact results. On the top-left figure, we can visualize the total number of deaths among Covid cases. The x-axis shows the scope of the Covid impact and the slope on y-axis gives rise to the mortality situation per country. On the top-right figure, with stringency index variation, we can further investigate political measurements setted up by each country as a response to Covid peak situations. Finally the left-down graph shows the importance of the epidemic peak on the evolution of the US GDP. We choose US because after our research, the US is considered the most Covid-impacted country of the world. We can observe that during the first peak, the US peak dropped from 21.5 k in early 2020 to 19.5 k during the first peak. Nevertheless,it is interesting to note that the US GDP has recovered its initial level(post - covid) but even that it is increasing faster than before. It would be interesting to compare this curve with that of China - the first country impacted by the crisis, to be able to interpret the potential effect of time scale of the Covid on economic impact.                                                  
                                    """)]) # say if one of the two countries emerged stronger from the Covid crisis (from the point of view of the GDP marker).
                                ], className = "content-grid")], className = "content sidebar-left", style = {
                                "flex-basis": "100%"
                            }
                        )], style = {
                            "display": "flex"
                        }
                    )]) 

layout31 = html.Div([
    navbar(),
    html.Div(
html.Div(
        html.Div([
            ], className = "content-grid"),
        className = "content",
        style = {
            "flex-basis": "100%"
        }),style={"display":"flex"})
    ])

layout3 = html.Div([navbar(),
            html.Div([
                html.Div([
                    html.Div([
                        html.H2('Study case: regression model applied on CAC40 in France',style={"grid-area": "Title"}),
                        html.Div([
                            dcc.Graph(figure=plot_deaths_cases_stringency(df, "France")),
                        ],style={"grid-area": "Plot1"}),
                        html.Div([html.Div(id='page-3-display-value'),
                            dcc.Graph(figure=case_cac40(df_pred2.total_cases, df_pred2.Daily_High)),
                        ],style={"grid-area": "Plot2"}),
                        html.Div([  # html.H3('Prediction by Random Forest Regressor'),
                            html.Div(id='page-3-display-value'),
                            dcc.Graph(figure=plot_prediction(df_pred.index, df_pred.y_real, df_pred.y_model)),
                        ],style={"grid-area": "Plot3"}),

                        html.Div([dcc.Markdown('''
                            -  *Objectif*: For the prediction part, we would like to study relation between number of positive Covid cases in France and CAC 40 using a random forest regressor pre-implemented in scikit-learn library.
                            -- feature = total positive Covid case, 
                            -- daily target = CAC 40 daily high, daily
                            - *Data prepocessing*: The first step is to clean and reshape our data into a feature - target matrix. In order to gather feature and target on the same time scale, our feature - target matrix is limited to 87 data, correspondant to the time period 2019-12-31 to 2020-04-03, excluding on one hand weekends where there is no CAC40 recording, and on the other hand NaN rows, i.e. both feature and target data are NaN.
                            - *Prediction graph*: The plots besides are computed with a 5-tree random forest regressor, they represent the value of the CAC40 as a function of the total number of
                                    Covid cases. We observe that the CAC40 price drops by a third during the first epidemic peak.Then, it stabilizes when the total number of cases reaches 20 k people.Its price even remains constant despite the fact that the number of
                                    cases increases: this is due to the fact that it is not an epidemic peak.A second time, around 57 k cases, a second epidemic peak appeared and the CAC40 price collapsed again.
                            - *Model evaluation*: score=0.8298072051345051, Mean Absolute
                                        Error = 2.78135200191064, Mean Squared Error = 41.44987646583772, Root Mean Squared Error = 6.438157847229106
                            '''), 
                                 html.H5("""💡 Conclusion: given the limited data at our disposal, the random forest regression model performs surprisingly well with a score of 0.83. Thus, we are optimistic about if it was possible to predict the behavior of the CAC40 stock price in France or the GDP of a country from the Covid markers. Furthermore, if the data were available to us, it would be interesting to analyze the behavior of other stock prices to compare them.""",style={"color":"#4c6a9c"})
                                  ],style={"grid-area": "Description"})
                    ], className = "content-grid predictions")], className = "content", style = {
                            "flex-basis": "100%"
                        }
                    )], style = {
                        "display": "flex"
                    }
                )])

