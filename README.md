# comtrade_data_selection

This repository accompanies [my ongoing work](https://github.com/pechouc/destination-based-sales) on the adjustment of aggregated country-by-country report statistics to approximate a destination-based mapping of multinational companies' sales. It mainly contains data on imports and re-imports of merchandise downloaded from the [UN Comtrade data portal](https://comtrade.un.org/data/) and describes the selection of the information relevant for further research.

## About the data stored here

### `db_downloads`

- This folder contains the `.csv` files obtained from the UN Comtrade data portal. There is at least one file for each `Reporter` that one can select on the query interface. For each of these, I requested the following data by clicking on `Download data (+) CSV`: 

| Selection field | Value chosen |
| --- | --- |
| Type of product | Goods |
| Frequency | Annual |
| HS | As reported |
| Periods (year) | 2016, 2017, 2018 |
| Partners | All |
| Trade flows | All |
| HS (as reported) commodity codes | TOTAL - Total of all HS commodities |




