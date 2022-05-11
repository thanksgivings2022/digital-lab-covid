import pandas as pd
import pickle

def load_prediction():
    try:
        df_pred
        print("Pred data loaded locally !")
    except:
        print("Reading data1 from distant server...")
        #path = './preprocess/RFR_model.sav'
        #pred_df = pickle.load(open(path, 'rb'))
        path = './ytest_ypred.csv'
        df_pred = pd.read_csv(path)
        #result = pred_df.score(X_test, y_test)
        #print(result)
        #= pd.read_csv('RFR_model.sav')#pd.read_excel(path, sheet_name=0, header=0, names=None, index_col=None, usecols=None)
        print("Data loaded !")
    return df_pred

df_pred=load_prediction()