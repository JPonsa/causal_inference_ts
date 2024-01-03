'''
Download market stock data from yahoo finance
'''
import os
from datetime import date, datetime

import pandas as pd
import yfinance as yf
from tqdm import tqdm

TODAY_str = datetime.today().date().strftime("%Y-%M-%d")

def string2date(txt:str):
    year, month, day = txt.split("-")
    return date(year, month, day)

def split_stock_by_ticket(stock_df:pd.DataFrame, ticket:str):
        
    sticker_df = stock_df.loc[:, stock_df.columns.get_level_values(1)==ticket]
    stock_kpis = sticker_df.columns.get_level_values(0)
    sticker_df.columns = stock_kpis
    
    return sticker_df
    
def download_stocks(start:date, end:date, tickers:list, out_dir:str):
    
    # Download stock price from yahoo finance
    df = yf.download(start=start, end=end, tickers=tickers)
    
    for ticker in tqdm(tickers, desc="Processing stock"):
        ticker_df = split_stock_by_ticket(df, ticker)
        ticker_df.to_csv(f"{out_dir}{ticker}.csv")

if __name__ == "__main__":
    
    from argparse import ArgumentParser
    
    parser = ArgumentParser()
    parser.add_argument("--tickers", type=list, required=True, 
                        help="List of stock tickets")
    parser.add_argument("--start", type=str, default="1999-1-1",
                        help="Start date format YYYY-MM-DD")
    parser.add_argument("--end", type=str, default=TODAY_str,
                        help="End date format YYYY-MM-DD")
    parser.add_argument("--out", type=str, default="./stock_market/",
                        help="Outcome directory")
    
    args = parser.parse_args

    args.start = string2date(args.star)
    args.end = string2date(args.end)
    
    assert args.start <= args.end
    assert args.end <= datetime.today().date()
       
    if not os.path.isdir(args.out):
        os.makedirs(args.out)
    
    print("Downloading stock ...")
    download_stocks(args.start, args.end, args.tickers, args.out)
    print("Downloading stock - Completed")
    
    