import pandas as pd
import numpy as np

url = 'https://docs.google.com/spreadsheets/d/1JkoTopkSk86Z2ru7wax9Dz7fJJxc4eJyQYrDG1IJkCc/export?format=csv&gid=1402886754'
register_df = pd.read_csv(url)

url = 'https://docs.google.com/spreadsheets/d/16zN1B_DIpAuCcywG5ScNnSZb-b50XA-xGavESKVKP5Q/export?format=csv&gid=0'
# url = 'https://docs.google.com/spreadsheets/d/1BD914GEplMKaS582_2gbLiia-sgjOrcUHXpSbfJi1KU/export?format=csv&gid=111784537'
awardee_df = pd.read_csv(url, error_bad_lines=False)

winning_teams_dict = {}

winning_teams_dict['MAG240M'] = [('ComeAgain', 0.7570), ('DSE-node', 0.7522), ('CogDL', 0.7506)]
winning_teams_dict['WikiKG90Mv2'] = [('wikiwiki', 0.2562), ('DNAKG', 0.2514), ('TIEG-Youpu', 0.2309)]
winning_teams_dict['PCQM4Mv2'] = [('WeLoveGraphs', 0.0719), ('ViSNet', 0.0723), ('NVIDIA-PCQM4Mv2', 0.0723)]

dataset_list = ['MAG240M', 'WikiKG90Mv2', 'PCQM4Mv2']

place2title = {1: '1st place', 2: '2nd place', 3: '3rd place'}
dataset2metric = {'MAG240M': 'accuracy', 'WikiKG90Mv2': 'MRR', 'PCQM4Mv2': 'MAE'}

for dataset in dataset_list:
    print('=======', dataset)
    place = 1

    print('##### **Winners**')

    for team, perf in winning_teams_dict[dataset]:
        
        # try:
        tf = np.logical_and(awardee_df['Dataset'] == dataset, awardee_df['Team name'] == team)
        # tf = np.logical_and(awardee_df['Ignore'] != awardee_df['Ignore'], tf)
        idx = tf.to_numpy().nonzero()[0]
        assert len(idx) == 1
        idx = idx[0]
        awardee_info = awardee_df.iloc[idx]
        # except:
        #     print(team)
        #     continue

        tf = np.logical_and(register_df['Dataset'] == dataset, register_df['Team name'] == team)
        tf = np.logical_and(register_df['Ignore'] != register_df['Ignore'], tf)
        idx = tf.to_numpy().nonzero()[0]
        assert len(idx) == 1
        idx = idx[0]

        contact = register_df['Email Address'][idx]
        name_list = []
        
        for i in range(1, 11):
            info = register_df[f'Team member ({i})'][idx]
            if info != info:
                break
            name = info.split(',')[0]
            aff = info.split(',')[1]
            name_list.append(f'{name} ({aff})')

        print(f"###### **{place2title[place]}: {team} ([contact](mailto:{awardee_info['メールアドレス']}))**")
        # print(f"###### **{place2title[place]}: {team}**")
         # [technical report]({awardee_info['Final paper link']}), [code]({awardee_info['Github']})
        print('- **Team members**: ' + ', '.join(name_list))
        print('- **Method**:', awardee_info['Method name'])
        print('- **Short summary**:', awardee_info['Method description'])
        print(f"- **Learn more: [Technical report](/paper/neurips2022/{dataset.lower()}_{team}.pdf), [code]({awardee_info['Github']})**")
        print(f'- **Test {dataset2metric[dataset]}**: {perf:.4f}')
        
        # print('Code:', awardee_info['Github'])

        print('')

        place += 1


