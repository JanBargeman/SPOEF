# Welcome to the SPOEF documentation

**SPOEF** is a Python package that lets you easily generate features with signal processing methods from transaction data.

## Example Usage - Generating Features

```python
transaction_features_quarterly = feature_generation(
    data=data[["name", "date", "transaction"]],
    grouper="name",
    combine_fill_method="transaction",
    time_window='quarter',
    list_featuretypes=list_featuretypes,
    observation_length=1
)
```
## License
SPOEF is created under the MIT License, see more in the LICENSE file
