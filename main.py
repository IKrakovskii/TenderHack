#!/usr/bin/python3
import excel2json
import pandas as pd

df_contracts = pd.read_excel('Data/Контракты_Иркутск.xlsx')
df_STE_Irkutsk = pd.read_excel('Data/СТЕ_Иркутск.xlsx')
# df_STE_Irkutsk.to_json('Data/СТЕ_Иркутск.json')
# df_contracts.to_json('Data/Контракты_Иркутск.json')
# excel2json.convert_from_file('Data/Контракты_Иркутск.xlsx')
excel2json.convert_from_file('Data/Контракты_Иркутск.xlsx', 'Data')