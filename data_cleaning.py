import numpy as np
import pandas as pd

# Clean up the data

# def impute_by_LR(predictors,response, cat = True):
#     if cat:
#         lm = LogisticRegression()
#     else:
#         lm = LinearRegression()
#
#     response_to_pred = response.isnull()
#     predictors_to_pred = predictors[response.isnull()]
#     response_to_fit = response.notnull()
#     predictors_to_fit = predictors[response.notnull()]
#     lm.fit(predictors_to_fit, response_to_fit)
#     pred = lm.predict(predictors_to_pred)
#     response[response.isnull()] = pred
#     return response

def dummify(df,column_name, drop_first = False):
    dummies = pd.get_dummies(df[column_name], prefix = column_name, drop_first = False)
    df = df.drop(column_name, axis = 1)
    return pd.concat([df,dummies], axis = 1)

def log_transform(df,column_names):
    for col_name in column_names:
        new_col = 'log_' + col_name
        df[new_col] = df[(df[col_name] != 0)].col_name.apply(np.log)
        df[new_col] = df[new_col].apply(lambda x: 0 if np.isnan(x) else x)
    return df

def remove_outliers(df, column_names, std = 3):
    for col in column_names:
        df = df[(df[col].std() <= std)]
    return df

def remove_missing_values(df, column_name):
    null_mask = df[column_name].isnull()
    df = df[~(null_mask)]
    return df

def add_zeros(df, column_name):
    return df.fillna(0)
# Making plots
# Categorical variable plot, label is cateogrical
def cat_bar_plot(df, predictor_column, label_column):
    agg = df.groupby([predictor_column, label_column]).apply(len)
    agg = agg.unstack(level=label_column)
    agg.plot(kind='bar')

# Numberical variable plot, label is cateogrical
def num_kde_plot(df, predictor_column, label_column, title):
    df[df[label_column]==1][predictor_column].plot.kde(label = 1)
    df[df[label_column]==0][predictor_column].plot.kde(label = 0)
    plt.title(title)
    plt.legend()
