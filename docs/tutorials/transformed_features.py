import pandas as pd
from spoef.feature_generation import feature_generation
from spoef.transforms import feature_generation_transformed


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


# Generating normalized features over 1 quarter.

# For the transactions:
normalized_transaction_features_quarterly = feature_generation(
    data=data[["name", "date", "transaction"]],
    grouper="name",
    combine_fill_method="transaction",
    time_window='quarter',
    list_featuretypes=list_featuretypes,
    observation_length=1,
    normalize=True
)

# Generating PCA features over 1 quarter.

# For the transformed transactions and balances:
PCA_features_quarterly = feature_generation_transformed(
    data=data[["name", "date", "transaction", "balance"]],
    grouper="name",
    combine_fill_method="transaction",
    time_window='quarter',
    transformer_type='PCA',
    list_featuretypes=list_featuretypes,
    observation_length=1
)

# Generating ICA features over 1 quarter.

# For the transformed transactions and balances:
ICA_features_quarterly = feature_generation_transformed(
    data=data[["name", "date", "transaction", "balance"]],
    grouper="name",
    combine_fill_method="transaction",
    time_window='quarter',
    transformer_type='ICA',
    list_featuretypes=list_featuretypes,
    observation_length=1
)