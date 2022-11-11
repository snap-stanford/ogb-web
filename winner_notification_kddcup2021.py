import pandas as pd
import numpy as np

url = 'https://docs.google.com/spreadsheets/d/1JEPvB62RJ1w15b4VAclWQcyNSOjrPVmBW68EyYT0Q00/export?format=csv&gid=1188631267'
register_df = pd.read_csv(url)

url = 'https://docs.google.com/spreadsheets/d/1BD914GEplMKaS582_2gbLiia-sgjOrcUHXpSbfJi1KU/export?format=csv&gid=111784537'
awardee_df = pd.read_csv(url)

winning_teams_dict = {}

winning_teams_dict['MAG240M-LSC'] = [('BD-PGL', 0.7549), ('Academic', 0.7519), ('Synerise AI', 0.7460), ('Topology_mag', 0.7447), ('passages', 0.7381), ('DeeperBiggerBetter', 0.7353)]
winning_teams_dict['WikiKG90M-LSC'] = [('BD-PGL', 0.9727), ('OhMyGod', 0.9712), ('GraphMIRAcles', 0.9707), ('littleant', 0.9511), ('vcdbro', 0.9489), ('JohnZheng', 0.9465)]
winning_teams_dict['PCQM4M-LSC'] = [('MachineLearning', 0.1200), ('SuperHelix', 0.1204), ('Quantum', 0.1205), ('DIVE@TAMU', 0.1235), ('no_free_lunch', 0.1244), ('GNNLearner', 0.1253)]

dataset_list = ['MAG240M-LSC', 'WikiKG90M-LSC', 'PCQM4M-LSC']

place2title = {1: '1st place', 2: '2nd place', 3: '3rd place', 4: '4th place', 5: '5th place', 6: '6th place'}
dataset2metric = {'MAG240M-LSC': 'accuracy', 'WikiKG90M-LSC': 'MRR', 'PCQM4M-LSC': 'MAE'}

for dataset in dataset_list:
    print('=======', dataset)
    place = 1

    print('##### **Winners**')

    for team, perf in winning_teams_dict[dataset]:
        
        try:
            tf = np.logical_and(awardee_df['Dataset'] == dataset, awardee_df['Team name'] == team)
            tf = np.logical_and(awardee_df['Ignore'] != awardee_df['Ignore'], tf)
            idx = tf.to_numpy().nonzero()[0]
            assert len(idx) == 1
            idx = idx[0]
            awardee_info = awardee_df.iloc[idx]
        except:
            # print(team)
            continue

        if place == 4:
            print('##### **Runner-ups**')

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
         # [technical report]({awardee_info['Final paper link']}), [code]({awardee_info['Github']})
        print('- **Team members**: ' + ', '.join(name_list))
        print('- **Method**:', awardee_info['Method name'])
        print('- **Short summary**:', awardee_info['Method description'])
        print(f"- **Learn more: [Technical report]({awardee_info['Final paper link']}), [code]({awardee_info['Github']})**")
        print(f'- **Test {dataset2metric[dataset]}**: {perf:.4f}')
        
        # print('Code:', awardee_info['Github'])
        # print('Technical report:', awardee_info['Technical report'])

        print('')

        place += 1


