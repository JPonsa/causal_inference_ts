# Pharmaceutical Companies
pharma_companies = {
    # 'BNTX': 'BioNTech SE',
    'PFE': 'Pfizer Inc.',
    'JNJ': 'Johnson & Johnson',
    'NVS': 'Novartis AG',
    'ROG': 'Roche Holding AG',
    'MRK': 'Merck & Co., Inc.',
    'SNY': 'Sanofi',
    'GSK': 'GlaxoSmithKline plc',
    'AZN': 'AstraZeneca PLC',
    'LLY': 'Eli Lilly and Company',
    'ABBV': 'AbbVie Inc.'
 }

# consumner stables
consumer_staples = {
'KO' : 'The Coca-Cola Company (KO)',
'CL' : 'Colgate-Palmolive Company (CL):',
'KMB' : 'Kimberly-Clark Corporation (KMB)',
'UL': 'Unilever (UL)'
}

# Retail
retail = {
    "AMZN" : "Amazon.com, Inc.",
    "ITX.MC" : "Industria de Diseño Textil, S.A.",
    "HNNMY" : "Hennes & Mauritz AB",
    "MC.PA" : "LVMH Moët Hennessy Louis Vuitton S.E.",
    "9983.T": "Fast Retailing Co., Ltd."
}

# Global Economy Indicators
global_economy_indicators = {
    '^GSPC' : 'S&P 500 Index',
    '^IXIC' : 'NASDAQ Composite',
    '^FTSE' : 'FTSE 100 (^FTSE)',
    '^DJI' : 'Dow Jones Industrial Average',
    'MSCI' : 'MSCI World Index'
 }

industry_tickers = {"Pharma" : pharma_companies,
                    "Consumables" : consumer_staples,
                    "Retail" : retail,
                    "Global Economy" : global_economy_indicators}

tickers = (list(pharma_companies.keys())
          + list(consumer_staples.keys())
          + list(retail.keys())
          + list(global_economy_indicators.keys()))