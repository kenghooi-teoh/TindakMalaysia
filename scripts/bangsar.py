import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from analysis import *

# VOTERS
roll14 = pd.read_csv('Lembah Pantai GE14 Roll.csv')
roll13 = pd.read_csv('Lembah Pantai GE13 Roll.csv')

# SCORE
score_bangsar = pd.read_excel('results.xlsx', sheetname='Bangsar')
score_bangsar14 = score_bangsar[score_bangsar['GE'] == 'GE14']
score_bangsar13 = score_bangsar[score_bangsar['GE'] == 'GE13']


#______________________________________________________________________________________________________________________________

roll_bangsar14 = roll14[(roll14['NamaDM']=='BANGSAR BARU') | (roll14['NamaDM']=='TAMAN LUCKY') |(roll14['NamaDM']=='JALAN MAAROF')]
roll_bangsar13 = roll13[(roll13['NamaDM']=='BANGSAR BARU') | (roll13['NamaDM']=='TAMAN LUCKY') |(roll13['NamaDM']=='JALAN MAAROF')]

def calculate_age(born):
    electionday = pd.to_datetime('2018-05-09')
    return electionday.year - born.year - ((electionday.month, electionday.day) < (born.month, born.day))

roll_bangsar14['Age'] = pd.to_datetime(roll_bangsar14['TahunLahir']).apply(lambda x: calculate_age(x))
max_age = max(roll_bangsar14['Age'].max(),roll_bangsar13['Umur'].max())

roll_bangsar14['AgeGroup'] = pd.cut(roll_bangsar14['Age'], [20,30,40,50,60,70,80,max_age] )
roll_bangsar13['AgeGroup'] = pd.cut(roll_bangsar13['Umur'], bins=[20,30,40,50,60,70,80,max_age])

#______________________________________________________________________________________________________________________________
age_group14_dict_bangsarbaru = dict(age_group_ratio(roll_bangsar14, 'BANGSAR BARU') )
age_group14_dict_jlnmaarof = dict(age_group_ratio(roll_bangsar14, 'JALAN MAAROF') )
age_group14_dict_tmnlucky = dict(age_group_ratio(roll_bangsar14, 'TAMAN LUCKY') )

score_bangsarbaru14 = score_bangsar14[score_bangsar14['NAMA DM']=='BANGSAR BARU']
score_jlnmaarof14 = score_bangsar14[score_bangsar14['NAMA DM']=='JALAN MAAROF']
score_tmnlucky14 = score_bangsar14[score_bangsar14['NAMA DM']=='TAMAN LUCKY']

bangsarbaru_total_released_votes14 = get_released_vote_count(score_bangsar14 , "BANGSAR BARU")
jlnmaarof_total_released_votes14 = get_released_vote_count(score_bangsar14 , "JALAN MAAROF")
tmnlucky_total_released_votes14 = get_released_vote_count(score_bangsar14 , "TAMAN LUCKY")

print('Total votes in Bangsar Baru in GE14: ', bangsarbaru_total_released_votes14)
print('Total votes in Jalan Maarof in GE14: ', jlnmaarof_total_released_votes14)
print('Total votes in Taman Lucky in GE14: ', tmnlucky_total_released_votes14)

#______________________________________________________________________________________________________________________________
age_group13_dict_bangsarbaru = dict(age_group_ratio(roll_bangsar13, 'BANGSAR BARU') )
age_group13_dict_jlnmaarof = dict(age_group_ratio(roll_bangsar13, 'JALAN MAAROF') )
age_group13_dict_tmnlucky = dict(age_group_ratio(roll_bangsar13, 'TAMAN LUCKY') )

score_bangsarbaru13= score_bangsar13[score_bangsar13['NAMA DM']=='BANGSAR BARU']
score_jlnmaarof13 = score_bangsar13[score_bangsar13['NAMA DM']=='JALAN MAAROF']
score_tmnlucky13 = score_bangsar13[score_bangsar13['NAMA DM']=='TAMAN LUCKY']

bangsarbaru_total_released_votes13 = get_released_vote_count(score_bangsar13 , "BANGSAR BARU")
jlnmaarof_total_released_votes13 = get_released_vote_count(score_bangsar13 , "JALAN MAAROF")
tmnlucky_total_released_votes13 = get_released_vote_count(score_bangsar13 , "TAMAN LUCKY")

print('Total votes in Bangsar Baru in GE13: ', bangsarbaru_total_released_votes13)
print('Total votes in Jalan Maarof in GE13: ', jlnmaarof_total_released_votes13)
print('Total votes in Taman Lucky in GE13: ', tmnlucky_total_released_votes13)

