import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

from analysis import *


# VOTERS
roll14 = pd.read_csv('Lembah Pantai GE14 Roll.csv')
roll13 = pd.read_csv('Lembah Pantai GE13 Roll.csv')

# SCORE
score_slp = pd.read_excel('results.xlsx', sheetname='SouthLembahPantai')
score_slp14 = score_slp[score_slp['GE'] == 'GE14']
score_slp13 = score_slp[score_slp['GE'] == 'GE13']


#______________________________________________________________________________________________________________________________

roll_slp14 = roll14[(roll14['NamaDM']=='TAMAN BUKIT ANGKASA') | (roll14['NamaDM']=='PANTAI HILL PARK') |(roll14['NamaDM']=='TAMAN SRI SENTOSA UTARA') |(roll14['NamaDM']=='TAMAN SRI SENTOSA SELATAN')]
roll_slp13 = roll13[(roll13['NamaDM']=='TAMAN BUKIT ANGKASA') | (roll13['NamaDM']=='PANTAI HILL PARK') |(roll13['NamaDM']=='TAMAN SRI SENTOSA UTARA') |(roll13['NamaDM']=='TAMAN SRI SENTOSA SELATAN')]

def calculate_age(born):
    electionday = pd.to_datetime('2018-05-09')
    return electionday.year - born.year - ((electionday.month, electionday.day) < (born.month, born.day))

roll_slp14['Age'] = pd.to_datetime(roll_slp14['TahunLahir']).apply(lambda x: calculate_age(x))
max_age = max(roll_slp14['Age'].max(),roll_slp13['Umur'].max())

roll_slp14['AgeGroup'] = pd.cut(roll_slp14['Age'], [20,30,40,50,60,70,80,max_age] )
roll_slp13['AgeGroup'] = pd.cut(roll_slp13['Umur'], bins=[20,30,40,50,60,70,80,max_age])
#______________________________________________________________________________________________________________________________
age_group14_dict_tba = dict(age_group_ratio(roll_slp14, 'TAMAN BUKIT ANGKASA') )
age_group14_dict_php = dict(age_group_ratio(roll_slp14, 'PANTAI HILL PARK') )
age_group14_dict_tssu = dict(age_group_ratio(roll_slp14, 'TAMAN SRI SENTOSA UTARA') )
age_group14_dict_tssa = dict(age_group_ratio(roll_slp14, 'TAMAN SRI SENTOSA SELATAN') )

score_tba14 = score_slp14[score_slp14['NAMA DM']=='TAMAN BUKIT ANGKASA']
score_php14 = score_slp14[score_slp14['NAMA DM']=='PANTAI HILL PARK']
score_tssu14 = score_slp14[score_slp14['NAMA DM']=='TAMAN SRI SENTOSA UTARA']
score_tssa14 = score_slp14[score_slp14['NAMA DM']=='TAMAN SRI SENTOSA SELATAN']

tba_total_released_votes14 = get_released_vote_count(score_slp14 , "TAMAN BUKIT ANGKASA")
php_total_released_votes14 = get_released_vote_count(score_slp14 , "PANTAI HILL PARK")
tssu_total_released_votes14 = get_released_vote_count(score_slp14 , "TAMAN SRI SENTOSA UTARA")
tssa_total_released_votes14 = get_released_vote_count(score_slp14 , "TAMAN SRI SENTOSA SELATAN")

print('Total votes in Taman Bukit Angkasa in GE14: ', tba_total_released_votes14)
print('Total votes in Pantai Hill Park in GE14: ', php_total_released_votes14)
print('Total votes in Taman Sri Sentosa Utara in GE14: ', tssu_total_released_votes14)
print('Total votes in Taman Sri Sentosa Selatan in GE14: ', tssa_total_released_votes14)
#______________________________________________________________________________________________________________________________
age_group13_dict_tba = dict(age_group_ratio(roll_slp13, 'TAMAN BUKIT ANGKASA') )
age_group13_dict_php = dict(age_group_ratio(roll_slp13, 'PANTAI HILL PARK') )
age_group13_dict_tssu = dict(age_group_ratio(roll_slp13, 'TAMAN SRI SENTOSA UTARA') )
age_group13_dict_tssa = dict(age_group_ratio(roll_slp13, 'TAMAN SRI SENTOSA SELATAN') )

score_tba13 = score_slp13[score_slp13['NAMA DM']=='TAMAN BUKIT ANGKASA']
score_php13 = score_slp13[score_slp13['NAMA DM']=='PANTAI HILL PARK']
score_tssu13 = score_slp13[score_slp13['NAMA DM']=='TAMAN SRI SENTOSA UTARA']
score_tssa13 = score_slp13[score_slp13['NAMA DM']=='TAMAN SRI SENTOSA SELATAN']

tba_total_released_votes13 = get_released_vote_count(score_slp13 , "TAMAN BUKIT ANGKASA")
php_total_released_votes13 = get_released_vote_count(score_slp13 , "PANTAI HILL PARK")
tssu_total_released_votes13 = get_released_vote_count(score_slp13 , "TAMAN SRI SENTOSA UTARA")
tssa_total_released_votes13 = get_released_vote_count(score_slp13 , "TAMAN SRI SENTOSA SELATAN")

print('Total votes in Taman Bukit Angkasa in GE13: ', tba_total_released_votes13)
print('Total votes in Pantai Hill Park in GE13: ', php_total_released_votes13)
print('Total votes in Taman Sri Sentosa Utara in GE13: ', tssu_total_released_votes13)
print('Total votes in Taman Sri Sentosa Selatan in GE13: ', tssa_total_released_votes13)
#______________________________________________________________________________________________________________________________
f,ax = plt.subplots(2,2, figsize=(15,5))
pd.DataFrame({'GE13':age_group13_dict_tba}).join(pd.DataFrame({'GE14':age_group14_dict_tba})).plot.bar(ax=ax[0][0])
pd.DataFrame({'GE13':age_group13_dict_php}).join(pd.DataFrame({'GE14':age_group14_dict_php})).plot.bar(ax=ax[0][1])
pd.DataFrame({'GE13':age_group13_dict_tssu}).join(pd.DataFrame({'GE14':age_group14_dict_tssu})).plot.bar(ax=ax[1][0])
pd.DataFrame({'GE13':age_group13_dict_tssa}).join(pd.DataFrame({'GE14':age_group14_dict_tssu})).plot.bar(ax=ax[1][1])

ax[0][0].set_ylim(0,1)
ax[0][1].set_ylim(0,1)
ax[1][0].set_ylim(0,1)
ax[1][1].set_ylim(0,1)

ax[0][0].set_title('Taman Bukit Angkasa')
ax[0][1].set_title('Pantai Hill Park')
ax[1][0].set_title('Taman Sri Sentosa Utara')
ax[1][1].set_title('Taman Sri Sentosa Selatan')

plt.tight_layout()
plt.show()

#______________________________________________________________________________________________________________________________
slp_dict13 = {'TAMAN BUKIT ANGKASA':{'BN': score_tba13['Barisan Nasional '].sum() / tba_total_released_votes13,
                              'Pakatan':score_tba13['Pakatan Rakyat'].sum() / tba_total_released_votes13,
                               'Bebas':score_tba13['Bebas'].sum() / tba_total_released_votes13,
                                'UndiRosak':score_tba13['Rejected Votes'].sum() / tba_total_released_votes13,
                                'NorReturnedVote':score_tba13['BIL KERTAS UNDI YG TIDAK DIKEMBALIKAN (D)'].sum() / tba_total_released_votes13},
               'PANTAI HILL PARK':{'BN': score_php13['Barisan Nasional '].sum() / php_total_released_votes13,
                              'Pakatan':score_php13['Pakatan Rakyat'].sum() / php_total_released_votes13,
                               'Bebas':score_php13['Bebas'].sum() / php_total_released_votes13,
                                'UndiRosak':score_php13['Rejected Votes'].sum() / php_total_released_votes13,
                                'NorReturnedVote':score_php13['BIL KERTAS UNDI YG TIDAK DIKEMBALIKAN (D)'].sum() / php_total_released_votes13},
               'TAMAN SRI SENTOSA UTARA':{'BN': score_tssu13['Barisan Nasional '].sum() / tssu_total_released_votes13,
                              'Pakatan':score_tssu13['Pakatan Rakyat'].sum() / tssu_total_released_votes13,
                               'Bebas':score_tssu13['Bebas'].sum() / tssu_total_released_votes13,
                                'UndiRosak':score_tssu13['Rejected Votes'].sum() / tssu_total_released_votes13,
                                'NorReturnedVote':score_tssu13['BIL KERTAS UNDI YG TIDAK DIKEMBALIKAN (D)'].sum() / tssu_total_released_votes13},
               'TAMAN SRI SENTOSA SELATAN':{'BN': score_tssa13['Barisan Nasional '].sum() / tssa_total_released_votes13,
                              'Pakatan':score_tssa13['Pakatan Rakyat'].sum() / tssa_total_released_votes13,
                               'Bebas':score_tssa13['Bebas'].sum() / tssa_total_released_votes13,
                                'UndiRosak':score_tssa13['Rejected Votes'].sum() / tssa_total_released_votes13,
                                'NorReturnedVote':score_tssa13['BIL KERTAS UNDI YG TIDAK DIKEMBALIKAN (D)'].sum() / tssa_total_released_votes13}
                                }

slp_dict14 = {'TAMAN BUKIT ANGKASA':{'BN': score_tba14['Barisan Nasional '].sum() / tba_total_released_votes14,
                              'Pakatan':score_tba14['Pakatan Rakyat'].sum() / tba_total_released_votes14,
                               'PAS':score_tba14['PAS'].sum() / tba_total_released_votes14,
                                'UndiRosak':score_tba14['Rejected Votes'].sum() / tba_total_released_votes14,
                                'NorReturnedVote':score_tba14['BIL KERTAS UNDI YG TIDAK DIKEMBALIKAN (D)'].sum() / tba_total_released_votes14},
               'PANTAI HILL PARK':{'BN': score_php14['Barisan Nasional '].sum() / php_total_released_votes14,
                              'Pakatan':score_php14['Pakatan Rakyat'].sum() / php_total_released_votes14,
                               'PAS':score_php14['PAS'].sum() / php_total_released_votes14,
                                'UndiRosak':score_php14['Rejected Votes'].sum() / php_total_released_votes14,
                                'NorReturnedVote':score_php14['BIL KERTAS UNDI YG TIDAK DIKEMBALIKAN (D)'].sum() / php_total_released_votes14},
               'TAMAN SRI SENTOSA UTARA':{'BN': score_tssu14['Barisan Nasional '].sum() / tssu_total_released_votes14,
                              'Pakatan':score_tssu14['Pakatan Rakyat'].sum() / tssu_total_released_votes14,
                               'PAS':score_tssu14['PAS'].sum() / tssu_total_released_votes14,
                                'UndiRosak':score_tssu14['Rejected Votes'].sum() / tssu_total_released_votes14,
                                'NorReturnedVote':score_tssu14['BIL KERTAS UNDI YG TIDAK DIKEMBALIKAN (D)'].sum() / tssu_total_released_votes14},
               'TAMAN SRI SENTOSA SELATAN':{'BN': score_tssa14['Barisan Nasional '].sum() / tssa_total_released_votes14,
                              'Pakatan':score_tssa14['Pakatan Rakyat'].sum() / tssa_total_released_votes14,
                               'PAS':score_tssa14['PAS'].sum() / tssa_total_released_votes14,
                                'UndiRosak':score_tssa14['Rejected Votes'].sum() / tssa_total_released_votes14,
                                'NorReturnedVote':score_tssa14['BIL KERTAS UNDI YG TIDAK DIKEMBALIKAN (D)'].sum() / tssa_total_released_votes14}
                                }

tba13 = slp_dict13['TAMAN BUKIT ANGKASA']
tba14 = slp_dict14['TAMAN BUKIT ANGKASA']

php13 = slp_dict13['PANTAI HILL PARK']
php14 = slp_dict14['PANTAI HILL PARK']

tssu13 = slp_dict13['TAMAN SRI SENTOSA UTARA']
tssu14 = slp_dict14['TAMAN SRI SENTOSA UTARA']

tssa13 = slp_dict13['TAMAN SRI SENTOSA SELATAN']
tssa14 = slp_dict14['TAMAN SRI SENTOSA SELATAN']

tamanbukitangkasa = pd.DataFrame({'tamanbukitangkasa13':tba13, 'tamanbukitangkasa14':tba14})
pantaihillpark = pd.DataFrame({'pantaihillpark13':php13, 'pantaihillpark14':php14})
tamanssutara = pd.DataFrame({'tamanssutara13':tssu13, 'tamanssutara14':tssu14})
tamanssselatan = pd.DataFrame({'tamanssselatan13':tssa13, 'tamanssselatan14':tssa14})

tamanbukitangkasa.loc['Bebas','tamanbukitangkasa14'] = tamanbukitangkasa.loc['PAS','tamanbukitangkasa14']
tamanbukitangkasa.drop('PAS', inplace=True)
tamanbukitangkasa.index = ['BN', 'Bebas to PAS', 'NorReturnedVote', 'Pakatan', 'UndiRosak']

pantaihillpark.loc['Bebas','pantaihillpark14'] = pantaihillpark.loc['PAS','pantaihillpark14']
pantaihillpark.drop('PAS', inplace=True)
pantaihillpark.index = ['BN', 'Bebas to PAS', 'NorReturnedVote', 'Pakatan', 'UndiRosak']

tamanssutara.loc['Bebas','tamanssutara14'] = tamanssutara.loc['PAS','tamanssutara14']
tamanssutara.drop('PAS', inplace=True)
tamanssutara.index = ['BN', 'Bebas to PAS', 'NorReturnedVote', 'Pakatan', 'UndiRosak']

tamanssselatan.loc['Bebas','tamanssselatan14'] = tamanssselatan.loc['PAS','tamanssselatan14']
tamanssselatan.drop('PAS', inplace=True)
tamanssselatan.index = ['BN', 'Bebas to PAS', 'NorReturnedVote', 'Pakatan', 'UndiRosak']


dict_score_13_tamanbukitangkasa = {}
dict_score_13_tamanbukitangkasa.update({'BN':score_tba13['Barisan Nasional '].sum() / tba_total_released_votes13})
dict_score_13_tamanbukitangkasa.update({'Pakatan':score_tba13['Pakatan Rakyat'].sum() / tba_total_released_votes13})
dict_score_13_tamanbukitangkasa.update({'Bebas':score_tba13['Bebas'].sum() / tba_total_released_votes13})
dict_score_13_tamanbukitangkasa.update({'Rejected':score_tba13['Rejected Votes'].sum() / tba_total_released_votes13})
dict_score_13_tamanbukitangkasa.update({'NotReturned':score_tba13['BIL KERTAS UNDI YG TIDAK DIKEMBALIKAN (D)'].sum() / tba_total_released_votes13})

dict_score_13_pantaihillpark = {}
dict_score_13_pantaihillpark.update({'BN':score_php13['Barisan Nasional '].sum() / php_total_released_votes13})
dict_score_13_pantaihillpark.update({'Pakatan':score_php13['Pakatan Rakyat'].sum() / php_total_released_votes13})
dict_score_13_pantaihillpark.update({'Bebas':score_php13['Bebas'].sum() / php_total_released_votes13})
dict_score_13_pantaihillpark.update({'Rejected':score_php13['Rejected Votes'].sum() / php_total_released_votes13})
dict_score_13_pantaihillpark.update({'NotReturned':score_php13['BIL KERTAS UNDI YG TIDAK DIKEMBALIKAN (D)'].sum() / php_total_released_votes13})

dict_score_13_tamanssutara = {}
dict_score_13_tamanssutara.update({'BN':score_tssu13['Barisan Nasional '].sum() / tssu_total_released_votes13})
dict_score_13_tamanssutara.update({'Pakatan':score_tssu13['Pakatan Rakyat'].sum() / tssu_total_released_votes13})
dict_score_13_tamanssutara.update({'Bebas':score_tssu13['Bebas'].sum() / tssu_total_released_votes13})
dict_score_13_tamanssutara.update({'Rejected':score_tssu13['Rejected Votes'].sum() / tssu_total_released_votes13})
dict_score_13_tamanssutara.update({'NotReturned':score_tssu13['BIL KERTAS UNDI YG TIDAK DIKEMBALIKAN (D)'].sum() / tssu_total_released_votes13})

