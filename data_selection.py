import os

import numpy as np
import pandas as pd


def get_selected_data():

    dataframes = []

    for file in os.listdir('db_downloads'):
        if not file.endswith('.csv'):
            continue

        else:
            df = pd.read_csv(f'db_downloads/{file}')

            if df.shape[0] == 1:
                continue

            else:
                dataframes.append(df)

    data = pd.concat(dataframes, axis=0)

    # We focus on imports and re-imports
    data = data[data['Trade Flow'].isin(['M', 'RM'])].copy()

    # We eliminate the records with World as a partner
    data = data[data['Partner'] != 'World'].copy()

    # We eliminate the records where the reporter country and the partner country are the same
    # (may happen for re-imports)
    data = data[data['Reporter ISO'] != data['Partner ISO']].copy()

    # We do not differentiate based on the 2nd partner and thus select World as a 2nd partner
    data = data[data['2nd Partner'] == 'World'].copy()

    # We do not differentiate based on transport mode and thus focus on "All MOTs"
    data = data[data['Mode of Transport Code'] == 0].copy()

    # We do not differentiate based on customs procedures and thus select records for any customs procedure
    data = data[data['Customs Proc. Code'] == 'C00'].copy()

    # In some cases (in fact, for Georgia in 2018), the same trade flows are presented under several classifications
    # (H4 and H5, where H stands for the Harmonized System); in such cases, we only retain records with H5
    data['KEY'] = data['Reporter ISO'] + data['Partner ISO'] + data['Year'].astype(str) + data['Trade Flow']

    mapping = data.groupby('KEY').count()['Trade Value (US$)'].to_dict()
    data['NB_RECORDS'] = data['KEY'].map(mapping)

    data = data[
        np.logical_or(
            data['NB_RECORDS'] == 1,
            np.logical_and(
                data['NB_RECORDS'] > 1,
                data['Classification'] == 'H5'
            )
        )
    ].copy()

    # Keeping only the columns of interest
    data = data[
        ['Year', 'Trade Flow', 'Reporter', 'Reporter ISO', 'Partner', 'Partner ISO', 'Trade Value (US$)']
    ].copy()

    # Resetting the index
    data = data.reset_index(drop=True)

    return data.copy()


if __name__ == '__main__':
    data = get_selected_data()

    data.to_csv('selected_comtrade_data.csv', index=False)
