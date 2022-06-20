import pandas as pd
import os
from path import img_path

df = pd.read_csv('metadata/metadata.csv')

#Corrections
#1,,Stilleben mit Blumen und Eßwaren,Georg Flegel,,,9BA1B1E144A3411A9A51859A67D8E530,um 1630,Gemälde
df.at[1, 'dateiname'] = 'flegel_1640.jpg'
#9,,"Komposition in Weiß, Rot und Blau (Composition en blanc, rouge et bleu)",Piet Mondrian,,,61E27C0B46CAC95BBFAB85BBA5FF4C15,1936,Gemälde
df.at[9, 'dateiname'] = 'sgs_mup_mondrian_2753_s01_s.jpg'
#23,,Sturm in der Campagna,Oswald Achenbach,,,A5D5C0BF45225B82939352A80907767E,1887,Gemälde
df.at[23, 'dateiname'] = 'achenbach_941.jpg'
#36,,Tableau II,Piet Mondrian,,,AD15EEE340EF8F48546D97B6EE8F4265,1921,Gemälde
df.at[36, 'dateiname'] = 'sgs_mup_mondrian_3353_001_s.jpg'
#37,,Das Donautal bei Gutenstein,Christian Landenberger,,,60055473465C4C3283C4B983150418F2,1893,Gemälde
df.at[37, 'dateiname'] = 'landenberger_1671.jpg'
#48,,Leibls Landhaus in Aibling,Johann Sperl,,,0035DE614C2C737CC35437908E053DD7,um 1883,Gemälde
df.at[48, 'dateiname'] = 'sperl_1110.jpg'
#51,,Päonien,Max Slevogt,,,4DC1894446F64A38FA4E9F802678C3F8,1907,Gemälde
df.at[51, 'dateiname'] = 'slevogt_2581.jpg'
#64,,Landschaft am Ammersee,Christian Landenberger,,,C43BB34D4C3B87C7EEC39B9DA883E0A0,1922,Gemälde
df.at[64, 'dateiname'] = 'landenberger_2068.jpg'
#67,,Königstiger,Bruno Piglhein,,,AD14FBEF46CC061EFFB9C8B0D38C1BAD,Um 1910,Gemälde
df.at[67, 'dateiname'] = 'piglhein_1224.jpg'
#70,,Segelboote,Frans Swagers,,,F1952A9C4161EE10AA9C20A23458C6EC,Um 1800,Gemälde
df.at[70, 'dateiname'] = 'swagers_487.jpg'
#71,,Bächlingen an der Jagst,Theodor Schnitzer,,,482301914B7548C7B10F9489FB6A5A35,19. Jahrhundert,Gemälde
df.at[71, 'dateiname'] = 'schnizer_2705.jpg'
#90,,Farbentanz,Ernst Ludwig Kirchner,,,BED9F0C14D220818B64F4F8C875826DD,1933/34,Druckgraphik
df.at[90, 'dateiname'] = 'sgs_grs_kirchner_a_1957_2015_001_s.jpg'
#107,,Pianta di Roma e del Campo Marzo,Giovanni Battista Piranesi,,,99EB413A45028B1A6601058779D0A64E,um 1774 (um 1780),Druckgraphik
df.at[107, 'dateiname'] = 'piranesi_a-1961-2386-2-kk.jpg'
#119,,[Zeichnung],Adolf Hölzel,,,2D288F3BCF3445A4B116864CE5883F48,,Zeichnung
df.at[119, 'dateiname'] = 'sgs_grs_hoelzel_c-1918-32_001_s.jpg'
#131,,"Tiger (Vignette Seite 57 in: Gustav Schiefler, Edvard Munch. Das graphische Werk 1906-1926, Berlin 1928)",Gustav Schiefler,,,B03864A5D5334A27A5BF54315ADEF15A,1928,Druckgraphik
df.at[131, 'dateiname'] = 'munch_b-1950-664-16.jpg'
df.at[11, 'artist'] = 'Edvard Munch'
#151,,Bauhaus-Drucke. Neue Europäische Graphik. 3te Mappe: Deutsche Künstler (Mappe),Otto Dorfner,,,287028806EC34156B1225191A0B9A707,1922,Druckgraphik
df.at[151, 'dateiname'] = 'sgs_grs_bauhausmappe-3_a-1974-5353_001_s.jpg'
#181,,Le Bouquet d'annes,Charles-François Daubigny,,,5E74D2C2B230431A86B6C36ABFC25FB5,1862,Fotografie
df.at[181, 'dateiname'] = 'daubigny_f-2005-534.jpg'
#202,,Gebirgige Küste auf Madeira,Eduard Hildebrandt,,,9B291AA5FB404FBEB3B56586D417D5E2,1848,Zeichnung
df.at[202, 'dateiname'] = 'hildebrandt_c-2017-5756-87.jpg'
#209,,Hafen in Dordrecht,Franz Skarbina,,,8BA24627F9E8433BA225F858CFAEDFCB,1884,Zeichnung
df.at[209, 'dateiname'] = 'sgs_grs_skarbina_c-2017-5756-276_001_s.jpg'
#214,,Kōrin Album (Kōrin gafu),Taniguchi Kōkyō,,,158345691F0E4997B686609C0F36D461,1891,Skizzenbuch
df.at[214, 'dateiname'] = ''