#______________________________________________________________________________________________________________________________
f,ax = plt.subplots(1,3, figsize=(15,5))
pd.DataFrame({'GE13':age_group13_dict_bangsarbaru}).join(pd.DataFrame({'GE14':age_group14_dict_bangsarbaru})).plot.bar(ax=ax[0])
pd.DataFrame({'GE13':age_group13_dict_jlnmaarof}).join(pd.DataFrame({'GE14':age_group14_dict_jlnmaarof})).plot.bar(ax=ax[1])
pd.DataFrame({'GE13':age_group13_dict_tmnlucky}).join(pd.DataFrame({'GE14':age_group14_dict_tmnlucky})).plot.bar(ax=ax[2])

ax[0].set_ylim(0,1)
ax[1].set_ylim(0,1)
ax[2].set_ylim(0,1)

ax[0].set_title('Bangsar Baru')
ax[1].set_title('Jalan Maarof')
ax[2].set_title('Taman Lucky')

plt.show()

#______________________________________________________________________________________________________________________________
bangsar_dict13 = {'JALAN MAAROF':{'BN': score_jlnmaarof13['Barisan Nasional '].sum() / jlnmaarof_total_released_votes13,
                              'Pakatan':score_jlnmaarof13['Pakatan Rakyat'].sum() / jlnmaarof_total_released_votes13,
                               'Bebas':score_jlnmaarof13['Bebas'].sum() / jlnmaarof_total_released_votes13,
                                'UndiRosak':score_jlnmaarof13['Rejected Votes'].sum() / jlnmaarof_total_released_votes13,
                                'NorReturnedVote':score_jlnmaarof13['BIL KERTAS UNDI YG TIDAK DIKEMBALIKAN (D)'].sum() / bangsarbaru_total_released_votes13},
               'BANGSAR BARU':{'BN': score_bangsarbaru13['Barisan Nasional '].sum() / bangsarbaru_total_released_votes13,
                              'Pakatan':score_bangsarbaru13['Pakatan Rakyat'].sum() / bangsarbaru_total_released_votes13,
                               'Bebas':score_bangsarbaru13['Bebas'].sum() / bangsarbaru_total_released_votes13,
                                'UndiRosak':score_bangsarbaru13['Rejected Votes'].sum() / bangsarbaru_total_released_votes13,
                                'NorReturnedVote':score_bangsarbaru13['BIL KERTAS UNDI YG TIDAK DIKEMBALIKAN (D)'].sum() / jlnmaarof_total_released_votes13},
               'TAMAN LUCKY':{'BN': score_tmnlucky13['Barisan Nasional '].sum() / tmnlucky_total_released_votes13,
                              'Pakatan':score_tmnlucky13['Pakatan Rakyat'].sum() / tmnlucky_total_released_votes13,
                               'Bebas':score_tmnlucky13['Bebas'].sum() / tmnlucky_total_released_votes13,
                                'UndiRosak':score_tmnlucky13['Rejected Votes'].sum() / tmnlucky_total_released_votes13,
                                'NorReturnedVote':score_tmnlucky13['BIL KERTAS UNDI YG TIDAK DIKEMBALIKAN (D)'].sum() / tmnlucky_total_released_votes13}}

bangsar_dict14 = {'JALAN MAAROF':{'BN': score_jlnmaarof14['Barisan Nasional '].sum() / jlnmaarof_total_released_votes14,
                              'Pakatan':score_jlnmaarof14['Pakatan Rakyat'].sum() / jlnmaarof_total_released_votes14,
                               'PAS':score_jlnmaarof14['PAS'].sum() / jlnmaarof_total_released_votes14,
                                'UndiRosak':score_jlnmaarof14['Rejected Votes'].sum() / jlnmaarof_total_released_votes14,
                                'NorReturnedVote':score_jlnmaarof14['BIL KERTAS UNDI YG TIDAK DIKEMBALIKAN (D)'].sum() / jlnmaarof_total_released_votes14},
               'BANGSAR BARU':{'BN': score_bangsarbaru14['Barisan Nasional '].sum() / bangsarbaru_total_released_votes14,
                              'Pakatan':score_bangsarbaru14['Pakatan Rakyat'].sum() / bangsarbaru_total_released_votes14,
                               'PAS':score_bangsarbaru14['PAS'].sum() / bangsarbaru_total_released_votes14,
                                'UndiRosak':score_bangsarbaru14['Rejected Votes'].sum() / bangsarbaru_total_released_votes14,
                                'NorReturnedVote':score_bangsarbaru14['BIL KERTAS UNDI YG TIDAK DIKEMBALIKAN (D)'].sum() / jlnmaarof_total_released_votes13},
               'TAMAN LUCKY':{'BN': score_tmnlucky14['Barisan Nasional '].sum() / tmnlucky_total_released_votes14,
                              'Pakatan':score_tmnlucky14['Pakatan Rakyat'].sum() / tmnlucky_total_released_votes14,
                               'PAS':score_tmnlucky14['PAS'].sum() / tmnlucky_total_released_votes14,
                                'UndiRosak':score_tmnlucky14['Rejected Votes'].sum() / tmnlucky_total_released_votes14,
                                'NorReturnedVote':score_tmnlucky14['BIL KERTAS UNDI YG TIDAK DIKEMBALIKAN (D)'].sum() / tmnlucky_total_released_votes14}}


