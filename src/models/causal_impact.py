from causalimpact import CausalImpact
import pandas as pd
from sklearn.metrics import mean_absolute_percentage_error as MAPE

def causal_impact_analysis(ci_data, target, pre_period, post_period):

    ci_data.index = pd.to_datetime(ci_data.index, format="%Y-%m")

    ci = CausalImpact(ci_data, pre_period, post_period)
    ci.run()
    
    # Check model accuracy (MAPE) in the pre period
    y_pred_pre = ci.inferences.loc[:pre_period[1]]['point_pred']
    y_pre = ci_data.loc[:pre_period[1]][target]

    mape = MAPE(y_pre, y_pred_pre)
    print(f'The mean absolute percentage error in the pre period is {mape:.2f}%')
    
    # Model summary
    print(ci.summary())
    
    # This graph shows the empirical and counterfactual data
    #ci.plot(panels=['original', 'pointwise', 'cumulative'], figsize=(15,5))
    
    return ci