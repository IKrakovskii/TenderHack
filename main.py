#!/usr/bin/python3

import pandas as pd

# df_contracts = pd.read_excel('Data/Контракты_Иркутск.xlsx')
# df_STE_Irkutsk = pd.read_excel('Data/СТЕ_Иркутск.xlsx')
# df_contracts.to_csv('Data/Контракты_Иркутск.csv')
# df_STE_Irkutsk.to_csv('Data/СТЕ_Иркутск.csv')

df_contracts = pd.read_csv('Data/Контракты_Иркутск.csv')


# firs_file = pd.DataFrame({
#     'Name_Customer': list(df_contracts['Наименование заказчика'].values),
#     'INN': list(df_contracts['ИНН заказчика'].values),
#     'CPP': list(df_contracts['КПП заказчика'].values)
# })
#
# firs_file.to_csv('Data/csv_files/first_file.csv')
#
# second_file = pd.DataFrame({
#     'Name_Suppliers': list(df_contracts['Наименование поставщика'].values),
#     'INN': list(df_contracts['ИНН поставщика'].values),
#     'CPP': list(df_contracts['КПП поставщика'].values)
# })
#
# second_file.to_csv('Data/csv_files/Исполнители_file.csv')