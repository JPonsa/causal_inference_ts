# Time Series Causal Impact

# Summary
This project aims to analyze the impact of the Covid-19 lockdown on the stock values of pharmaceutical companies and other industries using the Causal Impact framework. By employing global economic indicators as counterfactuals, I seek to understand the specific influence of the lockdown on the stock performance of pharmaceutical companies and compare it with other industries.

# Goals
The primary goals of this project are as follows:

- Assessment of Impact: Evaluate and <u>quantify</u> the causal impact of Covid-19 lockdowns on the stock values of pharmaceutical companies and other selected industries. I have the hypothesis that although COVID affected all industries including pharma, this is more resilient and had a faster recovery; especially those pharma companies which developed a vaccine (e.g. GSK, Pfizer).

- Counterfactual Analysis: Use global economic indicators as counterfactuals to establish a baseline for stock performance. Ideally counterfactuals would helps us to assess the predicted performance if no treatment (e.g. COVID pandemic) would have been implemented. However, in this cases this is unrealistic as the COVID pandemic affected all economic sectors in multiple ways. However, the use of global indicators as counterfactuals help me to establish whether pharmaceutical companies had a stronger/faster recovery if the economic inactivity due to COVID lockdown.

- Insights Generation: Derive meaningful insights into the differential impact of lockdown measures on pharmaceutical stocks compared to different pharmaceutical industries (e.g. those which developed a vaccine vs those which did not) or other industries.

# About the Data

Daily Adjusted Closed Stock price was obtained using the yahoo finance API/library.Then monthly average was computed to address missing values and daily fluctuations  

# Approach
## Causal Impact Framework
The Causal Impact framework is employed to estimate the causal effect of Covid-19 lockdowns on stock values. It uses a Bayesian structural time-series model to compare the observed stock prices during the lockdown period with a counterfactual scenario (expected stock prices without the lockdown). This enables the isolation of the causal impact attributable to the lockdown.

The Google Data Science team created an [R package](https://google.github.io/CausalImpact/CausalImpact.html) for causal impact analysis. Several people have attempted to re-implement it in python.

## Global Economic Indicators as Counterfactuals
In addition to traditional control groups, global economic indicators such as S&P 500 Index, Dow Jones Industrial and MSCI World Index are used as counterfactuals. This approach aims to capture broader economic trends in response to the COVID lockdown and the resultant economical slow down.

# Observations
## Preliminary Findings

In March 2020, the global economy suffered an recession. However, observations indicate variations during the following 3-6 months in the impact of lockdowns on different industries. Pharmaceutical stocks, for instance, might display resilience compared to sectors more sensitive to economic downturns.

### Pfizer
![Pfizer Causal Impact Python](https://github.com/JPonsa/causal_inference_ts/blob/main/figures/python/PFE.png)
### GSK
![GSK Impact Python](https://github.com/JPonsa/causal_inference_ts/blob/main/figures/python/GSK.png)
### Coca-Cola
![KO Causal Impact Python](https://github.com/JPonsa/causal_inference_ts/blob/main/figures/python/KO.png)
### Inditext (Zara, Massimo Dutti, other)
![InDITEXT Causal Impact Python](https://github.com/JPonsa/causal_inference_ts/blob/main/figures/python/ITX.MC.png)

### Global Economy Indicators
<iframe src= "https://github.com/JPonsa/causal_inference_ts/blob/main/figures/global%20economy.html" 
        width="100%" 
        height="300px"></iframe>


## Visualizations
The project includes visualizations, such as time series plots and causal impact plots, to present the findings comprehensively. These visual aids enhance the interpretability of results.

## Inconsistent results
I obtained different result when analysing the same data using either the [original R package](https://google.github.io/CausalImpact/CausalImpact.html) (from Google) or [a port](https://github.com/jamalsenouci/causalimpact/) to pythons

Below I am showing the analysis for Pfizer using the Python library or the R package. It can be observed that in the Python analysis, the 

### Python analysis
![Pfizer Causal Impact Python](https://github.com/JPonsa/causal_inference_ts/blob/main/figures/python/PFE.png)
### R analysis
![Pfizer Causal Impact R](https://github.com/JPonsa/causal_inference_ts/blob/main/figures/R/PFE.png)

# Future Work
## Refinement of Models
Iterative refinement of the Bayesian structural time-series model and incorporation of additional variables may enhance the accuracy of impact estimates.

## Sector-Specific Analysis
Further exploration into sub-sectors within pharmaceuticals and other industries may reveal nuanced impacts that the current analysis may overlook.

## External Factors
Considering external factors, such as regulatory changes and vaccine developments, in the analysis may provide a more comprehensive understanding of stock value dynamics.

# References:
Brodersen KH, Gallusser F, Koehler J, Remy N, Scott SL. Inferring causal impact using Bayesian structural time-series models. Annals of Applied Statistics, 2015, Vol. 9, No. 1, 247-274. http://research.google.com/pubs/pub41854.html

https://www.kaggle.com/code/yessirbacon1/causal-inference-with-time-series-forecasting

https://www.youtube.com/watch?v=wdXTb9g1-w0