dict_score_13_tamanssselatan = {}
dict_score_13_tamanssselatan.update({'BN':score_tssa13['Barisan Nasional '].sum() / tssa_total_released_votes13})
dict_score_13_tamanssselatan.update({'Pakatan':score_tssa13['Pakatan Rakyat'].sum() / tssa_total_released_votes13})
dict_score_13_tamanssselatan.update({'Bebas':score_tssa13['Bebas'].sum() / tssa_total_released_votes13})
dict_score_13_tamanssselatan.update({'Rejected':score_tssa13['Rejected Votes'].sum() / tssa_total_released_votes13})
dict_score_13_tamanssselatan.update({'NotReturned':score_tssa13['BIL KERTAS UNDI YG TIDAK DIKEMBALIKAN (D)'].sum() / tssa_total_released_votes13})

dict_score_14_tamanbukitangkasa = {}
dict_score_14_tamanbukitangkasa.update({'BN':score_tba14['Barisan Nasional '].sum() / tba_total_released_votes14})
dict_score_14_tamanbukitangkasa.update({'Pakatan':score_tba14['Pakatan Rakyat'].sum() / tba_total_released_votes14})
dict_score_14_tamanbukitangkasa.update({'PAS':score_tba14['PAS'].sum() / tba_total_released_votes14})
dict_score_14_tamanbukitangkasa.update({'Rejected':score_tba14['Rejected Votes'].sum() / tba_total_released_votes14})
dict_score_14_tamanbukitangkasa.update({'NotReturned':score_tba14['BIL KERTAS UNDI YG TIDAK DIKEMBALIKAN (D)'].sum() / tba_total_released_votes14})

dict_score_14_pantaihillpark = {}
dict_score_14_pantaihillpark.update({'BN':score_php14['Barisan Nasional '].sum() / php_total_released_votes14})
dict_score_14_pantaihillpark.update({'Pakatan':score_php14['Pakatan Rakyat'].sum() / php_total_released_votes14})
dict_score_14_pantaihillpark.update({'PAS':score_php14['PAS'].sum() / php_total_released_votes14})
dict_score_14_pantaihillpark.update({'Rejected':score_php14['Rejected Votes'].sum() / php_total_released_votes14})
dict_score_14_pantaihillpark.update({'NotReturned':score_php14['BIL KERTAS UNDI YG TIDAK DIKEMBALIKAN (D)'].sum() / php_total_released_votes14})

dict_score_14_tamanssutara = {}
dict_score_14_tamanssutara.update({'BN':score_tssu14['Barisan Nasional '].sum() / tssu_total_released_votes14})
dict_score_14_tamanssutara.update({'Pakatan':score_tssu14['Pakatan Rakyat'].sum() / tssu_total_released_votes14})
dict_score_14_tamanssutara.update({'PAS':score_tssu14['PAS'].sum() / tssu_total_released_votes14})
dict_score_14_tamanssutara.update({'Rejected':score_tssu14['Rejected Votes'].sum() / tssu_total_released_votes14})
dict_score_14_tamanssutara.update({'NotReturned':score_tssu14['BIL KERTAS UNDI YG TIDAK DIKEMBALIKAN (D)'].sum() / tssu_total_released_votes14})

dict_score_14_tamanssselatan = {}
dict_score_14_tamanssselatan.update({'BN':score_tssa14['Barisan Nasional '].sum() / tssa_total_released_votes14})
dict_score_14_tamanssselatan.update({'Pakatan':score_tssa14['Pakatan Rakyat'].sum() / tssa_total_released_votes14})
dict_score_14_tamanssselatan.update({'PAS':score_tssa14['PAS'].sum() / tssa_total_released_votes14})
dict_score_14_tamanssselatan.update({'Rejected':score_tssa14['Rejected Votes'].sum() / tssa_total_released_votes14})
dict_score_14_tamanssselatan.update({'NotReturned':score_tssa14['BIL KERTAS UNDI YG TIDAK DIKEMBALIKAN (D)'].sum() / tssa_total_released_votes14})

