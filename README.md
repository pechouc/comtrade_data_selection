# comtrade_data_selection

This repository accompanies [ongoing work](https://github.com/pechouc/destination-based-sales) on the adjustment of aggregated country-by-country report statistics to approximate a destination-based mapping of multinational companies' sales. It mainly contains data on imports and re-imports of merchandise downloaded from the [UN Comtrade data portal](https://comtrade.un.org/data/) and describes the selection of the information relevant for further research.

## About the data stored here

### `db_downloads` folder

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

- For a few reporter country, no data were available. The related `.csv` files only contain one row stating the absence of results. The list of files concerned is stored in `countries_without_data.txt`;

- Eventually, after the first download, 4 files (for Germany, Spain, Turkey and Madagascar) displayed exactly 100,000 records. This corresponds to the maximum number of records for a data file downloaded from the UN Comtrade data portal. In 3 of these cases, all the available data could be downloaded for each year separately. In the remaining case (Spain), data were downloaded for each year separately, focusing on imports and re-imports in the `Trade flows` selection field. These are indeed the only trade flows in which I am ultimately interested.

### `agg_datasets` folder






