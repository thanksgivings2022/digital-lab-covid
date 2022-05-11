import pandas as pd

def loaddata1():
    try:
        raw_df
        print("Data loaded locally !")
    except:
        print("Reading data1 from distant server...")
        path = './data1.xlsx'
        # raw_df = pd.read_excel(path, sheet_name=0, header=0, names=None, index_col=None, usecols=None)
        # raw_df.to_pickle("./raw_data.pkl")
        raw_df =  pd.read_pickle("./raw_data.pkl")
        print("Data loaded !")
    return raw_df

raw_df=loaddata1()