#corrections for typos in metadata
df['tmp'] = df['dateiname']
df = df.set_index('tmp')

df.at['sgs_mup_widmayer_3835_o01_s.jpg', 'dateiname'] = 'sgs_mup_wiedmayer_3835_001_s.jpg'
df.at['sgs_grs_feuerbach_c-1920-5_001_s.jpg', 'dateiname'] = 'sgs_grs_feuerbach_c-1920-5_o01_s.jpg'
df.at['sgs_grs_klee_d-2005-681-1_001_s.jpg', 'dateiname'] = 'sgs_grs_klee_d-2005-681-2_001_s.jpg'
df.at['sgs_mup_jawlenski_2174_001_s.jpg', 'dateiname'] = 'sgs_mup_jawlensky_2174_001_s.jpg'
df.at['sgs_grs_ensor_a-1985-6234_001_s.jpg', 'dateiname'] = 'sgs_grs_ensor_a-1985-6234_o01_s.jpg'
df.at['sgs_mup_delaunay_2795_001_s.jpg', 'dateiname'] = 'sgs_mup_delaunay_2795_002_s.jpg'
df.at['sgs_mup_reininger_1216_001_s.jpg', 'dateiname'] = 'sgs_mup_reiniger_1216_001_s.jpg'
df.at['sgs_mup_kanoldt_3030_001_s.jpg', 'dateiname'] = 'sgs_mup_kanoldt_3030_002_s.jpg'
df.at['sgs_mup_klee_3089_001_s.jpg', 'dateiname'] = 'sgs_mup_klee_3089_002_s.jpg'
df.at['sgs_grs_kirchner_c-1957-761_001_s.jpg', 'dateiname'] = 'sgs_grs_kirchner_c-1957-761_o01_s.jpg'
df.at['sgs_grs_kirchner_c-1957-745_001_s.jpg', 'dateiname'] = 'sgs_grs_kirchner_c-1957-745_002_s.jpg'
df.at['sgs_grs_schwitters_d-1966-316-7_001_s.jpg', 'dateiname'] = 'sgs_grs_schwitters_d-1966-316-2_001_s.jpg'
df.at['sgs_mup_klee_l-1428_001_s.jpg', 'dateiname'] = 'sgs_mup_klee_3783_001_s.jpg'

#df.to_csv('metadata_clean.csv')

#check corrections
filenames_data = [f for f in os.listdir(img_path) if os.path.isfile(os.path.join(img_path, f))]
filenames_metadata = df['dateiname'].to_list()
missing = []
for file in filenames_data:
	if file not in filenames_metadata:
		missing.append(file)
		print(file)

for file in filenames_metadata:
	try: 
		open(img_path + file)
	except:
		pass
		print(file)

#remove from list
# files without metadata
img_without_data = ['sgs_arc_xxx_ah-1-ge-div-538-0001r_001_m.jpg', 'sgs_grs_klee_d-2005-681-6_001_s.jpg', 'sgs_grs_schwitters_d-1966-316-4_001_s.jpg']

#metadata entries without files
# sgs_grs_vuillard_a-1986-6279_001_s.jpg
# sgs_grs_moholy_a-1974-5368-c_001_s.jpg


