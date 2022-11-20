import numpy as np
import torch
import os
from ogb.lsc import MAG240MEvaluator, WikiKG90Mv2Evaluator, PCQM4Mv2Evaluator

mag_evaluator = MAG240MEvaluator()
wikikg_evaluator = WikiKG90Mv2Evaluator()
pcqm_evaluator = PCQM4Mv2Evaluator()

test_label_dir = '/Users/weihua/Documents/lab/research/ogb-lsc/leaderboard_sample/groundtruth_files/'
dataset_list = ['mag240m', 'wikikg90m', 'pcqm4m']
dataset_mapping = {'mag240m': 'MAG240M', 'wikikg90m': 'WikiKG90Mv2', 'pcqm4m': 'PCQM4Mv2'}
filename_mapping = {'mag240m': 'y_pred_mag240m_test-challenge.npz', 'wikikg90m': 't_pred_wikikg90m-v2_test-challenge.npz', 'pcqm4m': 'y_pred_pcqm4m-v2_test-challenge.npz'}
test_filename_mapping = {'mag240m': 'y_true_mag240m_test-challenge.npy', 'wikikg90m': 't_true_wikikg90m-v2_test-challenge.npy', 'pcqm4m': 'y_true_pcqm4m-v2_test-challenge.npy'}
metric_mapping = {'mag240m': 'Accuracy', 'wikikg90m': 'MRR', 'pcqm4m': 'MAE'}

def eval_mag240m(pred_filename, y_true):
    try:
        y_pred = np.load(pred_filename)['y_pred']
    except:
        return 0
    
    acc = mag_evaluator.eval(
    {
        'y_pred': y_pred,
        'y_true': y_true
    }
    )['acc']
    
    return acc

def eval_wikikg90mv2(pred_filename, t_true):
    try:
        t_pred_top10 = np.load(pred_filename)['t_pred_top10']
    except:
        return 0
    
    mrr = wikikg_evaluator.eval({'h,r->t': {'t': t_true, 't_pred_top10': t_pred_top10}})['mrr']
    
    return mrr
    
def eval_pcqm4mv2(pred_filename, y_true):
    try:
        y_pred = np.load(pred_filename)['y_pred']
    except:
        return 12345
    mae = pcqm_evaluator.eval(
        {
            'y_pred': y_pred,
            'y_true': y_true,
        }
    )['mae']

    return mae

def eval_wrapper(dataset, pred_filename, label_true):
    if dataset == 'mag240m':
        return eval_mag240m(pred_filename, label_true)
    elif dataset == 'wikikg90m':
        return eval_wikikg90mv2(pred_filename, label_true)
    elif dataset == 'pcqm4m':
        return eval_pcqm4mv2(pred_filename, label_true)

def get_info(dataset):
    # get performance, team name and email address
    dir = 'lsc_submission/neurips2022'
    
    label_true = np.load(os.path.join(test_label_dir, test_filename_mapping[dataset]))
    print(label_true)

    perf_list = []
    team_list = []
    email_list = []

    for folder in os.listdir(os.path.join(dir, dataset_mapping[dataset])):
        if '@' not in folder:
            continue
        pred_filename = os.path.join(dir, dataset_mapping[dataset], folder, filename_mapping[dataset])
        info_filename = os.path.join(dir, dataset_mapping[dataset], folder, 'info.txt')
        with open(info_filename, 'r') as f:
            for line in f.read().split('\n'):
                if 'Team name:' in line:
                    team_name = line[11:]
        perf = eval_wrapper(dataset, pred_filename, label_true)

        perf_list.append(perf)
        team_list.append(team_name)
        email_list.append(folder)

    return perf_list, team_list, email_list

def process_submissions(perf_list, team_list, email_list, dataset):
    
    if len(perf_list) > 0:
        perf_list = np.array(perf_list)
        metric = metric_mapping[dataset]
        if metric == 'MAE':
            ## from small to large
            sorted_ind_list = np.argsort(perf_list)
        else:
            ## from large to small
            sorted_ind_list = np.argsort(-perf_list)
            
        # header = f'| Rank  | Team | Email | Test {metric} \n'
        # header += '|:----:|:-----:|:------:|:------:|\n'

        header = f'| Rank  | Team | Test {metric} \n'
        header += '|:----:|:-----:|:------:|\n'

        current_ranking = 1

        for i, ind in enumerate(sorted_ind_list):
            perf = float(perf_list[ind])
            team = team_list[ind]
            email = email_list[ind]
            if perf == 0 or perf == 12345:
                # header += '|  {}  |  {}  | {} | Invalid  |\n'.format(current_ranking, team, email, perf)
                header += '|  {}  |  {}  | Invalid  |\n'.format(current_ranking, team, perf)
            else:
                # header += '|  {}  |  {}  | {} | {:.4f}  |\n'.format(current_ranking, team, email, perf) 
                header += '|  {}  |  {}  | {:.4f}  |\n'.format(current_ranking, team, perf)  

            if i < len(sorted_ind_list) - 1 and '{:.4f}'.format(perf_list[ind]) != '{:.4f}'.format(perf_list[sorted_ind_list[i+1]]):
                current_ranking += 1
    else:
        header = f'| Rank  | Team | Test {metric} \n'

    return header


def main():

    ### create leaderboard_dict
    leaderboard_dict = {}    
    for dataset in dataset_list:
        print()
        print(dataset)
        perf_list, team_list, email_list = get_info(dataset)
        print(perf_list)
        print(team_list)
        print(email_list)
        header = process_submissions(perf_list, team_list, email_list, dataset)
        leaderboard_dict[dataset] = header
        
        print(header)

    # # source scaffold file
    # with open('_docs/neurips2022/_leaderboard.md', 'r') as f:
    #     source = f.read().split('\n')

    # dest = []
    # for line in source:
    #     if line[1:] in leaderboard_dict:
    #         dest.append(leaderboard_dict[line[1:]])
    #     else:
    #         dest.append(line)

    # destination file
    # with open('_docs/neurips2022/results.md', 'w') as f:
    #     f.write('\n'.join(dest))


if __name__ == '__main__':
    # first copy from the public submission
    # scp -r weihuahu@ogb-save:/opt/ogb-lsc/data/neurips2022 lsc_submission/
    main()