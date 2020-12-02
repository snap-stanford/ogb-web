---
title: Leaderboards for Graph Property Prediction
permalink: /docs/leader_graphprop/
---

##### Check leaderboards for
###### - [ogbg-molhiv](#ogbg-molhiv)
###### - [ogbg-molpcba](#ogbg-molpcba)
###### - [ogbg-ppa](#ogbg-ppa)
###### - [ogbg-code](#ogbg-code)

The **bold** method name indicates that the implementation is **official** (by the author of the original paper). <br/>
**Package** denotes the required package version for each dataset to be eligible for the leaderboard.

<a name="ogbg-molhiv"/>

-------------

### Leaderboard for [ogbg-molhiv](../graphprop/#ogbg-mol)
##### The ROC-AUC score on the test and validation sets. The higher, the better. 

#### Package: >=1.1.1

| Rank  | Method | Test ROC-AUC | Validation ROC-AUC | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **MorganFP+Rand. Forest**  | 0.8060 ± 0.0010   | 0.8420 ± 0.0030 |[Cyrus Maher](mailto:cmaher@vir.bio) | [Paper](https://pubs.acs.org/doi/10.1021/ci100050t), [Code](https://github.com/cyrusmaher/ogb-molecule-comp) | 230,000 | CPU | Sep 21, 2020 |
|  2  |  **DeeperGCN+FLAG**  | 0.7942 ± 0.0120   | 0.8425 ± 0.0061 |[Kezhi Kong](mailto:kong@cs.umd.edu) | [Paper](https://arxiv.org/abs/2010.09891), [Code](https://github.com/devnkong/FLAG) | 531,976 | NVIDIA Tesla V100 (32GB GPU) | Oct 20, 2020 |
|  3  |  **PNA**  | 0.7905 ± 0.0132   | 0.8519 ± 0.0099 |[Gabriele Corso](mailto:gc579@cam.ac.uk) | [Paper](https://arxiv.org/abs/2004.05718), [Code](https://github.com/lukecavabarrett/pna) | 326,081 | NVIDIA Tesla T4 (15GB GPU) | Nov 25, 2020 |
|  4  |  **GCN+GraphNorm**  | 0.7883 ± 0.0100   | 0.7904 ± 0.0115 |[Shengjie Luo](mailto:shengjie.luo@outlook.com) | [Paper](https://arxiv.org/abs/2009.03294), [Code](https://github.com/lsj2408/GraphNorm) | 526,201 | NVIDIA Tesla P100 (16GB GPU) | Sep 16, 2020 |
|  5  |  **HIMP**  | 0.7880 ± 0.0082   | [Please tell us](mailto:ogb@cs.stanford.edu) |[Matthias Fey](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/2006.12179), [Code](https://github.com/rusty1s/himp-gnn) | 153,029 | GeForce RTX 2080 (11GB GPU) | Jun 22, 2020 |
|  6  |  **DeeperGCN**  | 0.7858 ± 0.0117   | 0.8427 ± 0.0063 |[Guohao Li - DeepGCNs.org](mailto:guohao.li@kaust.edu.sa) | [Paper](https://arxiv.org/abs/2006.07739), [Code](https://github.com/lightaime/deep_gcns_torch/tree/master/examples/ogb) | 531,976 | NVIDIA Tesla V100 (32GB GPU) | Jun 16, 2020 |
|  7  |  **WEGL**  | 0.7757 ± 0.0111   | 0.8101 ± 0.0097 |[Navid Naderializadeh](mailto:nnaderializadeh@hrl.com) | [Paper](https://arxiv.org/abs/2006.09430), [Code](https://github.com/navid-naderi/WEGL) | 361,064 | NVIDIA Tesla P100 (16GB GPU) | Jun 26, 2020 |
|  8  |  **GIN+virtual node+FLAG**  | 0.7748 ± 0.0096   | 0.8438 ± 0.0128 |[Kezhi Kong](mailto:kong@cs.umd.edu) | [Paper](https://arxiv.org/abs/2010.09891), [Code](https://github.com/devnkong/FLAG) | 3,336,306 | GeForce RTX 2080 Ti (11GB GPU) | Oct 20, 2020 |
|  9  |  **GIN+virtual node**  | 0.7707 ± 0.0149   | 0.8479 ± 0.0068 |[Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1810.00826), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/mol) | 3,336,306 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  10  |  **GCN+FLAG**  | 0.7683 ± 0.0102   | 0.8176 ± 0.0087 |[Kezhi Kong](mailto:kong@cs.umd.edu) | [Paper](https://arxiv.org/abs/2010.09891), [Code](https://github.com/devnkong/FLAG) | 527,701 | GeForce RTX 2080 Ti (11GB GPU) | Oct 20, 2020 |
|  11  |  **GIN+FLAG**  | 0.7654 ± 0.0114   | 0.8225 ± 0.0155 |[Kezhi Kong](mailto:kong@cs.umd.edu) | [Paper](https://arxiv.org/abs/2010.09891), [Code](https://github.com/devnkong/FLAG) | 1,885,206 | GeForce RTX 2080 Ti (11GB GPU) | Oct 20, 2020 |
|  12  |  GCN  | 0.7606 ± 0.0097   | 0.8204 ± 0.0141 | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/mol) | 527,701 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  13  |  GCN+virtual node  | 0.7599 ± 0.0119   | 0.8384 ± 0.0091 | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/mol) | 1,978,801 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  14  |  **GIN**  | 0.7558 ± 0.0140   | 0.8232 ± 0.0090 |[Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1810.00826), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/mol) | 1,885,206 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |


<a name="ogbg-molpcba"/>

-----------------

### Leaderboard for [ogbg-molpcba](../graphprop/#ogbg-mol)
##### The Average Precision (AP) score on the test and validation sets. The higher, the better. 
**Note: The evaluation metric has been changed from PRC-AUC (Aug 11, 2020).**

#### Package: >=1.2.2

| Rank  | Method | Test AP | Validation AP | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **GINE+**  | 0.2917 ± 0.0015   | 0.3065 ± 0.0030 |[Rémy Brossard](mailto:remy@anotherbrain.ai) | [Paper](https://arxiv.org/abs/2011.15069), [Code](https://github.com/RBrossard/GINEPLUS) | 6,147,029 | GeForce GTX 1080 Ti | Dec 1, 2020 |
|  2  |  **DeeperGCN+virtual node+FLAG**  | 0.2842 ± 0.0043   | 0.2952 ± 0.0029 |[Kezhi Kong](mailto:kong@cs.umd.edu) | [Paper](https://arxiv.org/abs/2010.09891), [Code](https://github.com/devnkong/FLAG) | 5,550,208 | NVIDIA Tesla V100 (32GB GPU) | Oct 21, 2020 |
|  3  |  **GIN+virtual node+FLAG**  | 0.2834 ± 0.0038   | 0.2912 ± 0.0026 |[Kezhi Kong](mailto:kong@cs.umd.edu) | [Paper](https://arxiv.org/abs/2010.09891), [Code](https://github.com/devnkong/FLAG) | 3,374,533 | GeForce RTX 2080 Ti (11GB GPU) | Oct 21, 2020 |
|  4  |  **DeeperGCN+virtual node**  | 0.2781 ± 0.0038   | 0.2920 ± 0.0025 |[Guohao Li - DeepGCNs.org](mailto:guohao.li@kaust.edu.sa) | [Paper](https://arxiv.org/abs/2006.07739), [Code](https://github.com/lightaime/deep_gcns_torch/tree/master/examples/ogb) | 5,550,208 | NVIDIA Tesla V100 (32GB GPU) | Aug 11, 2020 |
|  5  |  **GIN+virtual node**  | 0.2703 ± 0.0023   | 0.2798 ± 0.0025 |[Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1810.00826), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/mol) | 3,374,533 | GeForce RTX 2080 (11GB GPU) | Aug 11, 2020 |
|  6  |  **GCN+virtual node+FLAG**  | 0.2483 ± 0.0037   | 0.2556 ± 0.0040 |[Kezhi Kong](mailto:kong@cs.umd.edu) | [Paper](https://arxiv.org/abs/2010.09891), [Code](https://github.com/devnkong/FLAG) | 2,017,028 | GeForce RTX 2080 Ti (11GB GPU) | Oct 21, 2020 |
|  7  |  GCN+virtual node  | 0.2424 ± 0.0034   | 0.2495 ± 0.0042 | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/mol) | 2,017,028 | GeForce RTX 2080 (11GB GPU) | Aug 11, 2020 |
|  8  |  **GIN+FLAG**  | 0.2395 ± 0.0040   | 0.2451 ± 0.0042 |[Kezhi Kong](mailto:kong@cs.umd.edu) | [Paper](https://arxiv.org/abs/2010.09891), [Code](https://github.com/devnkong/FLAG) | 1,923,433 | GeForce RTX 2080 Ti (11GB GPU) | Oct 21, 2020 |
|  9  |  **GIN**  | 0.2266 ± 0.0028   | 0.2305 ± 0.0027 |[Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1810.00826), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/mol) | 1,923,433 | GeForce RTX 2080 (11GB GPU) | Aug 11, 2020 |
|  10  |  **GCN+FLAG**  | 0.2116 ± 0.0017   | 0.2150 ± 0.0022 |[Kezhi Kong](mailto:kong@cs.umd.edu) | [Paper](https://arxiv.org/abs/2010.09891), [Code](https://github.com/devnkong/FLAG) | 565,928 | GeForce RTX 2080 Ti (11GB GPU) | Oct 21, 2020 |
|  11  |  **MorganFP+Rand. Forest**  | 0.2054 ± 0.0004   | 0.2226 ± 0.0002 |[Cyrus Maher](mailto:cmaher@vir.bio) | [Paper](https://pubs.acs.org/doi/10.1021/ci100050t), [Code](https://github.com/cyrusmaher/ogb-molecule-comp) | 29,440,000 | CPU | Sep 21, 2020 |
|  12  |  GCN  | 0.2020 ± 0.0024   | 0.2059 ± 0.0033 | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/mol) | 565,928 | GeForce RTX 2080 (11GB GPU) | Aug 11, 2020 |


<a name="ogbg-ppa"/>

---------------------

### Leaderboard for [ogbg-ppa](../graphprop/#ogbg-ppa)
##### The multi-class classification accuracy on the test and validation sets. The higher, the better. 

#### Package: >=1.1.1

| Rank  | Method | Test Accuracy | Validation Accuracy | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **DeeperGCN+FLAG**  | 0.7752 ± 0.0069   | 0.7484 ± 0.0052 |[Kezhi Kong](mailto:kong@cs.umd.edu) | [Paper](https://arxiv.org/abs/2010.09891), [Code](https://github.com/devnkong/FLAG) | 2,336,421 | NVIDIA Tesla V100 (32GB GPU) | Oct 21, 2020 |
|  2  |  **DeeperGCN**  | 0.7712 ± 0.0071   | 0.7313 ± 0.0078 |[Guohao Li - DeepGCNs.org](mailto:guohao.li@kaust.edu.sa) | [Paper](https://arxiv.org/abs/2006.07739), [Code](https://github.com/lightaime/deep_gcns_torch/tree/master/examples/ogb) | 2,336,421 | NVIDIA Tesla V100 (32GB GPU) | Jun 16, 2020 |
|  3  |  **GIN+virtual node+FLAG**  | 0.7245 ± 0.0114   | 0.6789 ± 0.0079 |[Kezhi Kong](mailto:kong@cs.umd.edu) | [Paper](https://arxiv.org/abs/2010.09891), [Code](https://github.com/devnkong/FLAG) | 3,288,042 | GeForce RTX 2080 Ti (11GB GPU) | Oct 21, 2020 |
|  4  |  **GIN+virtual node**  | 0.7037 ± 0.0107   | 0.6678 ± 0.0105 |[Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1810.00826), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/ppa) | 3,288,042 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  5  |  **GCN+virtual node+FLAG**  | 0.6944 ± 0.0052   | 0.6638 ± 0.0055 |[Kezhi Kong](mailto:kong@cs.umd.edu) | [Paper](https://arxiv.org/abs/2010.09891), [Code](https://github.com/devnkong/FLAG) | 1,930,537 | GeForce RTX 2080 Ti (11GB GPU) | Oct 21, 2020 |
|  6  |  **GIN+FLAG**  | 0.6905 ± 0.0092   | 0.6465 ± 0.0070 |[Kezhi Kong](mailto:kong@cs.umd.edu) | [Paper](https://arxiv.org/abs/2010.09891), [Code](https://github.com/devnkong/FLAG) | 1,836,942 | GeForce RTX 2080 Ti (11GB GPU) | Oct 21, 2020 |
|  7  |  **GIN**  | 0.6892 ± 0.0100   | 0.6562 ± 0.0107 |[Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1810.00826), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/ppa) | 1,836,942 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  8  |  GCN+virtual node  | 0.6857 ± 0.0061   | 0.6511 ± 0.0048 | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/ppa) | 1,930,537 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  9  |  GCN  | 0.6839 ± 0.0084   | 0.6497 ± 0.0034 | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/ppa) | 479,437 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |



<a name="ogbg-code"/>

---------------------

### Leaderboard for [ogbg-code](../graphprop/#ogbg-code)
##### The F1 score on the test and validation sets. The higher, the better. 

#### Package: >=1.2.0

| Rank  | Method | Test F1 score | Validation F1 score | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **GCN+virtual node+FLAG**  | 0.3316 ± 0.0025   | 0.3099 ± 0.0016 |[Kezhi Kong](mailto:kong@cs.umd.edu) | [Paper](https://arxiv.org/abs/2010.09891), [Code](https://github.com/devnkong/FLAG) | 12,476,210 | GeForce RTX 2080 Ti (11GB GPU) | Oct 21, 2020 |
|  2  |  **GIN+virtual node+FLAG**  | 0.3296 ± 0.0036   | 0.3092 ± 0.0035 |[Kezhi Kong](mailto:kong@cs.umd.edu) | [Paper](https://arxiv.org/abs/2010.09891), [Code](https://github.com/devnkong/FLAG) | 13,833,715 | GeForce RTX 2080 Ti (11GB GPU) | Oct 21, 2020 |
|  3  |  GCN+virtual node  | 0.3263 ± 0.0013   | 0.3062 ± 0.0007 | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/code) | 12,476,210 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |
|  4  |  **GIN+FLAG**  | 0.3241 ± 0.0040   | 0.3044 ± 0.0039 |[Kezhi Kong](mailto:kong@cs.umd.edu) | [Paper](https://arxiv.org/abs/2010.09891), [Code](https://github.com/devnkong/FLAG) | 12,382,615 | GeForce RTX 2080 Ti (11GB GPU) | Oct 21, 2020 |
|  5  |  **GCN+FLAG**  | 0.3209 ± 0.0019   | 0.3016 ± 0.0016 |[Kezhi Kong](mailto:kong@cs.umd.edu) | [Paper](https://arxiv.org/abs/2010.09891), [Code](https://github.com/devnkong/FLAG) | 11,025,110 | GeForce RTX 2080 Ti (11GB GPU) | Oct 21, 2020 |
|  6  |  **GIN+virtual node**  | 0.3204 ± 0.0018   | 0.3020 ± 0.0016 |[Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1810.00826), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/code) | 13,833,715 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |
|  7  |  GCN  | 0.3163 ± 0.0018   | 0.2973 ± 0.0014 | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/code) | 11,025,110 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |
|  7  |  **GIN**  | 0.3163 ± 0.0020   | 0.2981 ± 0.0014 |[Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1810.00826), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/code) | 12,382,615 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |
