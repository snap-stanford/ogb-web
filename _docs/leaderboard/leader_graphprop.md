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
##### The ROC-AUC score on the test set. The higher, the better. 

#### Package: >=1.1.1

| Rank  | Method | ROC-AUC | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **HIMP**  | 0.7880 ± 0.0082   | [Matthias Fey](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/2006.12179), [Code](https://github.com/rusty1s/himp-gnn) | 153,029 | GeForce RTX 2080 (11GB GPU) | Jun 22, 2020 |
|  2  |  **DeeperGCN**  | 0.7858 ± 0.0117   | [Guohao Li - DeepGCNs.org](mailto:guohao.li@kaust.edu.sa) | [Paper](https://arxiv.org/abs/2006.07739), [Code](https://github.com/lightaime/deep_gcns_torch/tree/master/examples/ogb) | 531,976 | NVIDIA Tesla V100 (32GB GPU) | Jun 16, 2020 |
|  3  |  **GatedGCN**  | 0.7765 ± 0.0050   | [Chaitanya Joshi](mailto:chaitanya.joshi@ntu.edu.sg) | [Paper](https://arxiv.org/abs/2003.00982), [Code](https://github.com/chaitjo/ogb/tree/master/examples/graphproppred/mol) | [Please tell us](mailto:ogb@cs.stanford.edu) | [Please tell us](mailto:ogb@cs.stanford.edu) | May 9, 2020 |
|  4  |  **WEGL**  | 0.7757 ± 0.0111   | [Navid Naderializadeh](mailto:nnaderializadeh@hrl.com) | [Paper](https://arxiv.org/abs/2006.09430), [Code](https://github.com/navid-naderi/WEGL) | [Please tell us](mailto:ogb@cs.stanford.edu) | NVIDIA Tesla P100 (16GB GPU) | Jun 26, 2020 |
|  5  |  **GIN+virtual node**  | 0.7707 ± 0.0149   | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1810.00826), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/mol) | 3,336,306 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  6  |  GCN  | 0.7606 ± 0.0097   | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/mol) | 527,701 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  7  |  GCN+virtual node  | 0.7599 ± 0.0119   | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/mol) | 1,978,801 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  8  |  **GIN**  | 0.7558 ± 0.0140   | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1810.00826), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/mol) | 1,885,206 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  9  |  **Graph-agnostic MLP**  | 0.6819 ± 0.0071   | [Chaitanya Joshi](mailto:chaitanya.joshi@ntu.edu.sg) | [Paper](https://arxiv.org/abs/2003.00982), [Code](https://github.com/chaitjo/ogb/tree/master/examples/graphproppred/mol) | [Please tell us](mailto:ogb@cs.stanford.edu) | [Please tell us](mailto:ogb@cs.stanford.edu) | May 9, 2020 |


<a name="ogbg-molpcba"/>

-----------------

### Leaderboard for [ogbg-molpcba](../graphprop/#ogbg-mol)
##### The PRC-AUC score on the test set. The higher, the better. 

#### Package: >=1.1.1

| Rank  | Method | PRC-AUC | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **HIMP**  | 0.2739 ± 0.0017   | [Matthias Fey](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/2006.12179), [Code](https://github.com/rusty1s/himp-gnn) | 3,224,534 | GeForce RTX 2080 (11GB GPU) | Jun 22, 2020 |
|  2  |  **GIN+virtual node**  | 0.2655 ± 0.0027   | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1810.00826), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/mol) | 3,374,533 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  3  |  GCN+virtual node  | 0.2397 ± 0.0023   | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/mol) | 2,017,028 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  4  |  **GIN**  | 0.2217 ± 0.0023   | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1810.00826), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/mol) | 1,923,433 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  5  |  **GatedGCN**  | 0.2077 ± 0.0027   | [Chaitanya Joshi](mailto:chaitanya.joshi@ntu.edu.sg) | [Paper](https://arxiv.org/abs/2003.00982), [Code](https://github.com/chaitjo/ogb/tree/master/examples/graphproppred/mol) | [Please tell us](mailto:ogb@cs.stanford.edu) | [Please tell us](mailto:ogb@cs.stanford.edu) | May 12, 2020 |
|  6  |  GCN  | 0.1983 ± 0.0016   | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/mol) | 565,928 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  7  |  **Graph-agnostic MLP**  | 0.0823 ± 0.0004   | [Chaitanya Joshi](mailto:chaitanya.joshi@ntu.edu.sg) | [Paper](https://arxiv.org/abs/2003.00982), [Code](https://github.com/chaitjo/ogb/tree/master/examples/graphproppred/mol) | [Please tell us](mailto:ogb@cs.stanford.edu) | [Please tell us](mailto:ogb@cs.stanford.edu) | May 12, 2020 |


<a name="ogbg-ppa"/>

---------------------

### Leaderboard for [ogbg-ppa](../graphprop/#ogbg-ppa)
##### The multi-class classification accuracy on the test set. The higher, the better. 

#### Package: >=1.1.1

| Rank  | Method | Accuracy | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **DeeperGCN**  | 0.7712 ± 0.0071   | [Guohao Li - DeepGCNs.org](mailto:guohao.li@kaust.edu.sa) | [Paper](https://arxiv.org/abs/2006.07739), [Code](https://github.com/lightaime/deep_gcns_torch/tree/master/examples/ogb) | 2,336,421 | NVIDIA Tesla V100 (32GB GPU) | Jun 16, 2020 |
|  2  |  **GIN+virtual node**  | 0.7037 ± 0.0107   | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1810.00826), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/ppa) | 3,288,042 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  3  |  **GIN**  | 0.6892 ± 0.0100   | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1810.00826), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/ppa) | 1,836,942 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  4  |  GCN+virtual node  | 0.6857 ± 0.0061   | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/ppa) | 1,930,537 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  5  |  GCN  | 0.6839 ± 0.0084   | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/ppa) | 479,437 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |



<a name="ogbg-code"/>

---------------------

### Leaderboard for [ogbg-code](../graphprop/#ogbg-code)
##### The F1 score on the test set. The higher, the better. 

#### Package: >=1.2.0

| Rank  | Method | F1 score | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  GCN+virtual node  | 0.3263 ± 0.0013   | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/code) | 12,476,210 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |
|  2  |  **GIN+virtual node**  | 0.3204 ± 0.0018   | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1810.00826), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/code) | 13,833,715 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |
|  3  |  GCN  | 0.3163 ± 0.0018   | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/code) | 11,025,110 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |
|  3  |  **GIN**  | 0.3163 ± 0.0020   | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1810.00826), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/code) | 12,382,615 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |
