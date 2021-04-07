import numpy as np
import os

init_dir = 'lsc_submission/prelim/'
final_dir = 'lsc_submission/prelim/'
test_label_path = '/Users/weihua/Documents/lab/research/ogb-lsc/testset'
dataset_list = ['mag240m', 'wikikg90m', 'pcqm4m']

np.random.seed(42)

def eval_mag240m(filename, y_true):
    y_pred = np.load(filename)['y_pred']
    return (y_true == y_pred).sum() / y_true.shape[0]

def eval_wikikg90m(filename, test_t_correct_index):
    pred = np.load(filename)
    pred_dict = {'h,r->t': {'t_pred_top10': pred['t_pred_top10'], 't_correct_index': test_t_correct_index}}
    metrics = evaluator.eval(pred_dict)
    return metrics['mrr']

def eval_pcqm4m(filename, y_true):
    y_pred = np.load(filename)['y_pred']
    return np.average(np.absolute(y_true - y_pred))

def main(dir, coming_soon_initial = True, coming_soon_final = True):

    ### create leaderboard_dict
    ### initial
    leaderboard_dict = {}
    for dataset in dataset_list:
        key = f'initial_{dataset}'
        if coming_soon_initial:
            leaderboard_dict[key] = '##### Coming soon...'
        else:
            leaderboard_dict[key] = '##### Tmp'
    
    for dataset in dataset_list:
        key = f'final_{dataset}'
        if coming_soon_initial:
            leaderboard_dict[key] = '##### Coming soon...'
        else:
            leaderboard_dict[key] = '##### Tmp'

    # source scaffold file
    with open('_docs/kddcup2021/_leaderboard.md', 'r') as f:
        source = f.read().split('\n')

    dest = []
    for line in source:
        if line[1:] in leaderboard_dict:
            dest.append(leaderboard_dict[line[1:]])
        else:
            dest.append(line)

    # destination file
    with open('_docs/kddcup2021/leaderboard.md', 'w') as f:
        f.write('\n'.join(dest))


if __name__ == '__main__':
    # first copy from the public submission
    # scp -r weihuahu@ogb-save:/opt/ogb-lsc/data/prelim lsc_submission/
    main(dir)