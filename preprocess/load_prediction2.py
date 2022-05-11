import pandas as pd
#import pickle

def load_prediction2():
    try:
        df_pred2
        print("Pred data loaded locally !")
    except:
        print("Reading data pred2 from distant server...")
        #path = './preprocess/RFR_model.sav'
        #pred_df = pickle.load(open(path, 'rb'))
        path = './case_cac40.csv'
        df_pred = pd.read_csv(path)
        #result = pred_df.score(X_test, y_test)
        #print(result)
        #= pd.read_csv('RFR_model.sav')#pd.read_excel(path, sheet_name=0, header=0, names=None, index_col=None, usecols=None)
        print("Data pred2 loaded !")
    return df_pred

df_pred2=load_prediction2()