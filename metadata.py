import json
from pprint import pprint
import pandas as pd
import re
import os

def replace_ending(sentence, old, new):
    if sentence.endswith(old):
        i = sentence.rsplit(old,1)
        new_sentence =new.join(i)
        return new_sentence
    return sentence

with open("/Users/rkoop/Documents/cdvbw22/Data_Staatsgalerie_Stuttgart/sgs_codingDaVinci_20220329.json", "r") as f:
	data = json.loads(f.read())
	num_failed_dateiname = 0
	num_failed_entstehungszeit = 0

	lst_failed_dateiname = []
	lst_failed_entstehungszeit = []

	my_columns=['dateiname', 'titel', 'artist', 'enstehungszeit', 'objektbezeichnug', 'guid']
	df=pd.DataFrame(columns=my_columns)
	for i in range(len(data)):
		try:
			temp = data[i]["submaster"][0]['pfad']
			temp = replace_ending(temp, '.tif', '.jpg')
			df.loc[i, ['dateiname']] = temp
		except KeyError as e:
			df.loc[i, ['dateiname']] = 'NaN'
			num_failed_dateiname += 1
			lst_failed_dateiname.append(i)
		df.loc[i, ['titel']] = data[i]["titel"]
		df.loc[i, ['artist']] = data[i]["person"][0]["anzeigename"]
		try:
			df.loc[i, ['entstehungszeit']] = data[i]["entstehungszeit"]
		except KeyError as e:
			temp = data[i]["sammlung"]
			if not '19' in temp:
				df.loc[i, ['entstehungszeit']] = 'NaN'
				num_failed_entstehungszeit += 1
				lst_failed_entstehungszeit.append(i)
			else:
				df.loc[i, ['entstehungszeit']] = data[i]["sammlung"]
		df.loc[i, ['objektbezeichnung']] = data[i]["objektbezeichnung"]
		df.loc[i, ['guid']] = data[i]["guid"]

#get filename as new col
count = 0
while count < 238:
	for i in df['dateiname']:
		df.at[df.index[count],'dateiname'] = os.path.basename(df.at[df.index[count],'dateiname'])
	count += 1

df = df.set_index('dateiname')
#df.to_csv("metadata.csv")
print(df)

print("failed dateiname = " + str(num_failed_dateiname))
print("failed entstehungszeit = " + str(num_failed_entstehungszeit))
# print(df['entstehungszeit'])
# pprint(data[1])
print("failed dateinamen: ", end='')
print(lst_failed_dateiname)
print("failed entstehungszeit: ", end='')
print(lst_failed_entstehungszeit)
