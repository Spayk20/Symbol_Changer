import configparser
import pandas as pd
pd.options.mode.chained_assignment = None

config = configparser.ConfigParser()
config.optionxform = str
config.read('symbols_dict.cfg', encoding='utf-8')
DACH = dict(config['DACH'])
WW = dict(config['WW'])

def umlauts_changing(dtframe, region):
    columns = ('First Name', 'Last Name', 'Account Name (Account Name)')
    changes_in_columns = {'First Name': 0, 'Last Name': 0, 'Account Name (Account Name)': 0}

    for column in columns:
        changes = 0
        for cell in range(0, len(dtframe.index)):
            if region == 'Весь мир':
                dtframe[column].iloc[cell], changes = symbols_to_ascii(dtframe[column].iloc[cell], WW)
            if region == 'DACH':
                dtframe[column].iloc[cell], changes = symbols_to_ascii(dtframe[column].iloc[cell], DACH)
            changes_in_columns[column] += changes
    return dtframe, changes_in_columns


def symbols_to_ascii(cell, region):
    symbls_changed = 0
    for sym, val in region.items():
        if sym in cell:
            cell = cell.replace(sym, val)
            symbls_changed += 1
    return cell, symbls_changed


def emails_selection(dtframe):
    dtframe['Email'] = dtframe['Email'].fillna(dtframe['Secondary Email'])
    for i in range(0, len(dtframe.index)):
        if (dtframe['Wrong email'].iloc[i] is False) or (dtframe['Email source'].iloc[i] not in ('Direct communication', 'Company website')):
            dtframe['Email'].iloc[i] = dtframe['Secondary Email'].iloc[i]
    del dtframe['Secondary Email']
    del dtframe['Wrong email']
    del dtframe['Email source']
    del dtframe['Wrong secondary Email']
    del dtframe['Secondary Email source']
    return dtframe





