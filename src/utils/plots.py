import matplotlib.pyplot as plt
import pandas as pd
import plotly_express as px
import seaborn as sns

def timeline_px(df:pd.DataFrame, event_x:str, title:str=None,
                write_html:str=None, write_image:str=None,
                labels:dict={"value":"value", "index":"index", "variables":"variables"}):

    fig = px.line(df, x=df.index, y=df.columns, title=title, labels=labels)
    fig.update_layout(shapes=[
        dict(
            type='line',
            xref='x',
            yref='paper',
            x0=event_x,
            y0=0,
            x1=event_x,
            y1=1,
            line=dict(
                color='black',
                width=2,
                dash='dash'
            )
        )
    ])
    
    if write_html:
        fig.write_html(write_html)
    
    if write_image:
        fig.write_image(write_image, format='png',engine='kaleido')
    
    fig.show()
    
    
def plot_stocks(df:pd.DataFrame, tickers:list, event_x:str):
    for ticker in tickers:
        sns.lineplot(x=df.index, y=df[ticker], label=ticker)

    plt.axvline(x=event_x, c="k", linestyle="--")
    plt.xticks(rotation=90)