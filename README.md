# Time Series Causal Impact

# Summary
Explore the profound impact of the Covid-19 lockdown on stock values, particularly focusing on pharmaceutical companies and other industries. Leveraging the Causal Impact framework and global economic indicators, this project aims to provide a nuanced understanding of how certain industries/companies were initially affected by the economic impact of lockdown and their recovery trends.

# Goals
The primary goals of this project are as follows:

- Assessment of Impact: Evaluate and quantify the causal impact of Covid-19 lockdowns on the stock values of pharmaceutical companies and selected industries. The project hypothesizes that pharmaceutical companies, especially those developing vaccines (e.g., GSK, Pfizer), exhibit resilience and a faster recovery compared to other sectors.

- Counterfactual Analysis: Utilise global economic indicators as counterfactuals to establish a baseline for stock performance. While traditional control groups may not be feasible due to the widespread impact of the pandemic, global indicators like S&P 500, Dow Jones Industrial, and MSCI World Index help assess the unique recovery patterns of pharmaceutical companies amid the economic slowdown.

- Insights Generation: Derive meaningful insights into the varying impact of lockdown measures on pharmaceutical stocks, comparing different pharmaceutical industries (e.g., vaccine developers vs. non-developers) and other sectors.

# About the Data
Daily Adjusted Closed Stock prices were sourced using the Yahoo Finance API/library. Monthly averages were computed to address missing values and daily fluctuations, ensuring a robust dataset for analysis.

# Approach
## Causal Impact Framework
Employing the Causal Impact framework, a Bayesian structural time-series model is utilized to estimate the causal effect of Covid-19 lockdowns on stock values. By comparing observed stock prices during the lockdown period with a counterfactual scenario (expected prices without the lockdown), the project isolates the causal impact attributable to the lockdown

## Global Economic Indicators as Counterfactuals
In addition to traditional control groups, global economic indicators such as S&P 500, Dow Jones Industrial, and MSCI World Index are incorporated as counterfactuals. This approach captures broader economic trends in response to the COVID lockdown and the resulting economic slowdown.

# Observations
## Preliminary Findings
In the aftermath of the March 2020 global economic recession, variations in the impact of lockdowns on different industries were observed over the subsequent 3-6 months. Pharmaceutical stocks displayed resilience, especially those of companies involved in vaccine development (e.g., Pfizer, GSK), compared to sectors more sensitive to economic downturns (e.g., Coca-Cola, Inditext).

### Pfizer
![Pfizer Causal Impact Python](https://github.com/JPonsa/causal_inference_ts/blob/main/figures/python/PFE.png)
### GSK
![GSK Impact Python](https://github.com/JPonsa/causal_inference_ts/blob/main/figures/python/GSK.png)
### Roche
![Roche Impact Python](https://github.com/JPonsa/causal_inference_ts/blob/main/figures/python/ROG.png)
### Coca-Cola
![KO Causal Impact Python](https://github.com/JPonsa/causal_inference_ts/blob/main/figures/python/KO.png)
### Inditext (Zara, Massimo Dutti, other)
![InDITEXT Causal Impact Python](https://github.com/JPonsa/causal_inference_ts/blob/main/figures/python/ITX.MC.png)

### Global Economy Indicators
![Global Economy](https://github.com/JPonsa/causal_inference_ts/blob/main/figures/global%20economy.png)


## Visualizations
The project includes visualizations, such as time series plots and causal impact plots, to present the findings comprehensively. These visual aids enhance the interpretability of results.

## Inconsistent results
Notably, inconsistent results were obtained when analyzing the same data using both the [original R package](https://google.github.io/CausalImpact/CausalImpact.html) from Google and a [Python port](https://github.com/jamalsenouci/causalimpact/). Discrepancies were observed in the analysis for Pfizer, emphasizing the need for careful consideration of analysis tools.

Below I am showing the analysis for Pfizer using the Python library or the R package. It can be observed that in the Python analysis the predicted trend is influenced by the economic indicators use as covariants; while in the R package is driven mainly by the historic values. This leads to different counterfactuals and conclusions. In this particular scenario it is hard to determine which one is right. In an ideal scenario we would (1) have better covariants unaffected by the treatment and (2) able to conduct an A/B testing for further validation. 

### Python analysis
![Pfizer Causal Impact Python](https://github.com/JPonsa/causal_inference_ts/blob/main/figures/python/PFE.png)
### R analysis
![Pfizer Causal Impact R](https://github.com/JPonsa/causal_inference_ts/blob/main/figures/R/PFE.png)

# Future Work
- Explore other libraries for causal impact analysis.
- Explore other covariants.
- Implement some Time Series forecasting. I did some preliminary analysis using SARIMAX, VARMAX and others.

# References:
Brodersen KH, Gallusser F, Koehler J, Remy N, Scott SL. Inferring causal impact using Bayesian structural time-series models. Annals of Applied Statistics, 2015, Vol. 9, No. 1, 247-274. http://research.google.com/pubs/pub41854.html

https://www.kaggle.com/code/yessirbacon1/causal-inference-with-time-series-forecasting

https://www.youtube.com/watch?v=wdXTb9g1-w0