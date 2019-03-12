import pandas as pd

cleaner = pd.read_csv('ctnamecleaner.csv', index_col='name')
zips = pd.read_csv('zip2town.csv', dtype=str)
towns = pd.read_csv('https://raw.githubusercontent.com/CT-Data-Collaborative/ct-town-list/master/town_fips.csv')

zips['Town'] = zips['Town'].apply(str.upper)
towns['Town'] = towns['Town'].apply(str.upper)

zips['Town'] = zips['Town'].apply(lambda x: x if x in towns.Town.values else cleaner.loc[x]['real.town.name'])
zips['Town'] = zips['Town'].apply(str.title)

zips.to_csv('zip2town_169.csv', index=False)
