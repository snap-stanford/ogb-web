import pandas as pd 
import numpy as np
import os

nodeprop_dataset_list = ['ogbn-proteins', 'ogbn-products']
linkprop_dataset_list = ['ogbl-ppa', 'ogbl-reviews']
graphprop_mol_dataset_list = ['ogbg-mol-tox21', 'ogbg-mol-hiv', 'ogbg-mol-muv', 'ogbg-mol-esol', 'ogbg-mol-lipo', 'ogbg-mol-freesolv']
graphprop_other_dataset_list = []

dataset2metric = {'ogbn-proteins': 'ROC-AUC', 'ogbn-products': 'Accuracy', 'ogbl-ppa': 'ROC-AUC', 'ogbl-reviews': 'RMSE', 'ogbg-mol-tox21': 'ROC-AUC', 'ogbg-mol-hiv': 'ROC-AUC', 'ogbg-mol-muv': 'ROC-AUC', 'ogbg-mol-esol': 'RMSE', 'ogbg-mol-lipo': 'RMSE', 'ogbg-mol-freesolv': 'RMSE'}

task_question = 'On which kind of task do you want to report the performance?'

### relevant columns that will be used
relevant_column = ['Timestamp', 'Method name', 'Primary email contact', 'Github repository', 'Paper']

month_dict = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}

def round_float(num):
    return round(num*10000)/10000

def convert_date_to_str(date):
    # '2/8/2020 23:07:08' -> 'Feb 8, 2020'
    temp = date.split(' ')[0]
    splitted = temp.split('/')
    month = month_dict[int(splitted[0])]
    day = int(splitted[1])
    year = int(splitted[2])
    return '{} {}, {}'.format(month, day, year)

def get_default_leaderboard(dataset, valid_submission_list, metric = 'ROC-AUC'):
    avg_list = []
    std_list = []
    for perfo in [info[dataset] for info in valid_submission_list]:
        if isinstance(perfo, str):
            splitted = perfo.split(',')
            avg_list.append(round_float(float(splitted[0])))
            std_list.append(round_float(float(splitted[1])))
        else:
            avg_list.append(perfo)
            std_list.append(perfo)

    avg_list = np.array(avg_list)

    if metric == 'ROC-AUC' or metric == 'Accuracy':
        ## from large to small
        sorted_ind_list = np.argsort(-avg_list)
    elif metric == 'RMSE':
        ## from small to large
        sorted_ind_list = np.argsort(avg_list)

    header = '| Rank  | Method | {} | References | Date \n'.format(metric)
    header += '|:----:|:-----:|:------:|:-----:|:-----:|\n'

    current_ranking = 1

    for i, ind in enumerate(sorted_ind_list):
        info = valid_submission_list[ind]
        
        if not np.isnan(avg_list[ind]):
            header += '|  {}  |  {}  | {:.4f} ± {:.4f}   | [Contact](mailto:{}), [Paper]({}), [Code]({}) | {} | \n'.\
                       format(current_ranking, info['Method name'], avg_list[ind], std_list[ind], info['Primary email contact'], info['Paper'], info['Github repository'], convert_date_to_str(info['Timestamp']))
        else:
            header += '|  {} |  {}  | Not Submitted | [Contact](mailto:{}), [Paper]({}), [Code]({}) | {} | \n'.\
                       format(current_ranking, info['Method name'], info['Primary email contact'], info['Paper'], info['Github repository'], convert_date_to_str(info['Timestamp']))

        if i < len(sorted_ind_list) - 1 and avg_list[ind] != avg_list[sorted_ind_list[i+1]]:
            current_ranking += 1

    return header