bb13 = bangsar_dict13['BANGSAR BARU']
bb14 = bangsar_dict14['BANGSAR BARU']

tl13 = bangsar_dict13['TAMAN LUCKY']
tl14 = bangsar_dict14['TAMAN LUCKY']

jm13 = bangsar_dict13['JALAN MAAROF']
jm14 = bangsar_dict14['JALAN MAAROF']

bangsarbaru = pd.DataFrame({'bangsarbaru13':bb13, 'bangsarbaru14':bb14})
jalanmaarof = pd.DataFrame({'jalanmaarof13':jm13, 'jalanmaarof14':jm14})
tamanlucky = pd.DataFrame({'tamanlucky13':tl13, 'tamanlucky14':tl14})

bangsarbaru.loc['Bebas','bangsarbaru14'] = bangsarbaru.loc['PAS','bangsarbaru14']
bangsarbaru.drop('PAS', inplace=True)
bangsarbaru.index = ['BN', 'Bebas to PAS', 'NorReturnedVote', 'Pakatan', 'UndiRosak']

jalanmaarof.loc['Bebas','jalanmaarof14'] = jalanmaarof.loc['PAS','jalanmaarof14']
jalanmaarof.drop('PAS', inplace=True)
jalanmaarof.index = ['BN', 'Bebas to PAS', 'NorReturnedVote', 'Pakatan', 'UndiRosak']

tamanlucky.loc['Bebas','tamanlucky14'] = tamanlucky.loc['PAS','tamanlucky14']
tamanlucky.drop('PAS', inplace=True)
tamanlucky.index = ['BN', 'Bebas to PAS', 'NorReturnedVote', 'Pakatan', 'UndiRosak']

dict_score_13_bangsarbaru = {}
dict_score_13_bangsarbaru.update({'BN':score_bangsarbaru13['Barisan Nasional '].sum() / bangsarbaru_total_released_votes13})
dict_score_13_bangsarbaru.update({'Pakatan':score_bangsarbaru13['Pakatan Rakyat'].sum() / bangsarbaru_total_released_votes13})
dict_score_13_bangsarbaru.update({'Bebas':score_bangsarbaru13['Bebas'].sum() / bangsarbaru_total_released_votes13})
dict_score_13_bangsarbaru.update({'Rejected':score_bangsarbaru13['Rejected Votes'].sum() / bangsarbaru_total_released_votes13})
dict_score_13_bangsarbaru.update({'NotReturned':score_bangsarbaru13['BIL KERTAS UNDI YG TIDAK DIKEMBALIKAN (D)'].sum() / bangsarbaru_total_released_votes13})

dict_score_13_jlnmaarof = {}
dict_score_13_jlnmaarof.update({'BN':score_jlnmaarof13['Barisan Nasional '].sum() / jlnmaarof_total_released_votes13})
dict_score_13_jlnmaarof.update({'Pakatan':score_jlnmaarof13['Pakatan Rakyat'].sum() / jlnmaarof_total_released_votes13})
dict_score_13_jlnmaarof.update({'Bebas':score_jlnmaarof13['Bebas'].sum() / jlnmaarof_total_released_votes13})
dict_score_13_jlnmaarof.update({'Rejected':score_jlnmaarof13['Rejected Votes'].sum() / jlnmaarof_total_released_votes13})
dict_score_13_jlnmaarof.update({'NotReturned':score_jlnmaarof13['BIL KERTAS UNDI YG TIDAK DIKEMBALIKAN (D)'].sum() / jlnmaarof_total_released_votes13})

