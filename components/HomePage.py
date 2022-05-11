from tkinter.ttk import Style
from dash import html,dcc
import dash_daq as daq

class HomePage():
    def __init__(self):
        self.htmlContent = html.Div([
            html.Div([
            html.H2("The project."),
            html.P("""This site was created as part of a 3-day data analysis project at Centrale DigitalLab in March 2022."""),
            html.P("Team members (in alphabetic order): Arthur Louradou, Romain Marlet and Xieyu Na"),
            html.H5("""➡️ The problem addressed is the following: what is the impact of the Covid-19 pandemic on the world economy?""",style={"color":"#4c6a9c"}),
            html.P("""On this site, we present our exploratory data analysis through graphs based on our limited data mining in the Exploration tab, then our work on machine learning model to predict an economic marker from the pandemic data is shown in the Prediction tab.
            In order to investigate economic conditions during Covid period, during the data collection phase, we took care to gather data representing the evolution of the pandemic over time as well as the evolution of different markers of the economy on the same time scale. 
            The markers of the pandemic on which we have focused are: the number of deaths due to Covid, the number of Covid positive cases and the stringency index (in several countries of the world and at different moments of the pandemic).
            The economic markers on which we have focused are: trades, GDP, GDP per capita and stock prices and unemployment. """),
            html.Div("""Actually, due to different time scale (beginning/end of Covid data) and interval (per day, per month), we had to give up half of our collected data within the project framework. During the exploratory data analysis phase, the difficulties encountered are the lack of data that are updated regularly enough. Indeed, apart from the data related to the number of deaths, only the CAC 40 and the NASDAQ are not updated daily. The other data are only updated monthly or annually (as GDP), which prevents us from doing analyses on the effects of covid.
            Second, the time ranges of all these data are not the same, which prevents us from training our models on a meaningful number of points. Given these constraints, to answer the problem, we focused on CAC40 and US GDP data.
            """)

            #html.H5("""💡 Thus, we sought to know if it was possible to predict the behavior of the CAC40 stock price in France or the GDP of a country from the Covid markers.""",style={"color":"#4c6a9c"}),
        ]),
        
        html.Div([
            html.H2("""Sources."""),
            html.Div("""The data sources we explored include:"""),html.Br(),
            dcc.Markdown('''
                            - [[1] The Impact of Covid-19 Pandemic on the Global Economy: Emphasis on Poverty Alleviation and Economic Growth - Mendeley Data](https://data.mendeley.com/datasets/b2wvnbnpj9/1)
                            - [[2] COVID-19: Income Support and Debt Relief - Our World in Data](https://data.mendeley.com/datasets/b2wvnbnpj9/1)
                            - [[3] hawkes-processes/cac40.csv at main · leleogere/hawkes-processes (github.com)](https://github.com/leleogere/hawkes-processes/blob/main/cac40.csv)
                            - [[4] https://www.kaggle.com/datasets/qks1lver/nasdaq-and-nyse-stocks-histories?select=NYSE.txt](https://www.kaggle.com/datasets/qks1lver/nasdaq-and-nyse-stocks-histories?select=NYSE.txt)
                            - [[5] Gross Domestic Product (GDP) | FRED | St. Louis Fed (stlouisfed.org)](https://fred.stlouisfed.org/series/GDP)
                            - [[6] COVID-19 Stringency Index, Jul 27, 2021 (ourworldindata.org)](https://ourworldindata.org/grapher/covid-stringency-index)
                            ''')
                           
            #dcc.Markdown('''[[2] COVID-19: Income Support and Debt Relief - Our World in Data](https://data.mendeley.com/datasets/b2wvnbnpj9/1)'''),
            #dcc.Markdown('''[[3] hawkes-processes/cac40.csv at main · leleogere/hawkes-processes (github.com)](https://github.com/leleogere/hawkes-processes/blob/main/cac40.csv)'''),
            #dcc.Markdown('''[[4] https://www.kaggle.com/datasets/qks1lver/nasdaq-and-nyse-stocks-histories?select=NYSE.txt](https://www.kaggle.com/datasets/qks1lver/nasdaq-and-nyse-stocks-histories?select=NYSE.txt)'''),
            #dcc.Markdown('''[[5] Gross Domestic Product (GDP) | FRED | St. Louis Fed (stlouisfed.org)](https://fred.stlouisfed.org/series/GDP)'''),
            #dcc.Markdown('''[[6] COVID-19 Stringency Index, Jul 27, 2021 (ourworldindata.org)](https://ourworldindata.org/grapher/covid-stringency-index)''')


            #html.A("""[1] The Impact of Covid-19 Pandemic on the Global Economy: Emphasis on Poverty Alleviation and Economic Growth - Mendeley Data""",href="#"),html.Br(),
            #html.A("""[2] COVID-19: Income Support and Debt Relief - Our World in Data""",href="#"),html.Br(),
            #html.A("""[3] hawkes-processes/cac40.csv at main · leleogere/hawkes-processes (github.com)""",href="#"),html.Br(),
            #html.A("""[4] https://www.kaggle.com/datasets/qks1lver/nasdaq-and-nyse-stocks-histories?select=NYSE.txt""",href="#"),html.Br(),
            #html.A("""[5] Gross Domestic Product (GDP) | FRED | St. Louis Fed (stlouisfed.org)""",href="#"),html.Br(),
            #html.A("""[6] COVID-19 Stringency Index, Jul 27, 2021 (ourworldindata.org)""",href="#"),
            #html.Br()
            
            ],className="home-sources"),

        html.Div([
            html.H2("""First preview of the datas."""),
            html.H5("Select a date 📅. Then, select a feature to display 📊", className="sidebar-subtitle"),
            html.Div([
                html.Span("Date:"),
                dcc.DatePickerSingle(
                    id='page-1-date-picker-single',
                    min_date_allowed='2019-12-31',
                    max_date_allowed='2020-10-19',
                    date='2020-10-10',
                    style={"margin": "0 auto"}
                ),
                html.Span("Death"),
                daq.BooleanSwitch(
                    id='strig-death-switch'
                ),
                html.Span("Stringency*")
            ],style={"display":"flex","margin":"0 10px"}),
            html.Div(id='page-1-display-map'),
        ]),
        
        html.Div([html.Figure([
                html.Blockquote(html.Span("""Definition *""",className="pb-2"),className="blockquote"),
                     html.Figcaption(
                         html.Span("""The stringency index is a composite measure based on nine response indicators including school closures, workplace closures, and travel bans, rescaled to a value from 0 to 100 (100 = strictest). If policies vary at the subnational level, the index shows the response level of the strictest subregion.""")),
                     ],className="note note-primary p-4")           
        ])     
                
        
        ],className="home-grid")
