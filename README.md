# comtrade_data_selection

This repository accompanies [ongoing work](https://github.com/pechouc/destination-based-sales) on the adjustment of aggregated country-by-country report statistics to approximate a destination-based mapping of multinational companies' sales. It mainly contains data on imports and re-imports of merchandise downloaded from the [UN Comtrade data portal](https://comtrade.un.org/data/) and describes the selection of the information relevant for further research.

## About the data stored here

### `db_downloads` folder

- This folder contains the `.csv` files obtained from the UN Comtrade data portal. There is at least one file for each `Reporter` that one can select on the query interface. For each of these, I requested the following data by clicking on `Download CSV`: 

| Selection field | Value chosen |
| --- | --- |
| Type of product | Goods |
| Frequency | Annual |
| HS | As reported |
| Periods (year) | 2016, 2017, 2018, 2019, 2020 |
| Partners | All |
| Trade flows | All |
| HS (as reported) commodity codes | TOTAL - Total of all HS commodities |

For a few reporter country, no data were available. The related `.csv` files only contain one row stating the absence of results. The list of files concerned is stored in `countries_without_data.txt`;

### `agg_datasets` folder

Since these data files were downloaded one by one, they might be subject to mistakes and checks are necessary to control their soundness. One of these checks involves comparing, for each reporter country, the sum of its imports to the different partner countries displayed in the data to its imports from the partner "World", i.e. to its total imports directly provided in the UN Comtrade database. The comparison logic is discussed below but to run this check, reliable on total exports is required. These are collected by selecting the same items as above on the data portal, while choosing "All" for the reporters and "World" for the partners: `simplified.csv` was obtained by clicking on "Download CSV" and `all_fields.csv` by clicking on "Download data (+) CSV".

## About the code and the other documents

- As mentioned above, checks are run to assess the quality of the data thereby gathered. These are presented in the `database_checks.ipynb` notebook. They notably involve checking the number of records in the different files, matching the names of the files with the associated reporter country or checking the consistency of the different files with each reporter country's total imports and re-imports;

- `data_selection.py`, that can be run from the command line, encapsulates the selection of the relevant information in this overall dataset. In essence, it consists in gathering the different datasets and concatenating them in a single DataFrame and restricting the resulting table to the variables of interest. Its output is the `selected_comtrade_data.csv` file. Please note that **the latter will be overwritten if you run the Python script from the commande line**;

- Eventually, the `notes` folder contains some text files that have been useful when gathering these data.

## Conclusion

For any remark or question, feel free to write to paul-emmanuel.chouc@ensae.fr.
