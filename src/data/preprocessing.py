import pandas as pd

def cacl_monthly_avg_kpi(stock_df:pd.DataFrame, kpi:str="Adj Close"):

    kpi_df = stock_df[kpi]

    monthly_avg = kpi_df.resample('M').mean()
    monthly_avg.index = monthly_avg.index.strftime('%Y-%m')
    
    return monthly_avg

