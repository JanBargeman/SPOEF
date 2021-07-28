'''python
import pandas as pd
from spoef.feature_generation import feature_generation

# Generating the data
data = pd.DataFrame([
    ['John', 1, '2021-01-03', 1000, 1000],
    ['John', 1, '2021-02-03', 1000, 2000],
    ['John', 1, '2021-03-03', -3000, -1000],
    ['Jane', 0, '2021-01-03', 1000, 1000],
    ['Jane', 0, '2021-02-03', 5000, 6000],
    ['Jane', 0, '2021-03-03', 2000, 8000],
    ],
    columns=['name', 'label', 'date', 'transaction', 'balance']
    )
# Make the date into datetime object.
data.date = pd.to_datetime(data.date, format="%Y-%m-%d")


# Setting up which features to generate.
list_featuretypes = ["Basic", "FourierComplete", "FourierNLargest", "WaveletComplete", "WaveletBasic"]


# Generating features over 1 quarter.

# For the transactions:
transaction_features_quarterly = feature_generation(
    data=data[["name", "date", "transaction"]],
    grouper="name",
    combine_fill_method="transaction",
    time_window='quarter',
    list_featuretypes=list_featuretypes,
    observation_length=1
)

# Generating features over 1 year.

# For the transactions:
transaction_features_yearly = feature_generation(
    data=data[["name", "date", "transaction"]],
    grouper="name",
    combine_fill_method="transaction",
    time_window='year',
    list_featuretypes=list_featuretypes,
    observation_length=1
)
'''
