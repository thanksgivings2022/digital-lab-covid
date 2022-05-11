import pandas as pd

def loaddata2():
    try:
        raw_df2
        print("Data loaded locally !")
    except:
        print("Reading data1 from distant server...")
        path2 = 'https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1168&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=GDP&scale=left&cosd=2017-01-01&coed=2021-10-01&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Quarterly&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2022-03-30&revision_date=2022-03-30&nd=1947-01-01'
        # raw_df = pd.read_excel(path, sheet_name=0, header=0, names=None, index_col=None, usecols=None)
        # raw_df.to_pickle("./raw_data.pkl")
        raw_df2 =  pd.read_csv(path2)
        print("Data loaded !")
    return raw_df2

raw_df2=loaddata2()