dict_score_13_tmnlucky = {}
dict_score_13_tmnlucky.update({'BN':score_tmnlucky13['Barisan Nasional '].sum() / tmnlucky_total_released_votes13})
dict_score_13_tmnlucky.update({'Pakatan':score_tmnlucky13['Pakatan Rakyat'].sum() / tmnlucky_total_released_votes13})
dict_score_13_tmnlucky.update({'Bebas':score_tmnlucky13['Bebas'].sum() / tmnlucky_total_released_votes13})
dict_score_13_tmnlucky.update({'Rejected':score_tmnlucky13['Rejected Votes'].sum() / tmnlucky_total_released_votes13})
dict_score_13_tmnlucky.update({'NotReturned':score_tmnlucky13['BIL KERTAS UNDI YG TIDAK DIKEMBALIKAN (D)'].sum() / tmnlucky_total_released_votes13})

dict_score_14_bangsarbaru = {}
dict_score_14_bangsarbaru.update({'BN':score_bangsarbaru14['Barisan Nasional '].sum() / bangsarbaru_total_released_votes14})
dict_score_14_bangsarbaru.update({'Pakatan':score_bangsarbaru14['Pakatan Rakyat'].sum() / bangsarbaru_total_released_votes14})
dict_score_14_bangsarbaru.update({'PAS':score_bangsarbaru14['PAS'].sum() / bangsarbaru_total_released_votes14})
dict_score_14_bangsarbaru.update({'Rejected':score_bangsarbaru14['Rejected Votes'].sum() / bangsarbaru_total_released_votes14})
dict_score_14_bangsarbaru.update({'NotReturned':score_bangsarbaru14['BIL KERTAS UNDI YG TIDAK DIKEMBALIKAN (D)'].sum() / bangsarbaru_total_released_votes14})

dict_score_14_jlnmaarof = {}
dict_score_14_jlnmaarof.update({'BN':score_jlnmaarof14['Barisan Nasional '].sum() / jlnmaarof_total_released_votes14})
dict_score_14_jlnmaarof.update({'Pakatan':score_jlnmaarof14['Pakatan Rakyat'].sum() / jlnmaarof_total_released_votes14})
dict_score_14_jlnmaarof.update({'PAS':score_jlnmaarof14['PAS'].sum() / jlnmaarof_total_released_votes14})
dict_score_14_jlnmaarof.update({'Rejected':score_jlnmaarof14['Rejected Votes'].sum() / jlnmaarof_total_released_votes14})
dict_score_14_jlnmaarof.update({'NotReturned':score_jlnmaarof14['BIL KERTAS UNDI YG TIDAK DIKEMBALIKAN (D)'].sum() / jlnmaarof_total_released_votes14})

dict_score_14_tmnlucky = {}
dict_score_14_tmnlucky.update({'BN':score_tmnlucky14['Barisan Nasional '].sum() / tmnlucky_total_released_votes14})
dict_score_14_tmnlucky.update({'Pakatan':score_tmnlucky14['Pakatan Rakyat'].sum() / tmnlucky_total_released_votes14})
dict_score_14_tmnlucky.update({'PAS':score_tmnlucky14['PAS'].sum() / tmnlucky_total_released_votes14})
dict_score_14_tmnlucky.update({'Rejected':score_tmnlucky14['Rejected Votes'].sum() / tmnlucky_total_released_votes14})
dict_score_14_tmnlucky.update({'NotReturned':score_tmnlucky14['BIL KERTAS UNDI YG TIDAK DIKEMBALIKAN (D)'].sum() / tmnlucky_total_released_votes14})


df_bb_score = pd.DataFrame({'GE13':dict_score_13_bangsarbaru})\
.join(pd.DataFrame({'GE14':dict_score_14_bangsarbaru}), how='outer')

df_jm_score = pd.DataFrame({'GE13':dict_score_13_jlnmaarof})\
.join(pd.DataFrame({'GE14':dict_score_14_jlnmaarof}), how='outer')

df_tl_score = pd.DataFrame({'GE13':dict_score_13_tmnlucky})\
.join(pd.DataFrame({'GE14':dict_score_14_tmnlucky}), how='outer')

df_bb_score.loc['Bebas','GE14'] = df_bb_score.loc['PAS','GE14']
df_jm_score.loc['Bebas','GE14'] = df_jm_score.loc['PAS','GE14']
df_tl_score.loc['Bebas','GE14'] = df_tl_score.loc['PAS','GE14']

df_bb_score.drop('PAS', inplace=True)
df_jm_score.drop('PAS', inplace=True)
df_tl_score.drop('PAS', inplace=True)