def get_mol_leaderboard(valid_submission_list):

    ### for classification

    # metric = 'ROC-AUC'
    # mol_dataset_list = graphprop_mol_dataset_list[:3]

    leaderboard_list = []

    for metric, mol_dataset_list in zip(['ROC-AUC', 'RMSE'], [graphprop_mol_dataset_list[:3], graphprop_mol_dataset_list[3:]]):
        avg_mat = []
        std_mat = []
        for dataset in mol_dataset_list:
            avg_list = []
            std_list = []
            for perfo in [info[dataset] for info in valid_submission_list]:
                if isinstance(perfo, str):
                    splitted = perfo.split(',')
                    avg_list.append(float(splitted[0]))
                    std_list.append(float(splitted[1]))
                else:
                    avg_list.append(perfo)
                    std_list.append(perfo)
            avg_mat.append(avg_list)
            std_mat.append(std_list)

        total_avg_list = np.average(np.array(avg_mat), axis = 0) ## average across all datasets
        for i in range(len(total_avg_list)):
            total_avg_list[i] = round_float(total_avg_list[i])

        if metric == 'ROC-AUC' or metric == 'Accuracy':
            ## from large to small
            sorted_ind_list = np.argsort(-total_avg_list)
        elif metric == 'RMSE':
            ## from small to large
            sorted_ind_list = np.argsort(total_avg_list)

        header = '| Rank |  Method |  {} | {} | {} | {} | References | Date | \n'.format('Averaged ' + metric, mol_dataset_list[0], mol_dataset_list[1], mol_dataset_list[2])
        header += '|:----:|:------:|:-----:|:------:|:-----:|:-----:|:-----:|:-----:|\n'

        current_ranking = 1

        for i, ind in enumerate(sorted_ind_list):
            info = valid_submission_list[ind]
            
            if not np.isnan(total_avg_list[ind]):
                header += '|  {}  | {} | {:.4f} ± {:.4f}  | {:.4f} ± {:.4f}  | {:.4f} ± {:.4f}  | {:.4f}|  [Contact](mailto:{}), [Paper]({}), [Code]({}) |  {}  |\n'.\
                           format(current_ranking, info['Method name'], round_float(avg_mat[0][ind]), round_float(std_mat[0][ind]), round_float(avg_mat[1][ind]), round_float(std_mat[1][ind]), round_float(avg_mat[2][ind]), round_float(std_mat[2][ind]), total_avg_list[ind], 
                            info['Primary email contact'], info['Paper'], info['Github repository'], convert_date_to_str(info['Timestamp']))
            else:
                header += '|  {}  | {} | Not Submitted  | Not Submitted  | Not Submitted  | Not Submitted  |  [Contact](mailto:{}), [Paper]({}), [Code]({}) |  {}  |\n'.\
                           format(current_ranking, info['Method name'], info['Primary email contact'], info['Paper'], info['Github repository'], convert_date_to_str(info['Timestamp']))

            if i < len(sorted_ind_list) - 1 and total_avg_list[ind] != total_avg_list[sorted_ind_list[i+1]]:
                current_ranking += 1

        leaderboard_list.append(header)

    return {'ogbg-mol-cls': leaderboard_list[0], 'ogbg-mol-reg': leaderboard_list[1]}


def insert_leaderboard(source_file, dest_file, leaderboard_dict):
    PATH = '_docs/leaderboard'
    with open(os.path.join(PATH, source_file), 'r') as f:
        source = f.read().split('\n')

    dest = []
    for line in source:
        ### line = '#ogbg-mol-cls'
        ### line[1:] = 'ogbg-mol-cls'
        if line[1:] in leaderboard_dict:
            dest.append(leaderboard_dict[line[1:]])
        else:
            dest.append(line)

    with open(os.path.join(PATH, dest_file), 'w') as f:
        f.write('\n'.join(dest))


if __name__ == '__main__':
    url = 'https://docs.google.com/spreadsheets/d/1m9NWfmzxNqoNhX46LGbFLk7NPHWrBSVa73WKP4ObpTQ/export?format=csv&gid=155379025'
    df = pd.read_csv(url)

    graphprop_valid_submission_list = []
    nodeprop_valid_submission_list = []
    linkprop_valid_submission_list = []

    for index, row in df.iterrows():
        ### only consider the approved entry
        if row['Approved'] == 'Y':
            if row[task_question] == 'Node Property Prediction':
                if any([isinstance(row[col], str) for col in nodeprop_dataset_list]):
                    nodeprop_valid_submission_list.append({col: row[col] for col in relevant_column + nodeprop_dataset_list})
                else:
                    print('all nan')
                    print(row['Method name'])
            elif row[task_question] == 'Link Property Prediction':
                if any([isinstance(row[col], str) for col in linkprop_dataset_list]):
                    linkprop_valid_submission_list.append({col: row[col] for col in relevant_column + linkprop_dataset_list})
                else:
                    print('all nan')
                    print(row['Method name'])
            elif row[task_question] == 'Graph Property Prediction':
                if any([all([isinstance(row[col], str) for col in graphprop_mol_dataset_list])] + [not isinstance(row[col], str) for col in graphprop_other_dataset_list]):
                    graphprop_valid_submission_list.append({col: row[col] for col in relevant_column + graphprop_mol_dataset_list + graphprop_other_dataset_list})
                else:
                    print('all nan')
                    print(row['Method name'])


    ### make leaderboards for graph property prediction. Currently, we only have molecule data.
    graph_leaderboard_dict = get_mol_leaderboard(graphprop_valid_submission_list)
    insert_leaderboard('_leader_graphprop_scaf.md', 'leader_graphprop.md', graph_leaderboard_dict)

    ### make leaderboards for node property prediction
    node_leaderboard_dict = dict()
    for dataset in nodeprop_dataset_list:
        leaderboard = get_default_leaderboard(dataset, nodeprop_valid_submission_list, dataset2metric[dataset])
        node_leaderboard_dict[dataset] = leaderboard

    insert_leaderboard('_leader_nodeprop_scaf.md', 'leader_nodeprop.md', node_leaderboard_dict)

    ### make leaderboards for link property prediction
    link_leaderboard_dict = dict()
    for dataset in linkprop_dataset_list:
        leaderboard = get_default_leaderboard(dataset, linkprop_valid_submission_list, dataset2metric[dataset])
        link_leaderboard_dict[dataset] = leaderboard

    insert_leaderboard('_leader_linkprop_scaf.md', 'leader_linkprop.md', link_leaderboard_dict)


