from pyjstat import pyjstat
import requests
import pandas as pd
import os
os.makedirs('data', exist_ok=True)

flag_codes = {
    'Austria': ':at:',
    'Belgium': ':be:',
    'Bulgaria': ':bg:',
    'Croatia': ':hr:',
    'Cyprus': ':cy:',
    'Czechia': ':cz:',
    'Denmark': ':dk:',
    'EU27': ':eu:',
    'Estonia': ':ee:',
    'Finland': ':fi:',
    'France': ':fr:',
    'Germany': ':de:',
    'Greece': ':gr:',
    'Hungary': ':hu:',
    'Ireland': ':ie:',
    'Italy': ':it:',
    'Latvia': ':lv:',
    'Lithuania': ':lt:',
    'Luxembourg': ':lu:',
    'Malta': ':mt:',
    'Netherlands': ':nl:',
    'Poland': ':pl:',
    'Portugal': ':pt:',
    'Romania': ':ro:',
    'Slovakia': ':sk:',
    'Slovenia': ':si:',
    'Spain': ':es:',
    'Sweden': ':se:',
    'United States': ':us:'
}

#Minimum wage over time in Euros
dataset = pyjstat.Dataset.read('https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/earn_mw_cur?lang=en&lastTimePeriod=2&currency=EUR&geo=BE&geo=BG&geo=CZ&geo=DK&geo=DE&geo=EE&geo=IE&geo=EL&geo=ES&geo=FR&geo=HR&geo=IT&geo=CY&geo=LV&geo=LT&geo=LU&geo=HU&geo=MT&geo=NL&geo=AT&geo=PL&geo=PT&geo=RO&geo=SI&geo=SK&geo=FI&geo=SE&geo=US')
df = dataset.write('dataframe')
df_new = df.pivot(index='Geopolitical entity (reporting)', columns='Time', values='value')
df_new = df_new.dropna(how='all')
df_new.index = [f"{flag_codes[country]} {country}" for country in df_new.index]
df_new.to_csv('data/Eurostat_Minimum_Wage_EU_EUR.csv', index=True)

#Minimum wage over time in PPS
dataset = pyjstat.Dataset.read('https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/earn_mw_cur?lang=en&lastTimePeriod=2&currency=PPS&geo=BE&geo=BG&geo=CZ&geo=DK&geo=DE&geo=EE&geo=IE&geo=EL&geo=ES&geo=FR&geo=HR&geo=IT&geo=CY&geo=LV&geo=LT&geo=LU&geo=HU&geo=MT&geo=NL&geo=AT&geo=PL&geo=PT&geo=RO&geo=SI&geo=SK&geo=FI&geo=SE&geo=US')
df = dataset.write('dataframe')
df_new = df.pivot(index='Geopolitical entity (reporting)', columns='Time', values='value')
df_new = df_new.dropna(how='all')
df_new.index = [f"{flag_codes[country]} {country}" for country in df_new.index]
df_new.to_csv('data/Eurostat_Minimum_Wage_EU_PPS.csv', index=True)