df_bb_score.index = ['BN', 'Bebas->PAS', 'NotReturned', 'Pakatan', 'Rejected']
df_jm_score.index = ['BN', 'Bebas->PAS', 'NotReturned', 'Pakatan', 'Rejected']
df_tl_score.index = ['BN', 'Bebas->PAS', 'NotReturned', 'Pakatan', 'Rejected']

df_jm = pd.DataFrame({'GE13':{'BN':score_jlnmaarof13['Barisan Nasional '].sum(),
'Pakatan':score_jlnmaarof13['Pakatan Rakyat'].sum(),
'Bebas->PAS':score_jlnmaarof13['Bebas'].sum(),
'Rejected':score_jlnmaarof13['Rejected Votes'].sum(),
'NotReturned':score_jlnmaarof13['BIL KERTAS UNDI YG TIDAK DIKEMBALIKAN (D)'].sum()} ,
             'GE14':{'BN':score_jlnmaarof14['Barisan Nasional '].sum(),
'Pakatan':score_jlnmaarof14['Pakatan Rakyat'].sum(),
'Bebas->PAS':score_jlnmaarof14['PAS'].sum(),
'Rejected':score_jlnmaarof14['Rejected Votes'].sum(),
'NotReturned':score_jlnmaarof14['BIL KERTAS UNDI YG TIDAK DIKEMBALIKAN (D)'].sum()}})

df_tl = pd.DataFrame({'GE13':{'BN':score_tmnlucky13['Barisan Nasional '].sum(),
'Pakatan':score_tmnlucky13['Pakatan Rakyat'].sum(),
'Bebas->PAS':score_tmnlucky13['Bebas'].sum(),
'Rejected':score_tmnlucky13['Rejected Votes'].sum(),
'NotReturned':score_tmnlucky13['BIL KERTAS UNDI YG TIDAK DIKEMBALIKAN (D)'].sum()} ,
             'GE14':{'BN':score_tmnlucky14['Barisan Nasional '].sum(),
'Pakatan':score_tmnlucky14['Pakatan Rakyat'].sum(),
'Bebas->PAS':score_tmnlucky14['PAS'].sum(),
'Rejected':score_tmnlucky14['Rejected Votes'].sum(),
'NotReturned':score_tmnlucky14['BIL KERTAS UNDI YG TIDAK DIKEMBALIKAN (D)'].sum()}})

df_bb = pd.DataFrame({'GE13':{'BN':score_bangsarbaru13['Barisan Nasional '].sum(),
'Pakatan':score_bangsarbaru13['Pakatan Rakyat'].sum(),
'Bebas->PAS':score_bangsarbaru13['Bebas'].sum(),
'Rejected':score_bangsarbaru13['Rejected Votes'].sum(),
'NotReturned':score_bangsarbaru13['BIL KERTAS UNDI YG TIDAK DIKEMBALIKAN (D)'].sum()} ,
             'GE14':{'BN':score_bangsarbaru14['Barisan Nasional '].sum(),
'Pakatan':score_bangsarbaru14['Pakatan Rakyat'].sum(),
'Bebas->PAS':score_bangsarbaru14['PAS'].sum(),
'Rejected':score_bangsarbaru14['Rejected Votes'].sum(),
'NotReturned':score_bangsarbaru14['BIL KERTAS UNDI YG TIDAK DIKEMBALIKAN (D)'].sum()}})

#_______________________________________________________________________________________________________________________________

f, ax = plt.subplots(1,3, figsize=(12,3))

p1 = df_bb.plot.bar(ax=ax[0])
p2 = df_jm.plot.bar(ax=ax[1], sharey = p1)
p3 = df_tl.plot.bar(ax=ax[2], sharey = p1)

plt.subplots_adjust(wspace = 0.02)

p1.set_title('Bangsar Baru (Vote count)')
p2.set_title('Jalan Maarof (Vote count)')
p3.set_title('Taman Lucky (Vote count)')

p1.set_ylim(0,max(roll_bangsar14['NamaDM'].value_counts()) )
p2.set_ylim(0,max(roll_bangsar14['NamaDM'].value_counts()) )
p3.set_ylim(0,max(roll_bangsar14['NamaDM'].value_counts()) )

p1.legend().remove()
p2.legend().remove()
p3.legend().remove()

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
    
handles, labels = p1.get_legend_handles_labels()
plt.figlegend(handles,labels ,loc = 'lower center', ncol=2, bbox_to_anchor=[0.5, 0.])

plt.tight_layout()
plt.show()