df_tba_score = pd.DataFrame({'GE13':dict_score_13_tamanbukitangkasa}).join(pd.DataFrame({'GE14':dict_score_14_tamanbukitangkasa}), how='outer')

df_php_score = pd.DataFrame({'GE13':dict_score_13_pantaihillpark}).join(pd.DataFrame({'GE14':dict_score_14_pantaihillpark}), how='outer')

df_tssu_score = pd.DataFrame({'GE13':dict_score_13_tamanssutara}).join(pd.DataFrame({'GE14':dict_score_14_tamanssutara}), how='outer')

df_tssa_score = pd.DataFrame({'GE13':dict_score_13_tamanssselatan}).join(pd.DataFrame({'GE14':dict_score_14_tamanssselatan}), how='outer')


df_tba_score.loc['Bebas','GE14'] = df_tba_score.loc['PAS','GE14']
df_php_score.loc['Bebas','GE14'] = df_php_score.loc['PAS','GE14']
df_tssu_score.loc['Bebas','GE14'] = df_tssu_score.loc['PAS','GE14']
df_tssa_score.loc['Bebas','GE14'] = df_tssa_score.loc['PAS','GE14']

df_tba_score.drop('PAS', inplace=True)
df_php_score.drop('PAS', inplace=True)
df_tssu_score.drop('PAS', inplace=True)
df_tssa_score.drop('PAS', inplace=True)

df_tba_score.index = ['BN', 'Bebas->PAS', 'NotReturned', 'Pakatan', 'Rejected']
df_php_score.index = ['BN', 'Bebas->PAS', 'NotReturned', 'Pakatan', 'Rejected']
df_tssu_score.index = ['BN', 'Bebas->PAS', 'NotReturned', 'Pakatan', 'Rejected']
df_tssa_score.index = ['BN', 'Bebas->PAS', 'NotReturned', 'Pakatan', 'Rejected']


df_tba = pd.DataFrame({'GE13':{'BN':score_tba13['Barisan Nasional '].sum(),
								'Pakatan':score_tba13['Pakatan Rakyat'].sum(),
								'Bebas->PAS':score_tba13['Bebas'].sum(),
								'Rejected':score_tba13['Rejected Votes'].sum(),
								'NotReturned':score_tba13['BIL KERTAS UNDI YG TIDAK DIKEMBALIKAN (D)'].sum()} ,
					'GE14':{'BN':score_tba14['Barisan Nasional '].sum(),
								'Pakatan':score_tba14['Pakatan Rakyat'].sum(),
								'Bebas->PAS':score_tba14['PAS'].sum(),
								'Rejected':score_tba14['Rejected Votes'].sum(),
								'NotReturned':score_tba14['BIL KERTAS UNDI YG TIDAK DIKEMBALIKAN (D)'].sum()}})	

df_php = pd.DataFrame({'GE13':{'BN':score_php13['Barisan Nasional '].sum(),
							'Pakatan':score_php13['Pakatan Rakyat'].sum(),
							'Bebas->PAS':score_php13['Bebas'].sum(),
							'Rejected':score_php13['Rejected Votes'].sum(),
							'NotReturned':score_php13['BIL KERTAS UNDI YG TIDAK DIKEMBALIKAN (D)'].sum()} ,
					'GE14':{'BN':score_php14['Barisan Nasional '].sum(),
							'Pakatan':score_php14['Pakatan Rakyat'].sum(),
							'Bebas->PAS':score_php14['PAS'].sum(),
							'Rejected':score_php14['Rejected Votes'].sum(),
							'NotReturned':score_php14['BIL KERTAS UNDI YG TIDAK DIKEMBALIKAN (D)'].sum()}})

