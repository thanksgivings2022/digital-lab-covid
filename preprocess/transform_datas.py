import preprocess.load_data1 as data
import preprocess.load_data2 as data2
import pandas as pd

def transform_data1():
    data1=data.raw_df.copy()
    df_USA=data1[data1['iso_code']=='USA']
    df_USA['date']=pd.to_datetime(df_USA['date'])
    columns=['date', 'total_cases', 'total_deaths']
    df_USA=df_USA[columns]
    df_USA['total_cases']=df_USA['total_cases'].bfill()
    df_USA['total_deaths']=df_USA['total_deaths'].bfill()
    df_USA=df_USA.reset_index().drop('index', axis=1)
    df_USA['year-month']=df_USA['date'].dt.strftime('%Y-%m')#.agg(lambda row:str(row.year)+"-"+str(row.month))
    df_USA_monthly_mean=df_USA.groupby('year-month').agg('mean')
    df_USA_monthly_mean=df_USA_monthly_mean.reset_index().rename(columns={'year-month':'date'})
    return df_USA_monthly_mean

def transform_data2():
    df_USA_GDP=data2.raw_df2.copy()
    df_USA_GDP=df_USA_GDP.rename(columns={'DATE':'date'})
    df_USA_GDP['date']=pd.to_datetime(df_USA_GDP['date'])
    df_USA_GDP.loc[len(df_USA_GDP.index)]=['2019-12', 21481.367]
    df_USA_GDP.loc[len(df_USA_GDP.index)]=['2020-02', 21481.367]
    df_USA_GDP.loc[len(df_USA_GDP.index)]=['2020-03', 19477.444]
    df_USA_GDP.loc[len(df_USA_GDP.index)]=['2020-05', 19477.444]
    df_USA_GDP.loc[len(df_USA_GDP.index)]=['2020-06', 21138.574]
    df_USA_GDP.loc[len(df_USA_GDP.index)]=['2020-08', 21138.574]
    df_USA_GDP.loc[len(df_USA_GDP.index)]=['2020-09', 21477.597]
    df_USA_GDP.loc[len(df_USA_GDP.index)]=['2020-11', 21477.597]
    df_USA_GDP['date']=pd.to_datetime(df_USA_GDP['date'])
    df_USA_GDP['date']=df_USA_GDP['date'].dt.strftime('%Y-%m')#.agg(lambda row:str(row.year)+"-"+str(row.month))
    # df_USA_GDP=df_USA_GDP[df_USA_GDP['date']<'2020-10']
    df_USA_GDP=df_USA_GDP.sort_values(by='date', ascending=True).reset_index().drop('index', axis=1)
    return df_USA_GDP

def data_joined():
    df1_transformed=transform_data1()
    df2_transformed=transform_data2()
    df_USA_tot=pd.merge(df1_transformed,df2_transformed, how='outer', on='date')\
                .sort_values(by='date', ascending=True).reset_index().drop('index', axis=1)
    return df_USA_tot

df1_df2_joined=data_joined()