df_tssu = pd.DataFrame({'GE13':{'BN':score_tssu13['Barisan Nasional '].sum(),
							'Pakatan':score_tssu13['Pakatan Rakyat'].sum(),
							'Bebas->PAS':score_tssu13['Bebas'].sum(),
							'Rejected':score_tssu13['Rejected Votes'].sum(),
							'NotReturned':score_tssu13['BIL KERTAS UNDI YG TIDAK DIKEMBALIKAN (D)'].sum()} ,
					'GE14':{'BN':score_tssu14['Barisan Nasional '].sum(),
							'Pakatan':score_tssu14['Pakatan Rakyat'].sum(),
							'Bebas->PAS':score_tssu14['PAS'].sum(),
							'Rejected':score_tssu14['Rejected Votes'].sum(),
							'NotReturned':score_tssu14['BIL KERTAS UNDI YG TIDAK DIKEMBALIKAN (D)'].sum()}})

df_tssa = pd.DataFrame({'GE13':{'BN':score_tssa13['Barisan Nasional '].sum(),
							'Pakatan':score_tssa13['Pakatan Rakyat'].sum(),
							'Bebas->PAS':score_tssa13['Bebas'].sum(),
							'Rejected':score_tssa13['Rejected Votes'].sum(),
							'NotReturned':score_tssa13['BIL KERTAS UNDI YG TIDAK DIKEMBALIKAN (D)'].sum()} ,
					'GE14':{'BN':score_tssa14['Barisan Nasional '].sum(),
							'Pakatan':score_tssa14['Pakatan Rakyat'].sum(),
							'Bebas->PAS':score_tssa14['PAS'].sum(),
							'Rejected':score_tssa14['Rejected Votes'].sum(),
							'NotReturned':score_tssa14['BIL KERTAS UNDI YG TIDAK DIKEMBALIKAN (D)'].sum()}})
#_______________________________________________________________________________________________________________________________

f, ax = plt.subplots(2,2, figsize=(12,6))

p1 = df_tba.plot.bar(ax=ax[0][0])
p2 = df_php.plot.bar(ax=ax[0][1], sharey = p1)
p3 = df_tssu.plot.bar(ax=ax[1][0], sharey = p1)
p4 = df_tssa.plot.bar(ax=ax[1][1], sharey = p1)

plt.subplots_adjust(wspace = 0.02)

p1.set_title('Taman Bukit Angkasa (Vote count)')
p2.set_title('Pantai Hill Park(Vote count)')
p3.set_title('Taman Sri Sentosa Utara(Vote count)')
p4.set_title('Taman Sri Sentosa Selatan (Vote count)')

p1.set_ylim(0,max(roll_slp14['NamaDM'].value_counts()) )
p2.set_ylim(0,max(roll_slp14['NamaDM'].value_counts()) )
p3.set_ylim(0,max(roll_slp14['NamaDM'].value_counts()) )
p4.set_ylim(0,max(roll_slp14['NamaDM'].value_counts()) )

p1.legend().remove()
p2.legend().remove()
p3.legend().remove()
p4.legend().remove()

for patch in p1.patches:
	try:
		if patch.get_height()>0:
			p1.annotate(' %.0f' % patch.get_height(), xy=( patch.get_x() + patch.get_width()/2 ,patch.get_height()+ 100), ha='center',fontsize=9)
	except:
		pass
    
for patch in p2.patches:
    try:
        if patch.get_height()>0:
            p2.annotate(' %.0f' % patch.get_height(), xy=( patch.get_x() + patch.get_width()/2 ,patch.get_height()+100), ha='center',fontsize=9)
    except:
        pass
    
for patch in p3.patches:
    try:
        if patch.get_height()>0:
            p3.annotate(' %.0f' % patch.get_height(), xy=( patch.get_x() + patch.get_width()/2 ,patch.get_height()+100), ha='center',fontsize=9)
    except:
        pass

for patch in p4.patches:
    try:
        if patch.get_height()>0:
            p4.annotate(' %.0f' % patch.get_height(), xy=( patch.get_x() + patch.get_width()/2 ,patch.get_height()+100), ha='center',fontsize=9)
    except:
        pass
    
handles, labels = p1.get_legend_handles_labels()
plt.figlegend(handles,labels ,loc = 'lower center', ncol=2, bbox_to_anchor=[0.5, 0.])

plt.tight_layout()
plt.show()
